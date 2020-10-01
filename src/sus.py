#!/usr/bin/env python3


"""
This is the main sus package file.

It contains all functionality sus actually offers.
See specific function docstrings and README for more details.
"""


from pathlib import Path
from shutil import copy, rmtree
from string import Template
from typing import List, Tuple


SPLIT_CHAR = "|"
SUFFIX = ".html"

CURRENT_DIR = Path.cwd()
INPUT_FILE = CURRENT_DIR / "input"
OUTPUT_DIR = CURRENT_DIR / "output"

HOME_INDEX_FILE = (CURRENT_DIR / "home").with_suffix(SUFFIX)

HTML = Template("<meta http-equiv='refresh' content='0;url=$url' />")


def _ensure_dir(dir_: Path) -> None:
    try:
        rmtree(dir_)
    except FileNotFoundError:
        pass
    finally:
        dir_.mkdir()


def _read_input() -> List[str]:
    with open(INPUT_FILE) as urls_file:
        lines = urls_file.read().splitlines()
        return lines


def _sanitize_url(url: str) -> str:
    santized_url = url.replace("'", "%27")
    return santized_url


def _generate_page_params(line: str) -> Tuple[str, str]:
    slug, url = line.split(SPLIT_CHAR, 1)
    html = HTML.substitute(url=_sanitize_url(url))
    return slug, html


def _write_page(file_path: Path, html: str) -> None:
    with open(file_path, "w") as file_:
        file_.write(html)


def _generate_page(slug: str, html: str) -> None:
    url_dir = OUTPUT_DIR / slug
    _ensure_dir(url_dir)

    index_path = (url_dir / "index").with_suffix(SUFFIX)
    _write_page(index_path, html)


def _copy_home() -> None:
    output_home = (OUTPUT_DIR / "index").with_suffix(SUFFIX)
    try:
        copy(HOME_INDEX_FILE, output_home)
    except FileNotFoundError:
        pass


def sus() -> None:
    """
    Run all of sus.

    It runs the entire script to generate the output directory based on the input file.
    """
    _ensure_dir(OUTPUT_DIR)

    lines = _read_input()
    for line in lines:
        slug, html = _generate_page_params(line)
        _generate_page(slug, html)

    _copy_home()


if __name__ == "__main__":
    sus()
