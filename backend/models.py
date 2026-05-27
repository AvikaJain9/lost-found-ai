
from sqlalchemy import Column, Integer, String
from database import Base

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    type = Column(String)  # "lost" or "found"
    title = Column(String)
    description = Column(String)
    location = Column(String)
