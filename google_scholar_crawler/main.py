"""Fetch Google Scholar statistics and write JSON files for the homepage."""

from __future__ import annotations

import json
import os
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from scholarly import scholarly

RESULTS_DIR = Path("results")


def get_google_scholar_id() -> str:
    """Read the Google Scholar ID from the GitHub Actions environment."""
    scholar_id = os.getenv("GOOGLE_SCHOLAR_ID", "").strip()
    if not scholar_id:
        raise RuntimeError("GOOGLE_SCHOLAR_ID is not set.")
    return scholar_id


def fetch_author_data(scholar_id: str) -> dict[str, Any]:
    """Fetch and normalize author data from Google Scholar."""
    author = scholarly.search_author_id(scholar_id)
    scholarly.fill(author, sections=["basics", "indices", "counts", "publications"])

    author["updated"] = datetime.now(timezone.utc).isoformat()
    author["publications"] = {
        publication["author_pub_id"]: publication
        for publication in author.get("publications", [])
        if publication.get("author_pub_id")
    }
    return author


def write_json(path: Path, data: dict[str, Any]) -> None:
    """Write compact UTF-8 JSON."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")


def main() -> None:
    scholar_id = get_google_scholar_id()
    author = fetch_author_data(scholar_id)

    write_json(RESULTS_DIR / "gs_data.json", author)
    write_json(
        RESULTS_DIR / "gs_data_shieldsio.json",
        {
            "schemaVersion": 1,
            "label": "citations",
            "message": str(author.get("citedby", 0)),
        },
    )

    print(json.dumps(author, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
