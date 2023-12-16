from sqlalchemy import Column, String, Integer, create_engine, VARCHAR, DateTime, ForeignKey, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
import argparse
from datetime import datetime

Base = declarative_base()


class Booking(Base):

    __tablename__ = 'bookings'
    Bookid = Column(Integer, primary_key=True)
    Roomid = Column(Integer, ForeignKey('rooms.Roomid'))
    Customerid = Column(Integer, ForeignKey('customers.Customerid'))
    Bookdate = Column(DateTime)
    Checkin = Column(DateTime)
    Checkout = Column(DateTime)
    status = Column(String)

    def __init__(self, Roomid, Customerid, Bookdate, Checkin, Checkout, status):
        self.Roomid = Roomid
        self.Customerid = Customerid
        self.Bookdate = Bookdate
        self.Checkin = Checkin
        self.Checkout = Checkout
        self.status = status

    def __repr__(self):
        pass


class Customer(Base):

    __tablename__ = 'customers'
    Customerid = Column(Integer, primary_key=True)
    Customername = Column(String)
    address = Column(VARCHAR(50))
    phoneno = Column(VARCHAR(15))
    gender = Column(String)
    status = Column(String)

    def __init__(self, Customername, address, phoneno, gender, status):
        self.Customername = Customername
        self.address = address
        self.phoneno = phoneno
        self.gender = gender
        self.status = status

    def __repr__(self):
        pass


class Employee(Base):

    __tablename__ = 'employees'
    employeeid = Column(Integer, primary_key=True, autoincrement=True)
    employeename = Column(String)
    loginid = Column(VARCHAR(50))
    emptype = Column(String)
    status = Column(String)

    def __init__(self, employeename, loginid, emptype, status):
        self.employeename = employeename
        self.loginid = loginid
        self.emptype = emptype
        self.status = status

    def __repr__(self):
        pass


class Expense(Base):

    __tablename__ = 'expenses'
    expenseid = Column(Integer, primary_key=True, autoincrement=True)
    employeeid = Column(Integer, ForeignKey('employees.employeeid'))
    expensetype = Column(String)
    expensemat = Column(Float)
    expensedate = Column(DateTime)
    status = Column(String)

    def __init__(self, employeeid, expensetype, expensemat, expensedate, status):
        self.employeeid = employeeid
        self.expensetype = expensetype
        self.expensemat = expensemat
        self.expensedate = expensedate
        self.status = status

    def __repr__(self):
        pass


class Item(Base):

    __tablename__ = 'items'
    itemid = Column(Integer, primary_key=True)
    itemtype = Column(VARCHAR(50))
    itemname = Column(VARCHAR(100))
    itemcost = Column(Float)
    status = Column(String)

    def __init__(self, itemid, itemtype, itemname, itemcost, status):
        self.itemid = itemid
        self.itemtype = itemtype
        self.itemname = itemname
        self.itemcost = itemcost
        self.status = status

    def __repr__(self):
        pass


class Order(Base):

    __tablename__ = 'orders'
    orderid = Column(Integer, primary_key=True)
    itemid = Column(Integer, ForeignKey('items.itemid'))
    bookid = Column(Integer, ForeignKey('bookings.Bookid'))
    orderdate = Column(DateTime)
    quantity = Column(Float)
    cost = Column(Float)
    status = Column(String)

    def __init__(self, orderid, itemid, bookid, orderdate, quantity, cost, status):
        self.orderid = orderid
        self.itemid = itemid
        self.bookid = bookid
        self.orderdate = orderdate
        self.quantity = quantity
        self.cost = cost
        self.status = status

    def __repr__(self):
        pass


class Payment(Base):

    __tablename__ = 'payments'
    paymentid = Column(Integer, primary_key=True)
    Bookid = Column(Integer, ForeignKey('bookings.Bookid'))
    paymenttype = Column(VARCHAR(50))
    amount = Column(Float)
    paymentdetail = Column(String)
    paymentdate = Column(DateTime)
    status = Column(String)

    def __init__(self, paymentid, Bookid, paymenttype, amount, paymentdetail, paymentdate, status):
        self.paymentid = paymentid
        self.Bookid = Bookid
        self.paymenttype = paymenttype
        self.amount = amount
        self.paymentdetail = paymentdetail
        self.paymentdate = paymentdate
        self.status = status

    def __repr__(self):
        pass


class Room(Base):

    __tablename__ = 'rooms'
    Roomid = Column(Integer, primary_key=True)
    Roomtype = Column(String, ForeignKey('roomtypes.Roomtype'))
    Roomnumber = Column(VARCHAR(10))
    status = Column(String)

    def __init__(self, Roomid, Roomtype, Roomnumber, status):
        self.Roomid = Roomid
        self.Roomtype = Roomtype
        self.Roomnumber = Roomnumber
        self.status = status

    def __repr__(self):
        pass


class RoomType(Base):

    __tablename__ = 'roomtypes'
    Roomtypeid = Column(Integer, primary_key=True)
    Roomtype = Column(String)
    Cost = Column(Float)
    status = Column(String)

    def __init__(self, Roomtypeid, Roomtype, Cost, status):
        self.Roomtypeid = Roomtypeid
        self.Roomtype = Roomtype
        self.Cost = Cost
        self.status = status

    def __repr__(self):
        pass


engine = create_engine("sqlite:///mydb.db", echo=True)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()
#customer = Customer('Jane', 'Nairobi', '0712324', 'female', 'unavailable')
#employee= Employee('John Maina', '12W13','Waiter','Active')
#item = Item(1, 'Food', 'Pizza', 3000, 'Active')
#room= Room(1, 'Single', '101', 'Active')
#room = Room(2, 'Double', '102', 'inActive')
#booking = Booking(1, 1, '2021-05-20', '2021-05-21', '2021-05-22', 'Active')
#expense = Expense(1, 'Food', 3000, '2021-05-20', 'Active')
payment = Payment(1, 1, 'Cash', 30000, 'Paid', '2021-05-20', 'active')
#payment = Payment(2, 2, 'Cash', 2000, 'Paid', '2021-05-20', 'pending')
#order = Order(1, 1, 1, '2021-05-20', 2, 6000, 'Active')
#session.add(customer)
#session.add(order)
#session.add(employee)
session.add(payment)
#session.add(room)
#session.add(roomtype)
#session.add(booking)
session.commit()