#!/usr/bin/env python

"""
Usage:

    ./json-to-csv.py -i in.json -o out.csv

    ./json-to-csv.py < in.json > out.csv
"""

import json
import csv
from argparse import ArgumentParser, FileType
import sys


def parse_args():
    args = ArgumentParser(__file__)
    args.add_argument(
        "-i",
        "--input-file",
        type=FileType("r"),
        help="input file path. default is stdin",
        default=sys.stdin,
    )
    args.add_argument(
        "-o",
        "--output-file",
        type=FileType("w"),
        help="output file path. default is stdout",
        default=sys.stdout,
    )
    return args.parse_args()


def main(args):
    data = json.load(args.input_file)
    csvwriter = csv.writer(args.output_file)
    csvwriter.writerow(
        [
            "hypervisorId",
            "name",
            "guestId",
            "guestIds__state",
            "guestIds__active",
            "guestIds__virtWhoType",
            "facts__hypervisor.type",
            "facts__dmi.system.uuid",
            "facts__cpu.cpu_socket(s)",
            "facts__hypervisor.cluster",
            "facts__hypervisor.version",
        ]
    )

    last_id = None
    for h in data.get("hypervisors", []):
        id_ = h["hypervisorId"]["hypervisorId"]
        name = h["name"]
        type_ = h["facts"]["hypervisor.type"]
        uuid_ = h["facts"]["dmi.system.uuid"]
        sockets = int(h["facts"]["cpu.cpu_socket(s)"])
        cluster = h["facts"]["hypervisor.cluster"]
        version = h["facts"]["hypervisor.version"]

        for g in h["guestIds"]:
            guestId = g["guestId"]
            state = g["state"]
            active = g["attributes"]["active"]
            virtWhoType = g["attributes"]["virtWhoType"]
            csvwriter.writerow(
                [
                    id_ if id_ != last_id else "",
                    name if id_ != last_id else "",
                    guestId,
                    state,
                    active,
                    virtWhoType,
                    type_ if id_ != last_id else "",
                    uuid_ if id_ != last_id else "",
                    sockets if id_ != last_id else "",
                    cluster if id_ != last_id else "",
                    version if id_ != last_id else "",
                ]
            )
            last_id = id_
    return 0


if __name__ == "__main__":
    args = parse_args()
    rc = main(args)
    sys.exit(rc)
