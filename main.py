import argparse


parser = argparse.ArgumentParser(
    prog="Working with the database",
    description="Working with the database. Actions: create, list, update, remove")

parser.add_argument("-a", "--action", 
                    metavar="Choice action: create, list, update, remove", 
                    choice=("create", "list", "update", "remove"),
                    type=str)
parser.add_argument("-m", "--model", 
                    metavar="Choice model",
                    choice=("Grade", "Student", "Group", "Subject", "Teacher"),
                    type=str)
parser.add_argument("-n", "--name", metavar="Name record")
parser.add_argument("--id", metavar="ID number record")
args = parser.parse_args()
