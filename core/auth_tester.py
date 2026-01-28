import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import requests

def auth_diff(url, cookie):
    try:
        r1 = requests.get(url, timeout=10, verify=False)
        r2 = requests.get(url, headers={"Cookie": cookie}, timeout=10, verify=False)
        return r1.text != r2.text
    except Exception:
        return False
