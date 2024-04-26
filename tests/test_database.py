import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from ..src.models import Stock
from ..src.database import Base, StockDB

class TestStockDB:
    @pytest.fixture
    def db_session(self):
        engine = create_engine("sqlite:///:memory:")
        SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
        Base.metadata.create_all(bind=engine)
        yield SessionLocal()
        Base.metadata.drop_all(bind=engine)

    def test_stockdb_from_pydantic(self, db_session):
        stock_pydantic = Stock(
            symbol="AAPL",
            amount=100,
            afterHours=110.5,
            close=105.2,
            from_="2024-04-24",
            high=107.8,
            low=103.5,
            open=104.5,
            preMarket=104.8,
            status="active",
            volume=10000,
            performance={"1 Day": 1.23, "5 Day": 4.56}
        )

        stock_db = StockDB.from_pydantic(stock_pydantic)

        assert stock_db.symbol == "AAPL"
        assert stock_db.amount == 100
        assert stock_db.afterHours == 110.5
        assert stock_db.close == 105.2
        assert stock_db.from_ == "2024-04-24"
        assert stock_db.high == 107.8
        assert stock_db.low == 103.5
        assert stock_db.open == 104.5
        assert stock_db.preMarket == 104.8
        assert stock_db.status == "active"
        assert stock_db.volume == 10000
        assert stock_db.performance == {"1 Day": 1.23, "5 Day": 4.56}
