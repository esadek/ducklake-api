from typing import Any

from pydantic import BaseModel


class QueryResponse(BaseModel):
    sql: str
    rows: list[dict[str, Any]]
    timestamp: str
