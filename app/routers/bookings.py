from fastapi import APIRouter

router = APIRouter(prefix="/bookings", tags=["bookings"])

@router.get("/")
def get_bookings():
    return {"message": "Bookings endpoint not implemented yet"}
