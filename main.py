import argparse
from sqlalchemy import select
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
                    type=datetime)

parser.add_argument("--student_id", 
                    metavar="Value for Grade", 
                    type=int)

parser.add_argument("--subject_id", 
                    metavar="Value for Grade", 
                    type=int)

parser.add_argument("--id", 
                    metavar="ID record number", 
                    type=int)

args = parser.parse_args()

# print(vars(args))

# for key, value in vars(args).items():
#     print(f"{key=}: {value=}")

args_for_model = {key: value for key, value in vars(args).items() if value and key not in ("action", "model")}

# print(args_for_model)


def get_model(model: str):

    models = {
        "Grade": Grade,
        "Student": Student,
        "Group": Group,
        "Subject": Subject,
        "Teacher": Teacher
    }
    
    return models.get(model)


def create_record():
    
    model = get_model(args.model)
    session.add(model(**args_for_model))
    session.commit()


def create_teacher():
    
    # session.add(
    Teacher(**{"name": args.name})
    print(Teacher.id.key.index)  # , {Teacher.name=}")
    # session.commit()
    

def create_group():
    
    session.add(Group(name=args.name))
    session.commit()
    

def create_student():
    
    session.add(Student(name=args.name, 
                        group_id=args.group_id))
    session.commit()
    

def create_subject():
    
    session.add(Subject(name=args.name, 
                        teacher_id=args.teacher_id))
    session.commit()
    

def create_grade():
    
    session.add(Grade(rating=args.rating,
                      date=args.date,
                      student_id=args.student_id,
                      subject_id=args.subject_id))
    session.commit()


def remove_record():
    
    model = get_model(args.model)
    
    session.query(model).filter(model.id == args.id).delete()
    session.commit()
    
    
def list_records():
    
    model = get_model(args.model)
    
    result = session.execute(
        select(model.name)
    ).all()
    
    print(result)
    

def update_model():
    
    model = get_model(args.model)
    session.merge(model(id=args.id, name=args.name))
    session.commit()    
    
    
def get_action(action: str):
    
    actions = {
        "create": create_record,
        "create Teacher": create_teacher,
        "create Group": create_group,
        "create Subject": create_subject,
        "create Student": create_student,
        "create Grade": create_grade,
        f"list {args.model}": list_records,
        f"update {args.model}": update_model,
        f"remove {args.model}": remove_record
    }
    
    return actions.get(action)


if __name__ == "__main__":
    
    try:        
        action = get_action(args.action)
        action()
        
    except SQLAlchemyError as e:
        print(e.args)