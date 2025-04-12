# FastAPI 房地產查詢 API

本專案提供一套基於 FastAPI 與 PostgreSQL 的房地產資料查詢 API，支援多條件檢索、分頁、單筆查詢等功能，適合用於房地產資訊平台或資料分析應用。

## 目錄結構
```
app/
  ├── main.py                # FastAPI 入口
  ├── database.py            # 資料庫連線設定
  ├── models.py              # SQLAlchemy 資料表定義
  ├── schemas.py             # Pydantic schema
  └── routers/
      └── properties.py      # 查詢 API 路由
requirements.txt             # 依賴套件
db_test/init.sql             # 資料表與測試資料
```

## 安裝步驟

1. 安裝 Python 3.10+ 與 pip
2. 安裝依賴套件
   ```
   pip install -r requirements.txt
   ```
3. 確認 PostgreSQL 已啟動，並已依 `db_test/init.sql` 建立資料表與測試資料（建議用 docker-compose 啟動）

## 啟動 API 服務

於專案根目錄執行：
```
uvicorn app.main:app --reload
```

## API 文件

啟動後可於瀏覽器開啟 [http://localhost:8000/docs](http://localhost:8000/docs) 查看自動產生的 Swagger API 文件。

## 快速測試

1. 啟動 API 後，可用 curl 測試查詢：
   ```bash
   curl "http://localhost:8000/properties"
   ```
   查詢新北市板橋區：
   ```bash
   curl "http://localhost:8000/properties?city=新北市&district=板橋區"
   ```
   查詢單一物件（請替換為實際 transaction_id）：
   ```bash
   curl "http://localhost:8000/properties/11111111-1111-1111-1111-111111111111"
   ```

2. 或直接於 [http://localhost:8000/docs](http://localhost:8000/docs) 互動測試 API。

## 資料庫連線設定

預設連線字串為：
```
postgresql://postgres:mysecretpassword@localhost:5432/mydb
```
如有需要請於 `app/database.py` 調整。

## MCP 工具存取權限（多用戶 API Key）

API key 會存放於資料庫 `api_keys` 資料表。每個用戶可申請不同的 API key，只有在資料表中且 `is_active=1` 的 key 才能存取 `/mcp` 路徑。

MCP 客戶端存取 `/mcp` 路徑時，必須在 HTTP header 加上：
```
X-API-Key: 你的 API key
```
否則將回傳 401 Unauthorized。

你可直接於 `db_test/init.sql` 新增/管理 API key，或於資料庫中自行增刪。

## 主要 API

- `GET /properties`：多條件查詢（支援分頁、欄位篩選）
- `GET /properties/{transaction_id}`：依 ID 查詢單筆資料