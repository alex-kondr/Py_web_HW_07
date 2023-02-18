import argparse
from sqlalchemy.exc import SQLAlchemyError

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
parser.add_argument("-n", "--name", metavar="Value", type=str)
parser.add_argument("--id", metavar="ID record number", type=int)
args = parser.parse_args()

def get_model(model: str);

    models = {
        "Grade": Grade,
        "Student": Student,
        "Group": Group,
        "Subject": Subject,
        "Teacher": Teacher
    }
    
    return models.get(model)


def create_record(model: str, **kwargs):
    
    model = get_model(model)
    name = kwargs.get("name")
    
    session.add(model(name=name))
    session.commit()


def remove_record(model: str, **kwargs):
    
    model = get_model(model)
    id = kwargs.get("id")
    
    session.query(model).filter(model.id == id).delete()
    session.commit()
    
    
def get_action(action: str):
    
    actions = {
        "create": create_record,
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
    try:
        
        action = ACTIONS[args.action]
        action(args.model, id=args.id)
        
    except SQLAlchemyError as e:
        print(e.args)
    
    pass
