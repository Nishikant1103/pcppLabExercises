'''
Objectives
improving the student's skills in interacting with the SQLite database;
using known SQL statements.

Scenario
The application is almost ready. Let's add the missing functionalities to it:

1. Create a method called change_priority, responsible for updating task priority. The method should get the id of the task from the user and its new priority (greater than or equal to 1).
2. Create a method called delete_task, responsible for deleting single tasks. The method should get the task id from the user.

Implement a simple menu consisting of the following options:
1. Show Tasks
2. Add Task
3. Change Priority
4. Delete Task
5. Exit

where:
Show Tasks (calls the show_tasks method)
Add Task (calls the add_task method)
Change Priority (calls the change_priority method)
Delete Task (calls the delete_task method)
Exit (interrupts program execution)

The program should obtain one of these options from the user, and then call the appropriate method of the TODO object. Choosing option 5 must terminate the program. A menu should be displayed in an infinite loop so that the user can choose an option multiple times.

'''

import sqlite3


class Tasks:
    def __init__(self):
        self.conn = sqlite3.connect('tasks.db')
        self.c = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.c.execute(''' CREATE TABLE IF NOT EXISTS tasks(
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        priority INTEGER NOT NULL
        );''')

    def add_task(self):
        name = input('Enter task name:')
        while name == "":
            name = input('Task name cannot be null, please try again:')
        search_result = self.find_task(name)

        while search_result:
            name = input('Task name already exist in the table, please try again:')
            search_result = self.find_task(name)

        priority = int(input('Enter task priority:'))
        while priority < 1:
            priority = int(input('Priority cannot be less than 1, please try again:'))

        self.c.execute('INSERT INTO tasks (name, priority) VALUES (?,?)', (name, priority))

    def find_task(self, search_task):
        for row in self.c.execute(f'SELECT * FROM tasks WHERE name = "{search_task}"'):
            print(row)
            return True

    def find_task_by_id(self, task_id):
        for row in self.c.execute(f'SELECT * FROM tasks WHERE id = "{task_id}"'):
            print(row)
            return True

    def show_tasks(self):
        for row in self.c.execute('SELECT * FROM tasks'):
            print(row)

    def change_priority(self, task_id, new_priority):
        self.c.execute(f'UPDATE tasks SET priority = {new_priority} WHERE id = {task_id}')

    def delete_task(self, task_id):
        self.c.execute(f'DELETE FROM tasks WHERE id = {task_id}')


def get_user_input():
    user_input = 0
    while user_input not in (1, 2, 3, 4, 5):
        user_input = int(input('''Which operation you would like me to perform?'
                                1. Show Tasks 
                                2. Add Task 
                                3. Change Priority 
                                4. Delete Task
                                5. Exit
                                Please enter a corresponding number, e.g. please enter 2 if you would like to add task.
                                Enter your option here: '''))

    return user_input


if __name__ == "__main__":

    tasksObject = Tasks()

    while True:
        operation = get_user_input()
        if operation == 1:
            tasksObject.show_tasks()

        elif operation == 2:
            tasksObject.add_task()

        elif operation == 3:
            task_found = False
            while not task_found:
                task_id = int(input("Please enter an existing task id: "))
                task_found = tasksObject.find_task_by_id(task_id)

            task_priority = 0
            while task_priority not in range(1, 100):
                task_priority = int(input("Please input task priority as a integer from 1-100: "))

            tasksObject.change_priority(task_id, task_priority)

        elif operation == 4:
            task_found = False
            while not task_found:
                task_id = int(input("Please enter an existing task id: "))
                task_found = tasksObject.find_task_by_id(task_id)
            tasksObject.delete_task(task_id)

        elif operation == 5:
            break
