import requests

def auth_diff(url, cookie):
    r1 = requests.get(url, timeout=10)
    r2 = requests.get(url, headers={"Cookie": cookie}, timeout=10)
    return r1.text != r2.text
