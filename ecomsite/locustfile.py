from locust import HttpUser, task, between

class WebsiteUser(HttpUser):
    wait_time = between(1, 5)

    @task
    def view_index(self):
        self.client.get("/")

    @task
    def view_item(self):
        self.client.get("/food/item/")

    @task
    def view_detail(self):
        # 假設你有一個 `item_id` 為 1 的項目
        self.client.get("/food/1/")

    @task
    def create_item(self):
        self.client.post("/create_item/", {
            "name": "New Item",
            "description": "This is a test item.",
            "price": 10
        })

    @task
    def update_item(self):
        # 假設你要更新 `id` 為 1 的項目
        self.client.post("/update_item/1/", {
            "name": "Updated Item",
            "description": "This is an updated test item.",
            "price": 20
        })

    @task
    def delete_item(self):
        # 假設你要刪除 `id` 為 1 的項目
        self.client.post("/delete_item/1/")
