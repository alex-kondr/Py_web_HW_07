from datetime import date
from faker import Faker
from random import randint, sample

from connect_db import session
from models import Group, Student, Teacher, Subject, Grade


NUMBER_STUDENTS = 50
NUMBER_GROUPS = 3
NUMBER_TEACHERS = 5
NUMBER_SUBJECTS = 8
NUMBER_GRADES = 20


def generate_fake_data(number_students: int,
                       number_groups: int,
                       number_teachers: int,
                       number_subjects: int) -> tuple[list]:

    faker = Faker()

    fake_students = [faker.name() for _ in range(number_students)]
    fake_groups = [faker.company() for _ in range(number_groups)]
    fake_teachers = [faker.name() for _ in range(number_teachers)]

    list_subjects = ["English",
                     "math",
                     "art",
                     "science",
                     "history",
                     "music",
                     "geography",
                     "Physical Education",
                     "drama",
                     "biology",
                     "chemistry",
                     "physics",
                     "Information Technology",
                     "foreign languages",
                     "social studies",
                     "technology",
                     "philosophy",
                     "graphic design",
                     "literature",
                     "algebra",
                     "geometry"]

    fake_subjects = sample(list_subjects, k=number_subjects)

    return fake_students, fake_groups, fake_teachers, fake_subjects


def insert_to_db(students: list,
                 groups: list,
                 teachers: list,
                 subjects: list) -> None:

    [session.add(Group(name=group)) for group in groups]
    session.commit()    
    
    [session.add(Student(name=student, group_id=randint(1, NUMBER_GROUPS)))
                    for student in students]
    session.commit()    
    
    [session.add(Teacher(name=teacher)) for teacher in teachers]
    session.commit()
    
    [session.add(Subject(name=subject, teacher_id=randint(1, NUMBER_TEACHERS)))
                    for subject in subjects]
    session.commit()

    for ns in range(1, NUMBER_STUDENTS+1):
        for _ in range(NUMBER_GRADES):
            grade_date = date(
                year=2023, month=randint(1, 12), day=randint(1, 20))
            session.add(Grade(
                rating=randint(60, 100), 
                date=grade_date,
                student_id=ns, 
                subject_id=randint(1, NUMBER_SUBJECTS)
            ))
            
    session.commit()


if __name__ == "__main__":

    fake_data = generate_fake_data(
        NUMBER_STUDENTS, NUMBER_GROUPS, NUMBER_TEACHERS, NUMBER_SUBJECTS)
    
    insert_to_db(*fake_data)
