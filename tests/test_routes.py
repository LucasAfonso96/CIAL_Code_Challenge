from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from ..src.main import app
from ..src.routes import get_db


SQLALCHEMY_DATABASE_URL = "sqlite:///./stocks.db"


engine = create_engine(SQLALCHEMY_DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db
client = TestClient(app)

class TestStockAPI:
    @classmethod
    def setup_class(cls):
        cls.db = TestingSessionLocal()

    @classmethod
    def teardown_class(cls):
        cls.db.close()
        engine.dispose()

    def test_get_stock(self):
        response = client.get("/stock/AAPL")
        assert response.status_code == 200
        assert response.json()  # Ensure the response can be parsed as JSON

    def test_update_stock(self):
        response = client.post("/stock/teste", json={"amount": 10})
        assert response.status_code == 200
        assert response.json()["message"] == "10 units of stock teste were added to your stock record"

    # Additional test cases can be added for edge cases, error handling, etc.
