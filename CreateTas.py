Boo = True

def Task():

    task = []

    while Boo:

        print("1. Add a Task \n 2. View Tasks \n 3. Remove a Task \n 4. Quit")

        choc = int(input("Enter number : "))

        if choc == 1:

            task.append(input("Enter a Task : "))

        elif choc == 2:

            if task:

                print("Task : ")

                for tasr in task:

                    print(tasr)

            else:

                print("No Task")

        elif choc == 3:

            if task:

                taskar = input("Enter the task for remove : ")

                if taskar in task:

                    task.remove(taskar)

                    print("Task removed")

                else:

                    print("Task not found")

        elif choc == 4:

            break

        else:

            print("Enter number 1 2 3 4")

print(Task())