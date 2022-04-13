import random

def fetchTodoList()->dict:
    todoList=[
        {
            "name":"task1",
            "id":"1",
            "status":"done"
        },
        {
            "name":"task2",
            "id":"2",
            "status":"pending"
        },
        {
            "name":"task1",
            "id":"1",
            "status":"stopped"
        },
    ]
    return todoList

def updateTaskName(task_id:int,name:str)->None:
    pass
def updateTaskStatus(task_id:int,status:str)->None:
    pass
def get_name():
    return random.choice(["Aziz","Souha","Wafa","Baha","Omar","Mellouli","Mou7eb"])