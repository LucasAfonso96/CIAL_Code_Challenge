from sqlalchemy import create_engine, Column, Integer, String, Float, JSON
from sqlalchemy.orm import sessionmaker, declarative_base
from .models import Stock
import os

SQLALCHEMY_DATABASE_URL = os.environ.get("DATABASE_URL")

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    
Base = declarative_base()

class StockDB(Base):
    __tablename__ = "stocks"
    
    id = Column(Integer, primary_key=True, index=True)
    symbol = Column(String, index=True)
    amount = Column(Integer)
    afterHours = Column(Float, nullable=True)
    close = Column(Float, nullable=True)
    from_ = Column(String, nullable=True)
    high = Column(Float, nullable=True)
    low = Column(Float, nullable=True)
    open = Column(Float, nullable=True)
    preMarket = Column(Float, nullable=True)
    status = Column(String, nullable=True)
    volume = Column(Integer, nullable=True)
    performance = Column(JSON, nullable=True)

    @classmethod
    def from_pydantic(cls, stock: "Stock"):
        return cls(**stock.model_dump())


Base.metadata.create_all(bind=engine)