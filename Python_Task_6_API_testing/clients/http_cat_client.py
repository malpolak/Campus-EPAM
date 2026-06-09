import requests


class HttpCatClient:
    BASE_URL = "https://http.cat"

    @classmethod
    def get_status_page(cls, status_code):
        return requests.get(
            f'{cls.BASE_URL}/status/{status_code}',
            timeout=10
        )

    @classmethod
    def get_status_root(cls):
        return requests.get(
            f"{cls.BASE_URL}/status",
            timeout=10
        )
