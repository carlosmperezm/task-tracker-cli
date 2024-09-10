from typing import Any,Dict,List
from argparse import ArgumentParser
import os
import json

from src.model import Task

JSON_FILE_PATH:str = os.getcwd()+'/tasks.json'

def write_json(data:Dict[str,Any],file_path:str = JSON_FILE_PATH)->None:
    with open(file_path, 'w') as file:
        json.dump(data, file)

def add(description:str)->None:
    task_id:int=1
    data:dict[str,Any]={}
    tasks:list[dict[str,Any] | None]= []

    tasks = all_tasks()
    if tasks != []:
        task_id = tasks[-1].get('task_id') + 1

    task = Task(task_id,description)
    tasks.append(task.to_dict())

    write_json(tasks)
    print('Task Added Successfully')



def update(task_id:str)->None:...

def delete(task_id:str)->str:
    tasks:list[dict[str,Any] | None]= all_tasks()
    try:
        task_id = int(task_id)
    except Exception as e:
        return f'"{task_id}" is not a valid number'

    for index,task in enumerate(tasks.copy()):
        if task.get('task_id') == task_id:
            item_deleted = tasks.pop(index)
            write_json(tasks)
            return f'Successfully deleted item: {item_deleted.get('task_id')}'
    return 'No indexes found'


def mark_as_done(task_id:str)->None:...
def mark_as_in_progress(task_id:str)->None:...

def all_tasks()->List[Dict[str,Any] | None]:
    data:list[dict[str,Any]]=[]
    with open(JSON_FILE_PATH) as file:
        try:
            data = json.load(file)
        except json.JSONDecodeError :
            pass
            
    return data


def all_done()->None:...
def all_not_done()->None:...
def all_in_progress()->None:...






def main()->None:
    parser:ArgumentParser = ArgumentParser()
    subparser = parser.add_subparsers(dest='command')

    parser_add:ArgumentParser = subparser.add_parser('add',help='Add a new task')
    parser_add.add_argument('task_description', help='Add a description to the task')

    parser_list:ArgumentParser = subparser.add_parser('list', help='Shows all the tasks')

    parser_delete:ArgumentParser = subparser.add_parser('delete',help='Delete the task when an id is provided')
    parser_delete.add_argument('task_id', help='Provide the id of the specific id you want to delete')

    args = parser.parse_args()

    if args.command=='add':
        add(args.task_description)
    elif args.command =='list':
        print(all_tasks())
    elif args.command == 'delete':
        print(delete(args.task_id))
        

    else:
        parser.print_help()


