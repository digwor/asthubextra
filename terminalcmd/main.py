import os
import time

def execution_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time of '{func.__name__}': {end_time - start_time:.6f} seconds")
        return result
    return wrapper

class CommandPrompt:
    def __init__(self):
        self.current_directory = os.getcwd()

    @execution_time
    def list_directories(self):
        directories = os.listdir(self.current_directory)
        for item in directories:
            if os.path.isdir(os.path.join(self.current_directory, item)):
                print(item)

    @execution_time
    def change_directory(self, directory_name):
        path = os.path.join(self.current_directory, directory_name)
        if os.path.isdir(path):
            os.chdir(path)
            self.current_directory = os.getcwd()
        else:
            print("Directory not found.")

    @execution_time
    def create_directory(self, directory_name):
        path = os.path.join(self.current_directory, directory_name)
        os.makedirs(path, exist_ok=True)

    @execution_time
    def delete_directory(self, directory_name):
        path = os.path.join(self.current_directory, directory_name)
        if os.path.exists(path) and os.path.isdir(path):
            os.rmdir(path)
        else:
            print("Directory not found.")

    @execution_time
    def rename_directory(self, old_name, new_name):
        old_path = os.path.join(self.current_directory, old_name)
        new_path = os.path.join(self.current_directory, new_name)
        if os.path.exists(old_path) and os.path.isdir(old_path):
            os.rename(old_path, new_path)
        else:
            print("Directory not found.")

    @execution_time
    def view_file(self, file_name):
        file_path = os.path.join(self.current_directory, file_name)
        if os.path.isfile(file_path) and (file_name.endswith('.txt') or file_name.endswith('.md')):
            with open(file_path, 'r') as file:
                print(file.read())
        else:
            print("File not found or unsupported format.")

# Интерфейс командной строки
cmd = CommandPrompt()

while True:
    user_input = input(f"{cmd.current_directory}> ")
    tokens = user_input.split()

    if tokens[0] == "ls" or tokens[0] == "dir":
        cmd.list_directories()

    elif tokens[0] == "cd" and len(tokens) > 1:
        cmd.change_directory(tokens[1])

    elif tokens[0] == "mkdir" and len(tokens) > 1:
        cmd.create_directory(tokens[1])

    elif tokens[0] == "rmdir" and len(tokens) > 1:
        cmd.delete_directory(tokens[1])

    elif tokens[0] == "renamedir" and len(tokens) > 2:
        cmd.rename_directory(tokens[1], tokens[2])

    elif tokens[0] == "view":
        if len(tokens) > 1:
            cmd.view_file(tokens[1])

    elif tokens[0] == "exit":
        break

    else:
        print("Invalid command.")