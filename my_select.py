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
    ).mappings().all()
    
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


def select_3():
    
    result = session.execute(
        select(func.round(func.avg(Grade.rating), 1).label("avg_rating"), Group.name.label("group"), Subject.name.label("subject"))
        .select_from(Grade)
        .join(Student)
        .join(Subject)
        .join(Group)
        .filter(Subject.name == "music")
        .group_by(Group.id, Subject.id)
        .order_by(desc("avg_rating"))
        ).mappings().all()
    
    return result


def select_4():
    
    result = session.execute(
        select(func.round(func.avg(Grade.rating)).label("avg_rating"))
    ).mappings().all()
    
    return result


def select_5():
    
    result = session.execute(
        select(Subject.name.label("subject"), Teacher.fullname.label("teacher"))
        .join(Subject)
    ).mappings().all()
    
    return result


def select_6():
    
    group = "Young LLC"
    
    result = session.execute(
        select(Student.fullname.label("student"), Group.name.label("group"))
        .select_from(Student)
        .join(Group)
        .where(Group.name == group)
    ).mappings().all()
    
    return result


def select_7():
    
    subject = "music"
    group = "Young LLC"
    
    result = session.execute(
        select(Student.fullname.label('student'), Grade.rating, Grade.date, Group.name.label('group'), Subject.name.label('subject'))
        .select_from(Grade)
        .join(Student)
        .join(Group)
        .join(Subject)
        .where(Subject.name == subject)
        .where(Group.name == group)
        .order_by(Student.fullname)
    ).mappings().all()
    
    return result


def select_8():
    
    result = session.execute(
        select(func.round(func.avg(Grade.rating), 1).label("rating"), Teacher.fullname.label("teacher"), Subject.name.label('subject'))
        .select_from(Grade)
        .join(Subject)
        .join(Teacher)
        .group_by(Teacher.id, Subject.id)
    ).mappings().all()
    
    return result


def select_9():
    
    student = "Nicole Lambert"

    result = session.execute(
        select(Subject.name.label("subject"), Student.fullname.label("student"))
        .select_from(Subject)
        .join(Grade)
        .join(Student)
        .where(Student.fullname == student)
        .group_by(Subject.id)
    ).mappings().all()

    return result


def select_10():
    
    student = "Nicole Lambert"
    teacher = "Jasmine Martin"

    result = session.execute(
        select(Subject.name.label("subject"))
        .select_from(Grade)
        .join(Student)
        .join(Subject)
        .join(Teacher)
        .where(Student.fullname == student)
        .where(Teacher.fullname == teacher)
        .group_by(Subject.id)
    ).mappings().all()

    return result


def select_11():
    
    student = "Nicole Lambert"
    teacher = "Jasmine Martin"

    result = session.execute(
        select(func.round(func.avg(Grade.rating), 1).label("avg_rating"))
        .select_from(Grade)
        .join(Student)
        .join(Subject)
        .join(Teacher)
        .where(Student.fullname == student)
        .where(Teacher.fullname == teacher)
        .group_by(Student.id, Teacher.id)
    ).mappings().all()

    return result


def select_12():
    
    subject = "music"
    group = "Young LLC"
    
    def create_execute(select_: list|tuple):
        
        execute_ = (select(*select_)
                    .select_from(Grade)
                    .join(Student)
                    .join(Subject)
                    .join(Group)
                    .where(Group.name == group)
                    .where(Subject.name == subject)
                    )
        
        return execute_
    
    select_main = (Grade.rating, 
                   Grade.date, 
                   Student.fullname.label("student"), 
                   Group.name.label("group"), 
                   Subject.name.label("subject")
                   )
    
    select_minor = (Grade.date,)
    
    
    execute_minor = (create_execute(select_minor)
                     .order_by(desc(Grade.date))
                     .limit(1)
                     .scalar_subquery()
                     )
    
    execute_main = (create_execute(select_main)
                    .where(Grade.date == execute_minor)
                    )
    
    result = session.execute(
        execute_main
        ).mappings().all()
    
    return result


if __name__ == "__main__":
    
    print(select_12())