class Todo:
    def __init__(self):
        self.tasks = []
    def add(self,task):
        self.tasks.append({'task':task,'status':False})
    def delete(self,ind):
        if 0<=ind<=len(self.tasks):
            self.tasks.pop(ind-1)
        else:
            print("Invalid Task number:")
    def update(self,ind):
        if 0<=ind<=len(self.tasks):
            newone = input("Enter task to Update: ")
            self.tasks[ind-1]['task'] = newone
        else:
            print("Invalid Task number:")
    def completed(self,ind):
        if 0<=ind<=len(self.tasks):
            self.tasks[ind-1]['status'] = True
        else:
            print("Invalid Task number:")
    def display(self):
        for i in range(0,len(self.tasks)):
            if self.tasks[i]['status'] == False:
                print("Task",i+1,self.tasks[i]['task'],"\t",'Pending..')
            else:
                print("Task",i+1,self.tasks[i]['task'],"\t",'Completed..')

td = Todo()
while True:
    print("\nchoose the operation to be perfoemed in To-do list")
    print("1.Add task")
    print("2.Delete task")
    print("3.Completed task")
    print("4.Display all tasks")
    print("5.Update the task")
    print("6.exit")
    opt = int(input())
    if opt ==1:
        taskis = input("Enter the task: ")
        td.add(taskis)
    elif opt==2:
        ind = int(input("Enter number to delete the task:"))
        td.delete(ind)
    elif opt==3:
        ind = int(input("enter completed task Number: "))
        td.completed(ind)
    elif opt==4:
        td.display()
    elif opt==5:
        ind = int(input("Enter the number to update: "))
        td.update(ind)
    elif opt == 6:
        break
    else :
        print("please choose the correct option")
