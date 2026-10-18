import json

import json_db
import app
def status_couting():
    json_db.file_createing()
    
    data = json_db.for_file_reading()
    p_count=0
    c_count=0
    for status in data:
        if status['status'] == "pending":
            p_count += 1
        else:
            c_count += 1
    
    return f"Pending tasks: {p_count}\nCompleted tasks: {c_count}\n"  


def add_task():
    json_db.file_createing()
    title = input("Enter the task you want to do: ")

    data = json_db.for_file_reading()

    new_task = {
        "id": len(data) + 1,
        "title": title,
        "status": "pending"
    }

    data.append(new_task)

    json_db.for_file_writing(data)

    print("Task added successfully!")
    
    app.main()


def view_tasks():
    json_db.file_createing()
    
    data = json_db.for_file_reading()

    if not data:
                print("No tasks found.")
                print("Add a task to view it here")
                add_task()
                return

    print(" === U HAVE TO TO ===    \n")
    for i in data:
        
        print(f"{i['id']} -> {i['title']}")
        print(f"   Status({i['status']})\n")
    print("========================    \n")
    app.main()      

def delete_task():
    json_db.file_createing()
    task_id = int(input("Enter the task id to delete: "))

    data = json_db.for_file_reading()

    for i in data:

        if i['id'] == task_id:
            data.remove(i)

            for index, task in enumerate(data,start=1):
                task['id'] = index

            json_db.for_file_writing(data)
            print("           "+"*"*5)
            print("Task deleted successfully!")
            print("           "+"*"*5,"\n")
            app.main()
            return
        
    print("           "+"*"*5)
    print("Task not found...retry with valid task id")
    print("           "+"*"*5,"\n")
    delete_task()


        
    print(data)
    
def update_task():
    json_db.file_createing()
    task_id = int(input("Enter the task id to update: "))

    data = json_db.for_file_reading()

    for i in data:

        if i["id"] == task_id:
            new_title = input("Enter the new title for the task: ")
            i['title'] = new_title

            json_db.for_file_writing(data)
            print("           "+"*"*5)
            print("Task updated successfully!")
            print("           "+"*"*5,"\n")
            app.main()
            return
        
    print("           "+"*"*5)
    print("Task not found...retry with valid task id")
    print("           "+"*"*5,"\n")            
    update_task()


        
    

def task_status():
    json_db.file_createing()
    
    

    data = json_db.for_file_reading()
    
    for status in data:
        if status['status'] == "pending":
            
            print(f"{status['id']} -> {status['title']} (Status: {status['status']})")
        else:
            print(f"{status['id']} -> {status['title']} (Status: {status['status']})")
            
    
    
    
    print(status_couting())
    task_id = int(input("Enter the task id to update status: "))

    for i in data:

        if i['id'] == task_id:
            new_status = input("Enter the new status for the task (pending/completed): ")
            if new_status.lower() not in ["pending", "completed"]:
                print("Invalid status. Please enter 'pending' or 'completed'.")
                task_status()
                return
            i['status'] = new_status.lower()

            json_db.for_file_writing(data)

            print("           "+"*"*5)
            print("Task status updated successfully!")
            print("           "+"*"*5,"\n")
            app.main()
            return
        
    print("           "+"*"*5)
    print("Task not found...retry with valid task id")
    print("           "+"*"*5,"\n")
    task_status()
    
 
def exit():
    print("thanks for using")





        
