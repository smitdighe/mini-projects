tasks = []
while True:
    print("\n1.Add 2.View 3.Remove 4.Exit")
    c = input("Enter choice: ")
    if c == "1":
        tasks.append(input("Enter task: "))
    elif c == "2":
        [print(i+1, task) for i, task in enumerate(tasks)]
    elif c == "3":
        tasks.pop(int(input("Enter task number: ")) - 1)
    elif c == "4":
        break
    else:
        print("Invalid choice!")