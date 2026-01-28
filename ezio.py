#!/usr/bin/env python3
import argparse
from config import VERSION
from core.banner import show_banner
from core.menu import show_menu
from core.validator import normalize_url, get_domain
from core.scanner import header_scan
from core.js_extractor import extract_js
from core.param_miner import mine_params
from core.auth_tester import auth_diff
from core.chain_builder import build_chain
from core.ai_reasoner import analyze
from core.output import save_json, save_md
from core.theme import info, success

def main():
    parser = argparse.ArgumentParser(prog="ezio")
    parser.add_argument("-v", "--version", action="store_true")
    args, _ = parser.parse_known_args()

    if args.version:
        print(f"EZIO v{VERSION}")
        return

    show_banner()

    url = normalize_url(input("Enter target URL: ").strip())
    domain = get_domain(url)
    results = {}

    choices = show_menu()

    if "0" in choices:
        return

    if "7" in choices:
        choices = ["1", "2", "3", "4", "5", "6"]

    if "1" in choices:
        info("Running header scan")
        results["headers"] = header_scan(url)

    if "2" in choices:
        info("Extracting JS endpoints")
        results["js_endpoints"] = extract_js(url, domain)

    if "3" in choices:
        info("Mining parameters")
        results["params"] = mine_params(url)

    if "4" in choices:
        cookie = input("Enter session cookie: ")
        results["auth_diff"] = auth_diff(url, cookie)

    if "5" in choices:
        info("Building attack chains")
        results["chains"] = build_chain(
            results.get("js_endpoints", []),
            results.get("params", [])
        )

    if "6" in choices:
        info("Running AI analysis")
        results["ai"] = {c: analyze(c) for c in results.get("chains", [])}

    if "8" in choices:
        ep = input("Enter endpoint / URL for manual AI analysis: ")
        results["manual_ai"] = analyze(ep)

    save_json(results)
    save_md(results)
    success("EZIO run completed")

if __name__ == "__main__":
    main()
