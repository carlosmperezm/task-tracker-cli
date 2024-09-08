from src.status import Status
from datetime import datetime

class Task:
    __counter:int = 0


    def __init__(self,description:str,status:Status=Status.todo)->None:
        self.description:str=description
        self.status:Status=status
        created_at:datetime= datetime.now()
        updated_at:datetime=datetime.now()
        Task.__counter +=1
        self.task_id:int = Task.__counter


    
