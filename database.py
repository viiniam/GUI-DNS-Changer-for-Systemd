
import sqlite3

class DNSDatabase:
    def __init__(self, db_name="dns_servers.db"):
        self.conn = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        with self.conn:
            self.conn.execute("""
                CREATE TABLE IF NOT EXISTS servers (
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    primary_dns TEXT NOT NULL,
                    secondary_dns TEXT
                )
            """)

    def add_dns(self, name, primary_dns, secondary_dns=None):
        with self.conn:
            self.conn.execute(
                "INSERT INTO servers (name, primary_dns, secondary_dns) VALUES (?, ?, ?)",
                (name, primary_dns, secondary_dns)
            )

    def get_dns_servers(self):
        with self.conn:
            return self.conn.execute("SELECT name, primary_dns, secondary_dns FROM servers").fetchall()

    def remove_dns(self, name):
        with self.conn:
            self.conn.execute("DELETE FROM servers WHERE name = ?", (name,))
