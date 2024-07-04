# Project Title: Python - Object-relational mapping

## Table of Contents
1. About
2. Learning Objectives
3. Requirements
4. Getting Started
5. Contributing
6. License

## About <a name="about"></a>
This project is part of the curriculum of the ALX Software Engineering program. The main objective of this project is to understand and implement the linking of Python with Databases.
## Background Context <a name="background-context"></a>
In this project, you will link two amazing worlds: Databases and Python! In the first part, you will use the module `MySQLdb` to connect to a MySQL database and execute your SQL queries. n the second part, you will use the module `SQLAlchemy`  an Object Relational Mapper (ORM).

The biggest difference is: no more SQL queries! Indeed, the purpose of an ORM is to abstract the storage to the usage. With an ORM, your biggest concern will be “What can I do with my objects” and not “How this object is stored? where? when?”. You won’t write any SQL queries only Python code. Last thing, your code won’t be “storage type” dependent. You will be able to change your storage easily without re-writing your entire project.
Without ORM:
```
conn = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="root", db="my_db", charset="utf8")
cur = conn.cursor()
cur.execute("SELECT * FROM states ORDER BY id ASC") # HERE I have to know SQL to grab all states in my database
query_rows = cur.fetchall()
for row in query_rows:
    print(row)
cur.close()
conn.close()
```
With an ORM:
```
engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format("root", "root", "my_db"), pool_pre_ping=True)
Base.metadata.create_all(engine)

session = Session(engine)
for state in session.query(State).order_by(State.id).all(): # HERE: no SQL query, only objects!
    print("{}: {}".format(state.id, state.name))
session.close()
```
Do you see the difference? Cool, right?

The biggest difficulty with ORM is: The syntax!

Indeed, all of them have the same type of syntax, but not always. Please read tutorials and don’t read the entire documentation before starting, just jump on it if you don’t get something.

## Learning Objectives <a name="learning-objectives"></a>
At the end of this project, I am expected to be able to explain to anyone, without the help of Google:
- Why Python programming is awesome
- How to connect to a MySQL database from a Python script
- How to `SELECT` rows in a MySQL table from a Python script
- How to `INSERT` rows in a MySQL table from a Python script
- What ORM means
- How to map a Python Class to a MySQL table
- How to create a Python Virtual Environment

## Requirements <a name="requirements"></a>
- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- Your files will be executed with `MySQLdb` version `2.0.x`
- Your files will be executed with `SQLAlchemy` version `1.4.x`
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
- A `README.md` file, at the root of the folder of this project, is mandatory
- Your code should use the pycodestyle (version `2.8.*`)
- All your files must be executable
- The length of your files will be tested using `wc`
- All your modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
- All your classes should have a documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
- All your functions (inside and outside a class) should have a documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)
- A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)

## Getting Started <a name="getting-started"></a>
1. Clone this repository: `git clone https://github.com/Pritchad25/alx-higher_level_programming.git`
2. Access the project directory: `cd 0x0F-python-object_relational_mapping`
3. Run any executable file in the directory

## Contributing <a name="contributing"></a>
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License <a name="license"></a>
ALX 2024 - [alxafrica](https://www.alxafrica.com)
