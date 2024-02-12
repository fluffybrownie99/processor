from sqlalchemy import Column, Integer, String, DateTime
from base import Base
import datetime

class ServerStats(Base):
    __tablename__ = "ServerStats"
    id = Column(Integer, primary_key=True)
    total_uploads = Column(Integer, nullable=False)
    total_playbacks = Column(Integer, nullable=False)
    most_accessed_file_id = Column(Integer, nullable=False)
    largest_file_id = Column(Integer, nullable=False)
    last_updated = Column(DateTime, nullable=False)

    def __init__(self, total_uploads, total_playbacks, most_accessed_file_id, largest_file_id, last_updated):
        self.total_uploads = total_uploads
        self.total_playbacks = total_playbacks 
        self.most_accessed_file_id = most_accessed_file_id
        self.largest_file_id = largest_file_id
        self.last_updated = last_updated

    def to_dict(self):    
        return {
            'id': self.id,
            'total_uploads':self.total_uploads,
            'total_playbacks':self.total_playbacks,
            'most_accessed_file_id': self.most_accessed_file_id,
            'largest_file_id': self.largest_file_id,
            'last_updated': self.last_updated.strftime("%Y-%m-%dT%H:%M:%S")
        }