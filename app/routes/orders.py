from flask import Blueprint, render_template, redirect
import psycopg2
from flask_login import login_required

bp = Blueprint("orders", __name__, url_prefix="")

CONNECTION_PARAMETERS = {
    "dbname": "order_up_dev",
    "user": "order_up",
    "password": "9uCxydbt"
}

@bp.route("/")
@login_required
def index():
    return render_template("orders.html")


@bp.route("/assign_table")
@login_required
def assign_table(table_id, employee_id):
    with psycopg2.connect(**CONNECTION_PARAMETERS) as conn:
        with conn.cursor() as curs:
            curs.execute(
                """
                INSERT INTO orders (table_id, employee_id)
                VALUES (%(table_id)s, %(employee_id)s)
                """,
                {
                    "table_id": table_id,
                    "employee_id": employee_id
                }
            )
        return redirect('/')

@bp.route("/close_table")
@login_required
def close_table(order_id):
    with psycopg2.connect(**CONNECTION_PARAMETERS) as conn:
        with conn.cursor() as curs:
            curs.execute(
                """
                SELECT id FROM orders
                WHERE (%(order_id)s == id)
                """,
                {
                    'order_id': order_id
                }
            )

@bp.route("/add_to_order")
@login_required
def add_to_order():
    pass
