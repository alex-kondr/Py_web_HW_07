import argparse
from sqlalchemy.exc import SQLAlchemyError
from datetime import datetime

from connect_db import session
from models import Grade, Student, Group, Subject, Teacher



parser = argparse.ArgumentParser(
    prog="Working with the database",
    description="Working with the database. Actions: create, list, update, remove")

parser.add_argument("-a", "--action", 
                    metavar="Choice action: create, list, update, remove", 
                    choices=("create", "list", "update", "remove"),
                    type=str)

parser.add_argument("-m", "--model", 
                    metavar="Choice model",
                    choices=("Grade", "Student", "Group", "Subject", "Teacher"),
                    type=str)

parser.add_argument("-n", "--name", 
                    metavar="Value for Student, Group, Subject, Teacher", 
                    type=str)

parser.add_argument("--group_id", 
                    metavar="Value for Group", 
                    type=int)

parser.add_argument("--teacher_id", 
                    metavar="Value for Subject", 
                    type=int)

parser.add_argument("-r", "--rating", 
                    metavar="Value for Grade", 
                    type=int)

parser.add_argument("-d", "--date", 
                    metavar="Value for Grade", 
                    type=date)

parser.add_argument("--student_id", 
                    metavar="Value for Grade", 
                    type=date)

parser.add_argument("--subject_id", 
                    metavar="Value for Grade", 
                    type=date)

parser.add_argument("--id", 
                    metavar="ID record number", 
                    type=int)

args = parser.parse_args()

# print(list(Teacher.__table__.columns))

# print(vars(args))

def get_model(model: str):

    models = {
        "Grade": Grade,
        "Student": Student,
        "Group": Group,
        "Subject": Subject,
        "Teacher": Teacher
    }
    
    return models.get(model)


def commit_record(record):
    
    session.add(record)
    session.commit()


def create_teacher(name: str):    
    return Teacher(name=name)


def create_group(name: str):
    return Group(name=name)

def create_student(name: str, group_id:int=None):
    return Student(name=name, group_id=group_id)

def create_subject(name: str, teacher_id:int=None):
    return Subject(name=name, teacher_id=teacher_id)


def create_grade(rating: int, date=datetime().now().date):
    return 


def remove_record(model: str, **kwargs):
    
    model = get_model(model)
    id = kwargs.get("id")
    
    session.query(model).filter(model.id == id).delete()
    session.commit()
    
    
def get_action(action: str):
    
    actions = {
        # "create": create_record,
        "update": session.merge,
        "remove": remove_record
    }
    
    return actions.get(action)


if __name__ == "__main__":
    
    # model = MODELS[args.model]
    
    # try:
    #     session.add(model(fullname=args.name))
    #     session.commit()
    # except SQLAlchemyError as e:
    #     print(e.args)
    
    # record = session.query(Teacher).filter(Teacher.id==6)
    
    # session.merge(Teacher(id=6, fullname="Krya1"))
    # session.commit()
    
    
    # try:
        
    #     action = get_action(args.action)
    #     action(args.model, vars(args))
        
    # except SQLAlchemyError as e:
    #     print(e.args)
    
    pass
