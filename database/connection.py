from sqlalchemy import create_engine

DATABASE_URL = (
    "postgresql://postgres:Esther123@localhost:5433/banking_dw"
)

engine = create_engine(DATABASE_URL)