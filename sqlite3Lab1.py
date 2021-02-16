'''
Objectives:
improving the student's skills in interacting with the SQLite database;
using known methods of the Cursor object.
Scenario:
Our TODO application requires you to add a little security and display the data saved in the database. Your task is to implement the following functionalities:

Create a find_task method, which takes the task name as its argument. The method should return the record found or None otherwise.
Block the ability to enter an empty task (the name cannot be an empty string).
Block the ability to enter a task priority less than 1.
Use the find_task method to block the ability to enter a task with the same name.
Create a method called show_tasks, responsible for displaying all tasks saved in the database.
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

    def show_tasks(self):
        for row in self.c.execute('SELECT * FROM tasks'):
            print(row)


tasksObject = Tasks()

for i in range(3):
    tasksObject.add_task()

task_name = input("find task: ")
tasksObject.find_task(task_name)
tasksObject.show_tasks()
