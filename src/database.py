from sqlalchemy import create_engine, Column, Integer, String, Float, JSON
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .models import Stock

SQLALCHEMY_DATABASE_URL = "sqlite:///./stocks.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
#Base.metadata.drop_all(bind=engine)


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
        return cls(**stock.dict())


Base.metadata.create_all(bind=engine)