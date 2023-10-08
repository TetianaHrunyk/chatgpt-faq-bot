import sys
import os


def setup_env():
    # these three lines swap the stdlib sqlite3 lib with the pysqlite3 package
    __import__("pysqlite3")
    sys.modules["sqlite3"] = sys.modules.pop("pysqlite3")

    with open(".env") as f:
        for line in f.readlines():
            key, value = line.strip("\n").split("=")
            os.environ[key] = value


setup_env()
