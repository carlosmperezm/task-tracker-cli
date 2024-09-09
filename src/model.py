from typing import Any
from src.status import Status
from datetime import datetime

class Task:

    def __init__(self,task_id:int,description:str,status:Status=Status.todo)->None:
        self.description:str=description
        self.status:Status=status
        self.created_at:dict[str,Any] = self.created_at()
        self.updated_at:dict[str,Any] = self.updated_at()
        #####################################################

        self.task_id:int = task_id
        return super().__init__()


    def to_dict(self)->dict:
        return dict(
                task_id=self.task_id,
                status=self.status,
                description=self.description,
                created_at=self.created_at,
                updated_at=self.updated_at
             )
    
    def created_at(self)->dict[str,Any]:
        # TODO: Check if works
        now:datetime = datetime.now()
        date:dict[str,Any] = {
                'year':now.year,
                'month':now.month,
                'day':now.day,
                'hour':now.hour,
                'minute':now.minute,
                'second':now.second,
                'microsecond':now.microsecond,
                }
        return date


    def updated_at(self)->dict[str,Any]:
        # TODO: Check if works
       return self.created_at


