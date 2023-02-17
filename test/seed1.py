from datetime import date
from faker import Faker
from random import randint, sample

from connect_db import session
from models import Group, Student, Teacher, Subject, Grade


NUMBER_STUDENTS = 50
NUMBER_GROUPS = 3
NUMBER_TEACHERS = 5
NUMBER_SUBJECTS = 8
NUMBER_EVALUATIONS = 20


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


def prepare_data(students: list,
                 groups: list,
                 teachers: list,
                 subjects: list) -> tuple[list[tuple]]:

    # [session.add(Group(name=group)) for group in groups]
    session.add(Group(name=groups))
    
    session.commit()


if __name__ == "__main__":
    
    # session.add(Group(name="HW-101"))
    # session.commit()

    fake_data = generate_fake_data(
        NUMBER_STUDENTS, NUMBER_GROUPS, NUMBER_TEACHERS, NUMBER_SUBJECTS)
    prepare_data(*fake_data)