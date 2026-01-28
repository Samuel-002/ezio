import re, requests
from urllib.parse import urljoin
from core.scope import in_scope

JS_REGEX = r'src=["\'](.*?\.js)["\']'
EP_REGEX = r'["\'](\/api\/[^"\']+|\/[^"\']+)["\']'

def extract_js(url, base_domain):
    html = requests.get(url, timeout=10).text
    js_files = re.findall(JS_REGEX, html)
    endpoints = set()

    for js in js_files:
        js_url = urljoin(url, js)
        if not in_scope(base_domain, js_url):
            continue

        code = requests.get(js_url, timeout=10).text
        endpoints.update(re.findall(EP_REGEX, code))

    return list(endpoints)
