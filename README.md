# Task Tracker CLI

Sample solution for the [Task Tracker](https://roadmap.sh/projects/task-tracker) from [roadmap.sh](https://roadmap.sh)

This little app basically allows you to create new tasks, mark them as "todo", "done" or "in-progress".
Also you can delete a task, update it or see them as a list, and you can set a filter to the list too. You can see all the task you've done, or are in progress, etc.

## How to run
Clone the repository and run the following command:  
```
git clone https://github.com/carlosmperezm/task-tracker-cli.git
cd task-tracker
```
There are a few commands you can use, here are some examples:

Add a new task:
```
task-cli add "My new Task"
```
List all the tasks:
```
task-cli list
```
The list command also have a optional paramater -flag or -f to filter the list like this:
```
task-cli list -flag todo
```
the output would be a list with only contains the tasks you have to do.
You can also try:
```
task-cli list -flag done
```
this shows you all the list you've done
or
```
task-cli list -flag in-progress
```
this shows you all the list you have in progress

Update a task:
this takes the task id and the new description 
```
task-cli update 1 "new task updated"
```

Delete a task by id:
```
task-cli delete 3
```



