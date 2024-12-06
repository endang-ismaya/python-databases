# imports
from sqlalchemy import create_engine, Column, String, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.exc import IntegrityError

# create database
engine = create_engine("sqlite:///databases/tasks.db", echo=False)
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()


# define models
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    tasks = relationship("Task", back_populates="user", cascade="all, delete-orphan")


class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True)
    title = Column(String(50), nullable=False)
    description = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="tasks")


Base.metadata.create_all(engine)


# utility functions
def get_user_by_email(email):
    return session.query(User).filter_by(email=email).first()


def confirm_action(prompt: str) -> bool:
    return input(f"{prompt} (yes/no):").strip().lower() == "yes"


# CRUD ops
def add_user():
    name, email = input("Enter username: "), input("Enter the email: ")
    if get_user_by_email(email):
        print(f"User already exists: {email}")

    try:
        new_user = User(name=name, email=email)
        session.add(new_user)
        session.commit()
        print(f"User: {name} added!")

    except IntegrityError as e:
        session.rollback()
        print(e)


def add_task() -> None:
    email = input("Enter the email of the user to add task: ")
    user = get_user_by_email(email)

    if not user:
        print(f"No user found with email {email}")
        return

    title, description = input("Enter the title: "), input("Enter the description: ")

    try:
        new_task = Task(
            title=title, description=description, user_id=user.id, user=user
        )
        session.add(new_task)
        session.commit()
        print(f"Task added to database {title}:{description}")

    except IntegrityError as e:
        session.rollback()
        print(e)


# query
def query_users():
    for user in session.query(User).all():
        print(f"ID: {user.id}, Name: {user.name}, Email: {user.email}")


def query_tasks():
    email = input("Enter the email of the user: ")
    user = get_user_by_email(email)

    if not user:
        print(f"No user found with email {email}")
        return

    for task in user.tasks:
        print(f"Task ID: {task.id}, Title: {task.title}")


def update_user():
    email = input("Email of who do you want to update: ")
    user = get_user_by_email(email)

    if not user:
        print(f"No user found with email {email}")
        return

    try:
        user.name = input("Enter new name: ") or user.name
        user.email = input("Enter new email: ") or user.email
        session.commit()
        print("User has been updated!")

    except IntegrityError as e:
        session.rollback()
        print(e)


def delete_user():
    email = input("Email of who do you want to delete: ")
    user = get_user_by_email(email)

    if not user:
        print(f"No user found with email {email}")
        return

    try:
        if confirm_action(f"Are you sure you want to delete: {user.name}?"):
            session.delete(user)
            session.commit()
            print("User has been deleted")

    except IntegrityError as e:
        session.rollback()
        print(e)


def delete_task():
    task_id = input("Enter the Task ID to delete: ")
    task = session.get(Task, task_id)

    if not task:
        print(f"No task found with id {task_id}")
        return

    try:
        if confirm_action(f"Are you sure you want to delete task: {task.title}?"):
            session.delete(task)
            session.commit()
            print("Task has been deleted")

    except IntegrityError as e:
        session.rollback()
        print(e)


# main
def main() -> None:
    actions = {
        "1": add_user,
        "2": add_task,
        "3": query_users,
        "4": query_tasks,
    }

    while True:
        print(
            "\nOptions:\n1. Add User\n2. Add Task\n3. Query Users\n4. Query Tasks\n5. Update User\n6. Delete User"
            "\n7. Delete Task\n8. Exit"
        )

        choice = input("Enter an option: ")
        if choice == "8":
            print("Goodbyeee..")
            break

        action = actions.get(choice)
        if action:
            action()

        else:
            print("That is not an options")


if __name__ == "__main__":
    main()
