import json

def save_json(data, name="ezio_output.json"):
    with open(name, "w") as f:
        json.dump(data, f, indent=2)

def save_md(data, name="ezio_report.md"):
    with open(name, "w") as f:
        for k, v in data.items():
            f.write(f"## {k}\n{v}\n\n")
