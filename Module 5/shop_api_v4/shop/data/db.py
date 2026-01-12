# shop/data/db.py

import sqlite3
from pathlib import Path
from typing import Iterator, Optional

# Database file path
DB_FILE = Path(__file__).resolve().parent/"shop.db"

def connect(db_path: Optional[str] = None) -> sqlite3.Connection:
    """Create a database connection with dictionary-style rows."""
    path = Path(db_path) if db_path else DB_FILE
    conn = sqlite3.connect(path, detect_types=sqlite3.PARSE_DECLTYPES)
    conn.row_factory = sqlite3.Row
    return conn

def rows_to_dicts(rows: Iterator[sqlite3.Row]) -> list[dict]:
    """Convert SQLite rows to plain Python dicts."""
    return [dict(row) for row in rows]
