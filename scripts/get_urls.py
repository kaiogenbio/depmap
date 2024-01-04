#!/usr/bin/env python

import json
import argparse

from pathlib import Path
from collections import defaultdict


def parse_datasets_json(fname: Path):
    with open(fname) as f:
        datasets = json.load(f)
        downloads = datasets["table"]
        downloads_dict = defaultdict(dict)

        for download in downloads:
            fname = download["fileName"]
            url = download["downloadUrl"]
            release = download["releaseName"]

            downloads_dict[release][fname] = url

    return downloads_dict


def main(*, datasets, release, outfile):
    url_dict = parse_datasets_json(datasets)

    release_urls = url_dict[release]

    with open(outfile, "w") as fout:
        for fname, url in release_urls.items():
            if url is None:
                continue

            if not url.startswith("https://"):
                url = f"https://depmap.org{url_dict[fname]}"
            fout.write(f"{fname} {url}\n")

    print("[i] Done.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("--datasets", required=True, type=Path)
    parser.add_argument("--release", required=True, type=str)
    parser.add_argument("--outfile", required=True, type=Path)

    args = parser.parse_args()

    main(datasets=args.datasets, release=args.release, outfile=args.outfile)
