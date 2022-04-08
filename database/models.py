from typing import List

from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm.session import object_session, Session

Base = declarative_base()


class Note(Base):
    __tablename__ = 'note'

    offset = Column(Integer, autoincrement=False, primary_key=True)
    name = Column(String(3), unique=True, nullable=False)

    @classmethod
    def from_offset(cls, session: Session, offset: int):
        return session.query(cls).filter_by(offset=offset % 12).first()

    @classmethod
    def from_name(cls, session: Session, name: str):
        note = session.query(cls).filter_by(name=name.upper()).first()
        if note is None:
            raise ValueError(f'No note found with the name "{name}"')
        else:
            return note



class Scale(Base):
    __tablename__ = 'scale'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    offsets = relationship('ScaleOffset', backref='scale')

    def get_notes(self, key: Note) -> List[Note]:
        sess = object_session(self)

        return [
            Note.from_offset(sess, offset.offset + key.offset)
            for offset in self.offsets
        ]


class ScaleOffset(Base):
    __tablename__ = 'scale_offset'

    id = Column(Integer, primary_key=True)
    scale_id = Column(Integer, ForeignKey('scale.id'), nullable=False)
    offset = Column(Integer, nullable=False)


