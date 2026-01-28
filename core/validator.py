from urllib.parse import urlparse

def normalize_url(url):
    if not url.startswith("http"):
        url = "https://" + url
    return url.rstrip("/")

def get_domain(url):
    return urlparse(url).netloc
