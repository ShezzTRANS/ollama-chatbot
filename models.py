from sqlalchemy import Column, Integer, String
from app.database import Base

class Chat(Base):
    __tablename__ = "chats"

    id = Column(Integer, primary_key=True, index=True)
    prompt = Column(String, index=True)
    response = Column(String)
