import click
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from main import Base, Booking, Customer, Employee, Expense, Item, Order, Payment, Room, RoomType

# Set the database URI
DATABASE_URI = "sqlite:///mydb.db"

engine = create_engine(DATABASE_URI, echo=True)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()


@click.group()
def cli():
    pass


@cli.command()
def initdb():

    Base.metadata.create_all(engine)
    click.echo("Database initialized.")


@cli.command()
@click.option("--customername", prompt="Customer Name", help="Customer's name")
@click.option("--address", prompt="Address", help="Customer's address")
@click.option("--phoneno", prompt="Phone Number", help="Customer's phone number")
@click.option("--gender", prompt="Gender", help="Customer's gender")
@click.option("--status", default="active", help="Customer's status (default: active)")
def add_customer(customername, address, phoneno, gender, status):
    customer = Customer(
        Customername=customername,
        address=address,
        phoneno=phoneno,
        gender=gender,
        status=status
    )
    session.add(customer)
    session.commit()
    click.echo("Customer added successfully.")


@cli.command()
@click.option("--employeename", prompt="Employee Name", help="Employee's name")
@click.option("--loginid", prompt="Login ID", help="Employee's login ID")
@click.option("--emptype", prompt="Employee Type", help="Employee's type")
@click.option("--status", default="active", help="Employee's status (default: active)")
def add_employee(employeename, loginid, emptype, status):
    employee = Employee(
        employeename=employeename,
        loginid=loginid,
        emptype=emptype,
        status=status
    )
    session.add(employee)
    session.commit()
    click.echo("Employee added successfully.")

@cli.command()
@click.option("--employeeid", prompt="Employee ID", type=int, help="Employee ID")
@click.option("--expensetype", prompt="Expense Type", help="Expense Type")
@click.option("--expensemat", prompt="Expense Amount", help="Expense Amount")
@click.option("--expensedate", prompt="Expense Date", help="Expense Date")
@click.option("--status", default="pending", help="Expense Status (default: pending)")
def add_expense(employeeid, expensetype, expensemat,expensedate, status):
    expense = Expense(
        employeeid=employeeid,
        expensetype=expensetype,
        expensemat=expensemat,
        expensedate=expensedate,
        status=status
    )
    session.add(expense)
    session.commit()
    click.echo("Expense added successfully.")


if __name__ == "__main__":
    cli()
