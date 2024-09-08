import csv
import re
import random

class Task:
    def __init__(self, task_name: str, chargeable: str):
        self.task_id = self.generate_task_id()
        self.task_name = self.validate_task_name(task_name)
        self.chargeable = self.validate_chargeable(chargeable)

    @staticmethod
    def generate_task_id() -> str:
        # Generate a unique task ID
        random_number = random.randint(100000, 999999)
        return f"TSK_{random_number}"

    @staticmethod
    def validate_task_name(task_name: str) -> str:
        # Validate the task name using a regular expression
        pattern = re.compile(r'^[A-Za-z0-9\-_ ]+$')
        if not pattern.match(task_name):
            raise ValueError("Invalid task name. Only letters, digits, hyphens, underscores, and spaces are allowed.")
        return task_name

    @staticmethod
    def validate_chargeable(chargeable: str) -> bool:
        # Convert the chargeable string to a boolean value
        if chargeable.lower() in ['true', 'yes']:
            return True
        elif chargeable.lower() in ['false', 'no']:
            return False
        else:
            raise ValueError("Invalid chargeable value. It should be True/False or Yes/No.")

    def save_to_file(self, filename="tasks.txt"):
        # Save the task details to a text file
        with open(filename, 'a') as file:
            file.write(f"{self.task_id}, {self.task_name}, {self.chargeable}\n")

    def __repr__(self):
        return f"Task({self.task_id}, {self.task_name}, {self.chargeable})"
def create_tasks_from_csv(filename: str):
    tasks = []
    try:
        with open("C:/Users/GNANESH GANTA/tasks(2).csv", mode='r') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                task = Task(task_name=row['task_name'], chargeable=row['chargeable'])
                task.save_to_file()
                tasks.append(task)
    except FileNotFoundError:
        print(f"Error: The file {filename} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    return tasks
def create_new_task_manually(task_name: str, chargeable: str):
    try:
        task = Task(task_name, chargeable)
        task.save_to_file()
        print(f"Task created successfully: {task}")
    except ValueError as ve:
        print(f"Task creation failed: {ve}")
import csv
import re
import random

class Task:
    def __init__(self, task_name: str, chargeable: str, rate_card=None):
        self.task_id = self.generate_task_id()
        self.task_name = self.validate_task_name(task_name)
        self.chargeable = self.validate_chargeable(chargeable)
        self.rate_card = self.validate_rate_card(rate_card) if self.chargeable else None

    @staticmethod
    def generate_task_id() -> str:
        random_number = random.randint(100000, 999999)
        return f"TSK_{random_number}"

    @staticmethod
    def validate_task_name(task_name: str) -> str:
        pattern = re.compile(r'^[A-Za-z0-9\-_ ]+$')
        if not pattern.match(task_name):
            raise ValueError("Invalid task name. Only letters, digits, hyphens, underscores, and spaces are allowed.")
        return task_name

    @staticmethod
    def validate_chargeable(chargeable: str) -> bool:
        if chargeable.lower() in ['true', 'yes']:
            return True
        elif chargeable.lower() in ['false', 'no']:
            return False
        else:
            raise ValueError("Invalid chargeable value. It should be True/False or Yes/No.")

    @staticmethod
    def validate_rate_card(rate_card) -> float:
        if isinstance(rate_card, (int, float)) and rate_card > 0:
            return float(rate_card)
        else:
            raise ValueError("Invalid rate card value. It should be a positive integer or float.")

    def save_to_file(self, filename="tasks.txt"):
        with open(filename, 'a') as file:
            file.write(f"{self.task_id}, {self.task_name}, {self.chargeable}, {self.rate_card}\n")

    def __repr__(self):
        return f"Task({self.task_id}, {self.task_name}, {self.chargeable}, {self.rate_card})"

if __name__ == "__main__":
    # Create tasks from a CSV file
    tasks = create_tasks_from_csv('tasks.csv')
    print(f"{len(tasks)} tasks created from the CSV file.")

    # Manually create a new task
    create_new_task_manually("Legal Consultation", "Yes")
    create_new_task_manually("Documentation Review", "True")
    create_new_task_manually("Client Meeting", "No")
