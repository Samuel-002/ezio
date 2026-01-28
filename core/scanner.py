import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import requests

def header_scan(url):
    try:
        r = requests.get(url, timeout=10, verify=False)
        missing = [
            h for h in [
                "Content-Security-Policy",
                "X-Frame-Options",
                "Strict-Transport-Security"
            ] if h not in r.headers
        ]
        return {"status": r.status_code, "missing_headers": missing}
    except Exception as e:
        return {"error": str(e)}
