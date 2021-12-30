from flask import Blueprint, render_template, redirect
import psycopg2
from flask_login import login_required
from app.models import Table, Order, Employee, db
from app.forms import TableAssignmentForm

bp = Blueprint("orders", __name__, url_prefix="")

CONNECTION_PARAMETERS = {
    "dbname": "order_up_dev",
    "user": "order_up",
    "password": "9uCxydbt"
}

@bp.route("/")
@login_required
def index():

    form = TableAssignmentForm()

    # Get the tables and open orders
    tables = Table.query.order_by(Table.number).all()
    open_orders = Order.query.filter(Order.finished == False)

    # Get the table ids for the open orders
    busy_table_ids = [order.table_id for order in open_orders]

    # Filter the list of tables for only the open tables
    open_tables = [table for table in tables if table.id not in busy_table_ids]

    # Finally, convert those tables to tuples for the select field and set the
    # choices property to it
    form.tables.choices = [(t.id, f"Table {t.number}") for t in open_tables]

    servers = Employee.query.order_by(Employee.id).all()
    form.servers.choices = [(s.id, f"{s.name}" ) for s in servers]


    return render_template("orders.html", form=form)


@bp.route("/assign_table", methods=["POST"])
@login_required
def assign_table():

    form = TableAssignmentForm()
    print("------------------------------------------", form.data)

    return render_template("orders.html", form=form)

# @bp.route("/close_table", methods=["POST"])
# @login_required
# def close_table():

#     this_order = Order.query.get(order_id)
#     this_order.finished = True
#     db.session.commit()
#     return redirect('/')


# @bp.route("/add_to_order", methods=["POST"])
# @login_required
# def add_to_order(order_id, menu_items):
