from typing import Any, Generator

from duckdb import DuckDBPyConnection, connect


def get_connection() -> Generator[DuckDBPyConnection, Any, None]:
    with connect() as con:
        con.install_extension("ducklake")
        con.execute("ATTACH 'ducklake:metadata.ducklake' AS my_ducklake")
        yield con
