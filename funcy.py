# Functions for App1 (App-chi)

# Function "Open 'r' " reads the file to its end.
# The "readlines" method turns data into a list.
# With the 'with' operator we avoid .close().
# Write method writes the argument into the path

FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """ Read a text file and returns a list
    of to-do items.
    """
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """ Writes the to-do items list into the text file."""
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)


if __name__ == "__main__":
    """ Condition to exclude further operation from running...
        ...when file is imported elsewhere"""
    print("Hello!")
