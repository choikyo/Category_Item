from flask import Flask, render_template
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from categoryitem import Base, Category, Item
app = Flask(__name__)


engine = create_engine('sqlite:///itemcategory.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()
 
# add an item
@app.route('/catalog/<string:category_name>/new')
def NewItemForm(category_name):
    return render_template('new_item.html', category_name=category_name)

# add a new catagory
@app.route('/new_category')
def NewCategoryForm():
    return render_template('base.html')

# show list of items of a selected category
@app.route('/catalog/<string:category_name>/<string:item_name>')
def ShowItemDesc(category_name,item_name):
    item = session.query(Item).join(Category).filter(Category.name==category_name).filter(Item.name==item_name).first()
    return render_template('show_item_description.html', description =  item.description, item_name = item_name )

# show list of items of a selected category
@app.route('/catalog/<string:category_name>/items')
def CategoryItemList(category_name):
    category = session.query(Category).order_by(Category.name)
    item = session.query(Item).join(Category).filter(Category.name==category_name)
    count = item.from_self().count()
    if count >1:
        count_str = str(count) + " items"
    else:
        count_str = str(count) + " item"
    
    return render_template('category_item.html', category = category , item = item, category_name=category_name, count_str=count_str)

# main page    
@app.route('/')
def MainPage():
    category = session.query(Category).order_by(Category.name)
    item = session.query(Item).join(Category).limit(8)
    item = item.from_self().order_by(Item.insert_date.desc())
    return render_template('main.html', category=category, item=item)


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=8000)