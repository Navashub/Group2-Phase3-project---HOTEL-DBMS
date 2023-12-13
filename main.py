from sqlalchemy import Column, String, Integer, create_engine, VARCHAR, DATE, ForeignKey, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()


class Booking(Base):

    __tablename__ = 'bookings'
    Bookid = Column(Integer, primary_key=True)
    Roomid = Column(Integer, ForeignKey('rooms.Roomid'))
    Customerid = Column(Integer, ForeignKey('customers.Customerid'))
    Bookdate = Column(DATE)
    Checkin = Column(DATE)
    Checkout = Column(DATE)
    status = Column(String)

    def __init__(self, Bookid, Roomid, Customerid, Bookdate, Checkin, Checkout, status):
        pass

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

    def __init__(self, Customerid, Customername, address, phoneno, gender, status):
        pass

    def __repr__(self):
        pass


class Employee(Base):

    __tablename__ = 'employees'
    employeeid = Column(Integer, primary_key=True)
    employeename = Column(String)
    loginid = Column(VARCHAR(50))
    emptype = Column(String)
    status = Column(String)

    def __init__(self, employeeid, employeename, loginid, emptype, status):
        pass

    def __repr__(self):
        pass


class Expense(Base):

    __tablename__ = 'expenses'
    expenseid = Column(Integer, primary_key=True)
    employeeid = Column(Integer, ForeignKey('employees.employeeid'))
    expensetype = Column(String)
    expensemat = Column(Float)
    expensedate = Column(DATE)
    status = Column(String)

    def __init__(self, expenseid, employeeid, expensetype, expensemat, expensedate, status):
        pass

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
        pass

    def __repr__(self):
        pass


class Order(Base):

    __tablename__ = 'orders'
    orderid = Column(Integer, primary_key=True)
    itemid = Column(Integer, ForeignKey('items.itemid'))
    Bookid = Column(Integer, ForeignKey('bookings.Bookid'))
    orderdate = Column(DATE)
    quantity = Column(Float)
    cost = Column(Float)
    status = Column(String)

    def __init__(self, orderid, itemid, Bookid, orderdate, quantity, cost, status):
        pass

    def __repr__(self):
        pass


class Payment(Base):

    __tablename__ = 'payments'
    paymentid = Column(Integer, primary_key=True)
    Bookid = Column(Integer, ForeignKey('bookings.Bookid'))
    paymenttype = Column(VARCHAR(50))
    amount = Column(Float)
    paymentdetail = Column(String)
    paymentdate = Column(DATE)
    status = Column(String)

    def __init__(self, paymentid, Bookid, paymenttype, amount, paymentdetail, paymentdate, status):
        pass

    def __repr__(self):
        pass


class Room(Base):

    __tablename__ = 'rooms'
    Roomid = Column(Integer, primary_key=True)
    Roomtype = Column(String, ForeignKey('roomtypes.Roomtype'))
    Roomnumber = Column(VARCHAR(10))
    status = Column(String)

    def __init__(self, Roomid, Roomtype, Roomnumber, status):
        pass

    def __repr__(self):
        pass


class RoomType(Base):

    __tablename__ = 'roomtypes'
    Roomtypeid = Column(Integer, primary_key=True)
    Roomtype = Column(String)
    Cost = Column(Float)
    status = Column(String)

    def __init__(self, Roomtypeid, Roomtype, Cost, status):
        pass

    def __repr__(self):
        pass
