from argparse import ArgumentParser
import os

from src.model import Task

json_file_path:str = os.getcwd()+'/tasks.json'

def add(description:str)->None:
    with open(json_file_path,'a') as file:
        task = Task(description)
        file.write(task.description+'\n')

    print('Task Added Successfully')



def update(task_id:str)->None:...
def delete(task_id:str)->None:...
def mark_as_done(task_id:str)->None:...
def mark_as_in_progress(task_id:str)->None:...

def all_tasks()->None:...
def all_done()->None:...
def all_not_done()->None:...
def all_in_progress()->None:...






def main()->None:
    parser:ArgumentParser = ArgumentParser()
    subparser = parser.add_subparsers(dest='command')

    parser_add:ArgumentParser = subparser.add_parser('add',help='add a new task')
    parser_add.add_argument('task_description', help='Add a description to the task')

    args = parser.parse_args()

    if args.command=='add':
        add(args.task_description)
    else:
        parser.print_help()


