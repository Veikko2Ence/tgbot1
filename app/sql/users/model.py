from sqlalchemy import Column, Integer, String
from sql.base import Base



class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, unique=True, nullable=False)
    username = Column(String, nullable=True)
    age = Column(Integer, nullable=True)
    about = Column(String, nullable=True)

