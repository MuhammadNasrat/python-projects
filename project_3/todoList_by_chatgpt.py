todo_list = []

def view_tasks():
    if not todo_list:
        print('No tasks to view')
    else:
        for task in todo_list:
            print(task)

def add_task():
    task = input('Add the task you want:\n')
    todo_list.append(task)
    print('Task added')

def remove_task():
    if not todo_list:
        print('No tasks to remove')
    else:
        task = input('Enter the task you want to remove:\n')
        if task in todo_list:
            todo_list.remove(task)
            print('This task is removed')
        else:
            print('This task not found')

def main():
    while True:
        user_action = input('Enter a command (view, add, remove, exit): ').lower()

        if user_action == 'view':
            view_tasks()
        elif user_action == 'add':
            add_task()
        elif user_action == 'remove':
            remove_task()
        elif user_action == 'exit':
            break
        else:
            print('Invalid command')

if __name__ == "__main__":
    main()
