from fastapi import FastAPI
from sqlalchemy.orm import Session
from database import SessionLocal, engine, Base
import models
from ai_match import find_matches

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.post("/add-item")
def add_item(type: str, title: str, description: str, location: str):
    db: Session = SessionLocal()

    item = models.Item(
        type=type,
        title=title,
        description=description,
        location=location
    )

    db.add(item)
    db.commit()
    db.refresh(item)

    return {"message": "Item added", "id": item.id}


@app.get("/match/{item_id}")
def match_item(item_id: int):
    db: Session = SessionLocal()

    new_item = db.query(models.Item).get(item_id)
    others = db.query(models.Item).filter(models.Item.type != new_item.type).all()

    matches = find_matches(new_item.description, others)

    return [{"title": m[0].title, "score": m[1]} for m in matches]
