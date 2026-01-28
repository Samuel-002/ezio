import requests

def header_scan(url):
    r = requests.get(url, timeout=10)
    missing = []

    for h in [
        "Content-Security-Policy",
        "X-Frame-Options",
        "Strict-Transport-Security"
    ]:
        if h not in r.headers:
            missing.append(h)

    return {
        "status": r.status_code,
        "missing_headers": missing
    }
