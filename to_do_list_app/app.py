import CRUD
import title




def main():
    print("="*25)
    print("1. Add a task")
    print("2. View tasks")
    print("3. Delete a task")
    print("4. Update a task")
    print("5. task status")
    print("6. Exit")
    print("="*25,"\n")

    choice = input("Enter your choice: ")

    if choice == "1":
        CRUD.add_task()
    elif choice == "2":
        CRUD.view_tasks()
    elif choice == "3":
        CRUD.delete_task()
    elif choice == "4":
        CRUD.update_task()
    elif choice == "5":
        CRUD.task_status()
    elif choice == "6":
        CRUD.exit()
    else:
        print("Invalid choice. Please try again.")

        main()

if __name__ == "__main__":
    print("-"*35)
    title.print_title()
    print("-"*35,"\n")
    main()