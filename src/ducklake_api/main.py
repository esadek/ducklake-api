from datetime import datetime, timezone

from duckdb import DuckDBPyConnection
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.responses import HTMLResponse
from scalar_fastapi import get_scalar_api_reference
from uvicorn import run

from ducklake_api.ducklake import get_connection
from ducklake_api.models import QueryResponse

app = FastAPI(
    title="DuckLake API",
    description="A simple REST API for DuckLake",
)


@app.post("/query")
def query_ducklake(sql: str, con: DuckDBPyConnection = Depends(get_connection)) -> QueryResponse:
    """Execute a SQL query against DuckLake and return the results."""
    try:
        result = con.sql(sql)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    rows = []
    if result:
        rows = result.to_arrow_table().to_pylist()
    timestamp = datetime.now(timezone.utc).isoformat()
    return QueryResponse(sql=sql, rows=rows, timestamp=timestamp)


@app.get("/", include_in_schema=False)
async def scalar_html() -> HTMLResponse:
    return get_scalar_api_reference(
        openapi_url=app.openapi_url,
        title=app.title,
        default_open_all_tags=True,
    )


if __name__ == "__main__":
    run(app=app, host="0.0.0.0", port=8000)
