import contextlib
import psycopg

class DatabaseConnection:
    def __init__(self, config: dict):
        self.config = config

    @contextlib.contextmanager
    def connect(self) -> psycopg.Cursor:
        try:
            with psycopg.connect(**self.config) as conn:
                yield conn.cursor()
        except psycopg.Error as e:
            print(f"Database connection error: {e}")
            raise