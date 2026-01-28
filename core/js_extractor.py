import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import re, requests
from urllib.parse import urljoin
from core.scope import in_scope

JS_REGEX = r'src=["\'](.*?\.js)["\']'
EP_REGEX = r'["\'](\/api\/[^"\']+|\/[^"\']+)["\']'

def extract_js(url, domain):
    try:
        html = requests.get(url, timeout=10, verify=False).text
    except Exception:
        return []

    endpoints = set()
    for js in re.findall(JS_REGEX, html):
        js_url = urljoin(url, js)
        if not in_scope(domain, js_url):
            continue
        try:
            code = requests.get(js_url, timeout=10, verify=False).text
            endpoints.update(re.findall(EP_REGEX, code))
        except Exception:
            pass

    return list(endpoints)
