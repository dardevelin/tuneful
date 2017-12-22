from sqlalchemy import Column, Integer, String, Sequence, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Song(Base):
    __tablename__ = "song"

    id = Column(Integer, primary_key=True)
    
    file = relationship("File", uselist = False, backref = "file")

    def as_dictionary(self):
    	song = {"id": self.id,
    			"file": {"id": file.id, "name": file.name}
    	}


class File(Base):
    __tablename__ = "files"

    id = Column(Integer, primary_key=True)
    name = Column(String(1024))
    
    song = Column(Integer, ForeignKey('song.id'), nullable = False)

    def as_dictionary(self):
    	file = {"id": self.id,
    			"name": self.name
    	}