import pytest

from clients.http_cat_client import HttpCatClient
from utils.html_parser import get_h1_text


@pytest.mark.parametrize(
    "status_code",
    [
        101,
        200,
        301,
        407,
        500,
    ],
)
def test_status_groups(status_code):
    response = HttpCatClient.get_status_page(status_code)

    assert response.status_code == 200
    assert "text/html" in response.headers["Content-Type"]

    # http.cat always returns same H1
    assert get_h1_text(response.text) == "HTTP Cats"
