from typing import List
import datetime

from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, REAL
from sqlalchemy.orm.session import object_session, Session

Base = declarative_base()
date = datetime.date


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


class Customer(Base):
    __tablename__ = 'customer'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(50),  nullable=False)
    last_name = Column(String(50),  nullable=False)
    email = Column(String(125))
    address = Column(String(150))
    city = Column(String(50))
    state = Column(String(50))
    postal_code = Column(String(10))
    country = Column(String(50))


class Orders(Base):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey('customer.id'), nullable=False)
    order_date = Column(String(50), nullable=False)
    discount = Column(REAL(2), nullable=False)
    total_price = Column(REAL(2), nullable=False)
    ship_date = Column(String(50))


class Flute(Base):
    __tablename__ = 'flute'
    id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey('orders.id'), nullable=False)
    customer_id = Column(Integer, nullable=False)
    flute_type = Column(String(50), nullable=False)
    hand = Column(String(10), nullable=False)
    key = Column(String(5), nullable=False)
    octave = Column(Integer, nullable=False)
    scale_name = Column(String(50), nullable=False)
    tuning_ref = Column(Integer, nullable=False)
    flute_wood = Column(String(50))
    block_wood = Column(String(50))


class FHP(Base):
    __tablename__ = 'fhp'
    id = Column(Integer, primary_key=True)
    key = Column(String(5), nullable=False)
    octave = Column(Integer, nullable=False)
    scale = Column(String(25), nullable=False)
    # bore_length = Column(Integer, nullable=False)
    fh_1 = Column(REAL(2), nullable=False)
    fh_2 = Column(REAL(2), nullable=False)
    fh_3 = Column(REAL(2), nullable=False)
    fh_4 = Column(REAL(2), nullable=False)
    fh_5 = Column(REAL(2), nullable=False)
    fh_6 = Column(REAL(2), nullable=False)
    fh_7 = Column(REAL(2), nullable=False)

