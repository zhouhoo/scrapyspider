from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base

Basemodel = declarative_base()


class Zufang(Basemodel):
    __tablename__ = 'zufang' # 数据库表名
    id = Column(Integer, primary_key=True,autoincrement=True)
    name = Column(String(200))
    area = Column(String(30))
    price = Column(Integer)
    space = Column(String(20))
    types = Column(String(10))
    link = Column(String(100))

    def __init__(self,name,area,price,space,types,link):
        self.name = name
        self.area = area
        self.price = price
        self.space = space
        self.types = types
        self.link = link
