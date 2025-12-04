from fastapi import APIRouter, HTTPException
from sqlalchemy import text
from ..database import engine

router = APIRouter(prefix="/debug", tags=["debug"])

@router.get("/table/{table_name}")
def read_table(table_name: str):
    try:
        with engine.connect() as conn:
            result = conn.execute(text(f"SELECT * FROM {table_name}"))
            rows = [dict(row) for row in result]
        return {"table": table_name, "rows": rows}

    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error loading table: {str(e)}")
