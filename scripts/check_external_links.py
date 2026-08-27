#!/usr/bin/env python3
"""Check curated external links without treating publisher rate limits as breakage."""

from __future__ import annotations

import argparse
import csv
import socket
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


ROOT = Path(__file__).resolve().parents[1]
DEFINITIVE_FAILURES = {404, 410}
TRANSIENT_STATUSES = {403, 408, 425, 429, 500, 502, 503, 504}


@dataclass(frozen=True)
class Result:
    url: str
    state: str
    detail: str


def catalog_urls(include_all: bool) -> list[str]:
    with (ROOT / "data" / "references.csv").open(encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))
    fields = ("paper_url", "project_url", "code_url", "verification_evidence_url") if include_all else ("code_url",)
    return sorted({row[field].strip() for row in rows for field in fields if row[field].strip()})


def request(url: str, method: str, timeout: float) -> int:
    headers = {"User-Agent": "Awesome-Intelligent-Intersections-link-audit/1.0"}
    if method == "GET":
        headers["Range"] = "bytes=0-0"
    response = urlopen(Request(url, method=method, headers=headers), timeout=timeout)
    try:
        return response.status
    finally:
        response.close()


def check(url: str, timeout: float) -> Result:
    try:
        status = request(url, "HEAD", timeout)
        return Result(url, "ok", str(status))
    except HTTPError as error:
        if error.code in {400, 405, 501}:
            try:
                status = request(url, "GET", timeout)
                return Result(url, "ok", str(status))
            except HTTPError as get_error:
                error = get_error
            except (URLError, TimeoutError, socket.timeout) as get_error:
                return Result(url, "warning", str(get_error))
        if error.code in DEFINITIVE_FAILURES:
            return Result(url, "broken", f"HTTP {error.code}")
        state = "warning" if error.code in TRANSIENT_STATUSES else "broken"
        return Result(url, state, f"HTTP {error.code}")
    except (URLError, TimeoutError, socket.timeout) as error:
        return Result(url, "warning", str(error))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--all", action="store_true", help="also check publication, project, and evidence URLs")
    parser.add_argument("--workers", type=int, default=8)
    parser.add_argument("--timeout", type=float, default=15.0)
    parser.add_argument("--strict-transient", action="store_true", help="fail on rate limits and network errors")
    args = parser.parse_args()

    urls = catalog_urls(args.all)
    results: list[Result] = []
    with ThreadPoolExecutor(max_workers=max(1, args.workers)) as executor:
        futures = {executor.submit(check, url, args.timeout): url for url in urls}
        for future in as_completed(futures):
            results.append(future.result())

    results.sort(key=lambda result: (result.state, result.url))
    for result in results:
        if result.state != "ok":
            print(f"{result.state.upper():7} {result.detail:12} {result.url}")

    counts = {state: sum(result.state == state for result in results) for state in ("ok", "warning", "broken")}
    print(f"Checked {len(results)} unique URLs: {counts['ok']} ok, {counts['warning']} warnings, {counts['broken']} broken")
    if counts["broken"] or (args.strict_transient and counts["warning"]):
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
