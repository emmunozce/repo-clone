from fastapi import APIRouter, HTTPException
from app.schemas.item import ItemCreate, ItemResponse
from app.services.item_service import create_item, get_item

router = APIRouter(prefix="/items", tags=["items"])

@router.post("/", response_model=ItemResponse)
def create_new_item(item: ItemCreate):
    return create_item(item)

@router.get("/{item_id}", response_model=ItemResponse)
def read_item(item_id: int):
    item = get_item(item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item