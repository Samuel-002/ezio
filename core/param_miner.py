from urllib.parse import urlparse, parse_qs
import re, requests

COMMON = {"id", "uid", "user", "token", "next", "redirect"}

def mine_params(url):
    params = set(parse_qs(urlparse(url).query).keys())
    html = requests.get(url, timeout=10).text
    params.update(re.findall(r'[?&]([a-zA-Z_]{2,15})=', html))
    return list(params | COMMON)
