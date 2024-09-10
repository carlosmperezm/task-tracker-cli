from typing import Any,Dict,List
from argparse import ArgumentParser
import os
import json

from src.model import Task
from src.status import Status

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



def update(task_id:str,description:str)->str:
    tasks:list[dict[str,Any] | None]= all_tasks()
    try:
        task_id = int(task_id)
    except Exception as e:
        return f'"{task_id}" is not a valid number'

    for index,task in enumerate(tasks):
        if task.get('task_id') == task_id:
            tasks[index]['description'] = description
            write_json(tasks)
            return 'Data updated successfully'
    return 'No task with that id was found :('

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


def mark_as(status:Status,task_id:str)->str:
    tasks:list[dict[str,Any] | None]= all_tasks()
    try:
        task_id = int(task_id)
    except Exception as e:
        return f'"{task_id}" is not a valid number'

    for index,task in enumerate(tasks.copy()):
        if task.get('task_id') == task_id:
            tasks[index]['status'] = status
            write_json(tasks)
            return f'Task number: {task_id} marked as {status} correctly'
    return 'We couldn\'t find such task :('
    

def mark_as_done(task_id:str)-> str:
    return mark_as(Status.DONE,task_id)
    
def mark_as_in_progress(task_id:str)->str:
    return mark_as(Status.IN_PROGRESS,task_id)

def all_tasks(flag:str|None = None)->List[Dict[str,Any] | None]:
    data:list[dict[str,Any]]=[]

    with open(JSON_FILE_PATH) as file:
        try:
            data = json.load(file)
        except json.JSONDecodeError :
            pass
            
    if flag is None:
        return data

    all_flagged:List[Dict[str,Any] | None]=[]
    for task in data:
        if flag.upper() == task.get('status').upper() :
            all_flagged.append(task)
        elif flag.upper() == task.get('status').upper() :
            all_flagged.append(task)
        elif flag.upper() ==  task.get('status').upper():
            all_flagged.append(task)

    return all_flagged


def main()->None:
    parser:ArgumentParser = ArgumentParser()
    subparser = parser.add_subparsers(dest='command')

    parser_add:ArgumentParser = subparser.add_parser('add',help='Add a new task')
    parser_add.add_argument('task_description', help='Add a description to the task')

    parser_list:ArgumentParser = subparser.add_parser('list', help='Shows all the tasks')
    parser_list.add_argument('-flag','-f',help='Provide a flag in case you want to filter the data')

    parser_delete:ArgumentParser = subparser.add_parser('delete',help='Delete the task when an id is provided')
    parser_delete.add_argument('task_id', help='Provide the id of the specific id you want to delete')

    parser_mark_done:ArgumentParser = subparser.add_parser('mark-done', help='Mark a task as DONE')
    parser_mark_done.add_argument('task_id',help='Provide a id in order to know wich task set as DONE')

    parser_mark_in_progress:ArgumentParser = subparser.add_parser('mark-in-progress', help='Mark a task as IN PROGRESS')
    parser_mark_in_progress.add_argument('task_id',help='Provide a id in order to know wich task set as IN PROGRESS')

    parser_update:ArgumentParser = subparser.add_parser('update', help= 'Updated the task\' description ')
    parser_update.add_argument('task_id',help='Provide an id to know what task to updated')
    parser_update.add_argument('new_description',help='Provide the new description you want to update')


    args = parser.parse_args()

    if args.command=='add':
        add(args.task_description)

    elif args.command =='list':
        print(all_tasks(args.flag))

    elif args.command == 'delete':
        print(delete(args.task_id))

    elif args.command == 'mark-done':
        print(mark_as_done(args.task_id))

    elif args.command == 'mark-in-progress':
        print(mark_as_in_progress(args.task_id))

    elif args.command == 'update':
        print(update(args.task_id, args.new_description))


    else:
        parser.print_help()


