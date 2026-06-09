from bs4 import BeautifulSoup


def get_h1_text(html_content: str) -> str:
    soup = BeautifulSoup(html_content, "html.parser")

    h1 = soup.find("h1")

    if not h1:
        raise AssertionError("H1 element not found")

    return h1.get_text(strip=True)
