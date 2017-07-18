from sqlalchemy import Column, ForeignKey, Integer, String, Date, Numeric
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy import func

Base = declarative_base()

class Category(Base):
    __tablename__ = 'category'
    id = Column(Integer, primary_key = True)
    name = Column(String(80), nullable = False)
    description = Column(String(500), nullable = False)
    insert_date = Column(Integer, server_default = func.strftime('%s','now'))

class Item(Base):
    __tablename__ = 'item'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    description = Column(String(500), nullable = False)
    category_id = Column(Integer, ForeignKey('category.id'))
    category = relationship(Category)
    insert_date = Column(Integer, server_default = func.strftime('%s','now'))


engine = create_engine('sqlite:///itemcategory.db')


Base.metadata.create_all(engine)