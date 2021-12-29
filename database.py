from dotenv import load_dotenv
load_dotenv()

# Regardless of the lint error you receive,
# load_dotenv must run before running this
# so that the environment variables are
# properly loaded.
from app import app, db
from app.models import Employee, Menu, MenuItem, MenuItemType, Table


with app.app_context():
    db.drop_all()
    db.create_all()

    employee = Employee(name="Margot", employee_number=1234, password="password")
    db.session.add(employee)
    db.session.commit()

    beverages = MenuItemType(name="Beverages")
    db.session.add(beverages)
    db.session.commit()
    entrees = MenuItemType(name="Entrees")
    db.session.add(entrees)
    db.session.commit()
    sides = MenuItemType(name="Sides")
    db.session.add(sides)
    db.session.commit()

    dinner = Menu(name="Dinner")
    db.session.add(dinner)
    db.session.commit()

    fries = MenuItem(name="French fries", price=3.50, type=sides, menu=dinner)
    db.session.add(fries)
    db.session.commit()
    drp = MenuItem(name="Dr. Pepper", price=1.0, type=beverages, menu=dinner)
    db.session.add(drp)
    db.session.commit()
    jambalaya = MenuItem(name="Jambalaya", price=21.98, type=entrees, menu=dinner)
    db.session.add(jambalaya)
    db.session.commit()

    db.session.add_all([
        Table(number=1, capacity=5),
        Table(number=2, capacity=10),
        Table(number=3, capacity=15),
        Table(number=4, capacity=20),
        Table(number=5, capacity=25),
        Table(number=6, capacity=30),
        Table(number=7, capacity=35),
        Table(number=8, capacity=40),
        Table(number=9, capacity=45),
        Table(number=10, capacity=50),
    ])

    db.session.commit()