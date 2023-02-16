from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine("mysql+mysqlconnector://root:password@localhost/notes")
Session = sessionmaker(bind=engine)
session = Session()

