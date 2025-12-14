import re
import json
import yaml

INPUT_FILE = r"D:\all task\python project\pmbus\code improvement\header.h"
OUTPUT_JSON = r"D:\all task\python project\pmbus\code improvement\output.json"
OUTPUT_YAML = r"D:\all task\python project\pmbus\code improvement\output.yaml"

ENTRY_REGEX = re.compile(
    r'\{\s*"(?P<name>\w+)"\s*,\s*(?P<addr>0x[0-9A-Fa-f]+)\s*,\s*(?P<access>RW|RO|WO)\s*,\s*(?P<len>\d+)\s*\}'
)


def parse_registers(text):
    registers = []
    for match in ENTRY_REGEX.finditer(text):
        registers.append({
            "name": match.group("name"),
            "address": match.group("addr"),
            "access": match.group("access"),
            "length": int(match.group("len"))
        })
    return registers


def write_json(registers, path):
    with open(path, "w") as f:
        json.dump(registers, f, indent=2)


def write_yaml(registers, path):
    with open(path, "w") as f:
        yaml.dump(registers, f)


def main():
    with open(INPUT_FILE, "r") as f:
        text = f.read()

    registers = parse_registers(text)

    write_json(registers, OUTPUT_JSON)
    write_yaml(registers, OUTPUT_YAML)

    print("Generated:")
    print(" -", OUTPUT_JSON)
    print(" -", OUTPUT_YAML)


if __name__ == "__main__":
    main()
