from clients.http_cat_client import HttpCatClient
from utils.html_parser import get_h1_text


def test_status_endpoint_without_code():
    response = HttpCatClient.get_status_root()

    assert response.status_code == 403
    assert "text/html" in response.headers["Content-Type"]

    assert get_h1_text(response.text) == "403 Forbidden"
