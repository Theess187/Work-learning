import csv
import json

INPUT_FILE = "cameras.csv"
OUTPUT_FILE = "zabbix_import.json"

ZABBIX_VERSION = "7.2"

GROUPS = {
    "Cameras": {
        "uuid": "5bfa16d5bfe74153af77665de5bcade7",
        "template": "Generic by SNMP"
    },
    "Switches": {
        "uuid": "70d63c3421e64bc8af24f8d26ff903d3",
        "template": "PSW-2G4F"
    }
}


def build_host(ip, device_type, hostname):
    if device_type == "Switch":
        group = "Switches"
        details = {
            "version": "SNMPV1",
            "community": "{$SNMP_COMMUNITY}"
        }
    else:
        group = "Cameras"
        details = {
            "community": "{$SNMP_COMMUNITY}"
        }

    return {
        "host": hostname,
        "name": hostname,
        "templates": [
            {"name": GROUPS[group]["template"]}
        ],
        "groups": [
            {"name": group}
        ],
        "interfaces": [
            {
                "type": "SNMP",
                "ip": ip,
                "port": "161",
                "details": details,
                "interface_ref": "if1"
            }
        ]
    }


hosts = []

with open(INPUT_FILE, newline="", encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile)

    for row in reader:
        if not row:
            continue

        if len(row) < 3:
            continue

        ip, device_type, hostname = row[:3]
        hosts.append(build_host(ip, device_type, hostname))


zabbix_export = {
    "zabbix_export": {
        "version": ZABBIX_VERSION,
        "host_groups": [
            {"uuid": GROUPS["Cameras"]["uuid"], "name": "Cameras"},
            {"uuid": GROUPS["Switches"]["uuid"], "name": "Switches"}
        ],
        "hosts": hosts
    }
}

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    json.dump(zabbix_export, f, indent=4, ensure_ascii=False)

print(f"Создан файл: {OUTPUT_FILE}")
print(f"Добавлено хостов: {len(hosts)}")
