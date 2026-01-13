# tests/integration/db_test_helper.py

import sqlite3
import tempfile
from pathlib import Path

class IntegrationDatabase:
    """
    Creates an isolated SQLite database for integration tests
    using the same schema and seed data as the application.
    """

    def __init__(self):
        self._file = tempfile.NamedTemporaryFile(delete=False)
        self.path = Path(self._file.name)
        self._initialize_db()

    def _initialize_db(self) -> None:
        sql_path = Path(__file__).parents[2] / "shop" / "data" / "products.sql"
        sql = sql_path.read_text()

        conn = sqlite3.connect(self.path)
        conn.executescript(sql)
        conn.commit()
        conn.close()
