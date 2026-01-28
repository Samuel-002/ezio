import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from urllib.parse import urlparse, parse_qs
import re, requests

COMMON = {"id", "uid", "user", "token", "next", "redirect"}

def mine_params(url):
    params = set(parse_qs(urlparse(url).query).keys())
    try:
        html = requests.get(url, timeout=10, verify=False).text
        params.update(re.findall(r'[?&]([a-zA-Z_]{2,15})=', html))
    except Exception:
        pass
    return list(params | COMMON)
