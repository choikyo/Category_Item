from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from categoryitem import Base, Category, Item
import datetime

engine = create_engine('sqlite:///puppycategory.db')

Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)

session = DBSession()


#Add Categorys
category1 = Category(name = "Soccer", description = "A game played with foot")
session.add(category1)

category2 = Category(name = "Basketball", description = "A game to shoot balls into a basket")
session.add(category2) 

#Add Items
item1 = Category(name = "Soccer Ball", description = "A soccer ball")
session.add(item1)

item2 = Category(name = "Soccer socks", description = "Long socks that protects the ankels and knees")
session.add(item2)

item3 = Category(name = "Air Jordan", description = "Shoes from Jordan's brand that makes you jump a little higher")
session.add(item3)




