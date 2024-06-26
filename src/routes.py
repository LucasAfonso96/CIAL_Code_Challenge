from fastapi import Depends, HTTPException, APIRouter, Request
from sqlalchemy.orm import Session
from .services import fetch_polygon_data, scrape_marketwatch_data
from . import models, database
from datetime import datetime
from cachetools import TTLCache

router = APIRouter()

cache = TTLCache(maxsize=100, ttl=300)

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/stock/{stock_symbol}", response_model=models.Stock)
async def get_stock(stock_symbol:str, db: Session = Depends(get_db)):

    if stock_symbol in cache:
        cached_stock, cached_time = cache[stock_symbol]
        if (datetime.now() - cached_time).total_seconds() <= 300:
            return cached_stock
    

    try:
        stock_data_from_api = fetch_polygon_data(stock_symbol)
        marketwatch_data = await scrape_marketwatch_data(stock_symbol)
    except Exception as e:
        raise HTTPException(status_code=500, detail="Failed to fetch stock data")
    try:
        stock_data = {
            "afterHours": stock_data_from_api.get("afterHours"),
            "close": stock_data_from_api.get("close"),
            "from_": stock_data_from_api.get("from"),
            "high": stock_data_from_api.get("high"),
            "low": stock_data_from_api.get("low"),
            "open": stock_data_from_api.get("open"),
            "preMarket": stock_data_from_api.get("preMarket"),
            "status": stock_data_from_api.get("status"),
            "symbol": stock_data_from_api.get("symbol"),
            "volume": stock_data_from_api.get("volume"),
            "performance": marketwatch_data,
            "amount": 0  
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail="Failed to process stock data")

    stock = models.Stock(**stock_data)

    db_stock = database.StockDB.from_pydantic(stock)
    db.add(db_stock)
    db.commit()
    
    cache[stock_symbol] = (stock, datetime.now())
    return stock

@router.post("/stock/{stock_symbol}")
async def update_stock(request: Request, stock_symbol: str, db: Session = Depends(get_db)):
    try:
        request_body = await request.json()
        amount = request_body.get("amount")
        
        if amount is None:
            raise HTTPException(status_code=400, detail="Amount must be provided in the request body")

        db_stock = db.query(database.StockDB).filter(database.StockDB.symbol == stock_symbol).first()
        if db_stock:
            db_stock.amount += amount
        else:
            db_stock = database.StockDB(symbol=stock_symbol, amount=amount)
            db.add(db_stock)
        db.commit()
        return {"message": f"{amount} units of stock {stock_symbol} were added to your stock record"}
    except Exception as e:
        raise HTTPException(status_code=500, detail="Failed to update stock data")