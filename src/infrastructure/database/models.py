from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from .session import Base

class Commit(Base):
    __tablename__ = "commits"

    id = Column(Integer, primary_key=True, index=True)
    repo = Column(String, nullable=False)
    sha = Column(String, nullable=False)
    branch = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)