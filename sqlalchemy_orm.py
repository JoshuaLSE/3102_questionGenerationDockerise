from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
import sqlalchemy as db
from sqlalchemy.ext.declarative import declarative_base


class SQLStuff:
    Base = declarative_base()

    class Test(Base):
        __tablename__ = 'test_table'

        name = db.Column(db.VARCHAR(20), primary_key=True)
        color = db.Column(db.VARCHAR(10))

    def __init__(self, username, password, ip, port, table_name):
        # engine = db.create_engine(
        #     "mysql+pymysql://root:root@localhost:3306/02db")
        engine = db.create_engine(
            "mysql+pymysql://%s:%s@%s:%s/%s" % (username, password, ip, port, table_name))
        self.Session = sessionmaker(bind=engine)
        self.session = self.Session()

    def get_all(self):
        result = self.session.query(self.Test.name, self.Test.color).all()
        print(result)

    def find(self, colour):
        result = self.session.query(self.Test.name, self.Test.color).filter(self.Test.color == colour).all()
        print(result)

    def update(self, Old_Colour, New_Colour):
        try:
            statement = select(self.Test).where(self.Test.color == Old_Colour)
            new_colour = self.session.scalars(statement).one()
            new_colour.color = New_Colour
            self.session.commit()
        except Exception as e:
            print(e)

    def delete(self, colour):
        statement = self.session.query(self.Test).filter(self.Test.color == colour).delete()
        self.session.commit()

    def insert(self, name, color):
        self.session.add(self.Test(name=name, color=color))
        self.session.commit()
