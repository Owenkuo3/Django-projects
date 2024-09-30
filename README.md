創建multi_db_ecommerce專案
使用三個資料庫，安裝並啟用
MongoDB:
用途: 存儲非結構化或半結構化的數據，如商品評論、用戶行為日誌等。
MySQL:
用途: 存儲關係型數據，如用戶資料、商品資訊、訂單紀錄等。
示例資料表:
Redis:
用途: 存儲需要快速存取的數據，如熱門商品排行榜、用戶登入狀態、暫存的購物車資訊等。

創建app, Orders, Products, Shop, Users

創建Orders, Products, Shop, Users的Models
創建tests與signal測試Order
測試Models: Products, Users, 沒有測試Shop
測試完Shop
創建cart app 與 Models
設置好全域的api urls 
創建cart / shop的views (設置API)
透過Django REST framework 設置各app的serializer跟視圖、url等等
