#!/usr/bin/env python3
"""Build the standalone Weekly Management Meeting dashboard.

Usage: python3 build/build.py DATA_DIR PAGE_FILE OUT_FILE [UPDATED_ISO]

PAGE_FILE is the dashboard page HTML (the Claude dashboard's files/index.html "text").

DATA_DIR holds sales_weekly.json, sales_daily.json, wages_weekly.json,
wages_daily.json, gp_monthly.json, wastage.json and staff_wins.json.
Writes one self-contained (unencrypted) HTML file to OUT_FILE.
Encrypt it with StatiCrypt before publishing - never commit the plain file.
"""
import json, os, sys, datetime

HERE = os.path.dirname(os.path.abspath(__file__))
IDS = ["sales_weekly", "sales_daily", "wages_weekly", "wages_daily", "gp_monthly", "wastage", "staff_wins"]


def main():
    data_dir, page_file, out_file = sys.argv[1], sys.argv[2], sys.argv[3]
    updated = sys.argv[4] if len(sys.argv) > 4 else datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds")
    data = {}
    for i in IDS:
        p = os.path.join(data_dir, i + ".json")
        data[i] = json.load(open(p)) if os.path.exists(p) else []
    js = lambda o: json.dumps(o, separators=(",", ":")).replace("</", "<\\/")
    shell = open(os.path.join(HERE, "shell.html")).read()
    page = open(page_file).read()
    d3 = open(os.path.join(HERE, "d3.min.js")).read()
    assert "</script" not in d3.lower()
    out = (shell.replace("/*D3*/", d3, 1)
                .replace("/*DATA*/", js(data), 1)
                .replace("/*META*/", js({"updated": updated}), 1)
                .replace("/*PAGE*/", page, 1))
    os.makedirs(os.path.dirname(os.path.abspath(out_file)), exist_ok=True)
    open(out_file, "w").write(out)
    print("wrote", out_file, len(out), "bytes;", {k: len(v) for k, v in data.items()})


if __name__ == "__main__":
    main()
