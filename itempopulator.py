from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from categoryitem import Base, Category, Item
import datetime

engine = create_engine('sqlite:///itemcategory.db')

Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)

session = DBSession()


#Add Categorys
category1 = Category(name = "Soccer", description = "A game played with foot")
session.add(category1)

category2 = Category(name = "Basketball", description = "A game to shoot balls into a basket")
session.add(category2) 

#Add Items
item1 = Item(name = "Soccer Ball", description = "A soccer ball" , category_id = 1)
session.add(item1)

item2 = Item(name = "Soccer socks", description = "Long socks that protects the ankels and knees" , category_id = 1)
session.add(item2)

item3 = Item(name = "Air Jordan", description = "Shoes from Jordan's brand that makes you jump a little higher" , category_id = 2)
session.add(item3)

session.commit()




