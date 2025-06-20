from unittest.mock import MagicMock, patch

import pytest

from ducklake_api.ducklake import get_connection


@patch("ducklake_api.ducklake.connect")
def test_get_connection(mock_connect) -> None:
    mock_con = MagicMock()
    mock_connect.return_value.__enter__.return_value = mock_con

    gen = get_connection()
    con = next(gen)

    mock_con.install_extension.assert_called_once_with("ducklake")
    mock_con.execute.assert_called_with("ATTACH 'ducklake:metadata.ducklake' AS my_ducklake")
    assert con == mock_con

    with pytest.raises(StopIteration):
        next(gen)
