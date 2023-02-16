from sqlalchemy import func, select, desc

from connect_db import session
from models import Group, Student, Teacher, Subject, Grade


def select_1():
    
    result = session.execute(
        select(func.round(func.avg(Grade.rating), 1).label("avg_grade"), Student.fullname)
        .join(Student)
        .group_by(Student.id)
        .order_by(desc("avg_grade"))
        .limit(5)
        ).all()
    
    return result


def select_2():
    
    result = (session.query(
        func.round(func.avg(Grade.rating), 1).label("avg_rating"), Student.fullname, Subject.name)
        .select_from(Grade)
        .join(Student)
        .join(Subject)
        .filter(Subject.name == "music")
        .group_by(Subject.id, Student.id)
        .order_by(desc("avg_rating"))
        .limit(1).all()
        )
    
    return result


if __name__ == "__main__":
    
    print(select_2())