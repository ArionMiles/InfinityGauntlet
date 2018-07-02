from sqlalchemy import Column, Integer, String, Boolean
from database import Base


class Users(Base):
    __tablename__ = 'mortals'
    id = Column(Integer, primary_key=True)
    username = Column(String(100), unique=True)
    saved = Column(Boolean)  

    def __init__(self, username, saved=False):
        self.username = username
        self.saved = saved

    def __repr__(self):
        return '<Username: {} | Saved: {}>'.format(self.username, self.saved)