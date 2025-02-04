from app.schemas.item import ItemCreate, ItemResponse

# In-memory "database"
items_db = []
current_id = 0

def create_item(item: ItemCreate) -> ItemResponse:
    global current_id
    current_id += 1
    new_item = ItemResponse(id=current_id, **item.dict())
    items_db.append(new_item)
    return new_item

def get_item(item_id: int) -> ItemResponse | None:
    for item in items_db:
        if item.id == item_id:
            return item
    return None