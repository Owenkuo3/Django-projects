from django.test import TestCase
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group, Permission

class CustomUserModelTest(TestCase):

    def setUp(self):
        self.group = Group.objects.create(name='Test Group')
        self.permission = Permission.objects.first() 

        self.user = get_user_model().objects.create_user(
            username='testuser',
            password='password123',
            phone_number='123456789',
            address='123 Test Street',
            birthday='1990-01-01',
            gender='M',
            email='test@example.com',
            email_address='test@example.com',
        )
        self.user.groups.add(self.group)
        self.user.user_permissions.add(self.permission)

    def test_user_creation(self):
        self.assertEqual(self.user.username, 'testuser')
        self.assertTrue(self.user.check_password('password123'))
        self.assertEqual(self.user.phone_number, '123456789')
        self.assertEqual(self.user.address, '123 Test Street')
        self.assertEqual(self.user.birthday, '1990-01-01')
        self.assertEqual(self.user.gender, 'M')
        self.assertEqual(self.user.email, 'test@example.com')
        self.assertEqual(self.user.email_address, 'test@example.com')

    def test_user_str_representation(self):
        self.assertEqual(str(self.user), 'testuser')

    def test_user_update(self):
        self.user.phone_number = '987654321'
        self.user.address = '456 New Address'
        self.user.save()
        self.assertEqual(self.user.phone_number, '987654321')
        self.assertEqual(self.user.address, '456 New Address')

    def test_user_group_and_permission(self):
        self.assertIn(self.group, self.user.groups.all())
        self.assertIn(self.permission, self.user.user_permissions.all())

    def test_user_gender_choice(self):
        self.user.gender = 'F'
        self.user.save()
        self.assertEqual(self.user.gender, 'F')
        with self.assertRaises(ValueError):
            self.user.gender = 'X'  
            self.user.full_clean() 

    def test_user_email_field(self):
        self.user.email_address = 'new_email@example.com'
        self.user.save()
        self.assertEqual(self.user.email_address, 'new_email@example.com')
