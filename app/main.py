import os
from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse
from .routers import properties

from fastapi_mcp import FastApiMCP

app = FastAPI(
    title="房地產查詢 API",
    description="提供多條件查詢房地產資料的 RESTful API",
    version="1.0.0"
)

app.include_router(properties.router)


# 掛載 MCP 伺服器
mcp = FastApiMCP(
    app,
    name="房地產查詢 API MCP",
    description="將 FastAPI 查詢 API 自動轉換為 MCP 工具",
    base_url="http://localhost:8000"
)
mcp.mount()