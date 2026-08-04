from database.connection import engine

try:
    with engine.connect() as conn:
        print("=" * 50)
        print("Connection OK")
        print("=" * 50)
except Exception as e:
    print(type(e))
    print(repr(e))