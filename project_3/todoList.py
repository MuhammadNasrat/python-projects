
todoList = []

while(True):
    userAction = input('Enter a command (view, add, remove, exit) : ')

    if userAction == 'view':
       if not todoList :
        print('No tasks to view')
       else:
           for task in todoList:
            print(task)       

    elif userAction == 'add':
       task = input('add the task you want : \n')
       todoList.append(task)
       print('task added')

    elif userAction == 'remove':
        if not todoList:
            print('No tasks to remove')
        else:
            task = input('enter the task you want to remove \n')
        if task in todoList:
             todoList.remove(task)
             print('This task is removed')
        else:
            print('This task not founded')    

    elif userAction == 'exit':
         break
 
    else:
       print('Invalid command')