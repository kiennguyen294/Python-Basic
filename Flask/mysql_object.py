import sqlalchemy as db
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

Base = declarative_base()

class PerSon(Base):
    __tablename__ = 'person'
    id = Column(Integer, primary_key= True)
    name = Column(String(250), nullable= False)

class Address(Base):
    __tablename__ = 'address'

    id = Column(Integer, primary_key= True)
    street_name = Column(String(250))
    street_number = Column(String(250))
    post_code = Column(String(250), nullable=False)
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship(PerSon)


def create_connection():
    engine = db.create_engine('mysql+pymysql://root:ViettelidcIDC@127.0.0.1:3306/cloudwatch')
    Session = sessionmaker(bind=engine)
    session = Session()
    return session
