from pathlib import Path
from sqlalchemy import text

from database.connection import engine


def create_tables():

    sql_file = Path("sql/schema.sql")

    with open(sql_file, "r", encoding="utf-8") as file:
        sql_script = file.read()

    with engine.begin() as connection:

        for statement in sql_script.split(";"):

            statement = statement.strip()

            if statement:
                connection.execute(text(statement))

    print("=" * 50)
    print("Tables créées avec succès")
    print("=" * 50)


if __name__ == "__main__":
    create_tables()