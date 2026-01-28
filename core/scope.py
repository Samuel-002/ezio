from urllib.parse import urlparse

def in_scope(base_domain, url):
    return urlparse(url).netloc.endswith(base_domain)
