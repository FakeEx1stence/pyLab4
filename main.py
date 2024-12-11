import lab4

task_list = {
    "1": lab4.task,
}

if __name__ == '__main__':
    choice = input("Оберіть завдання:\n1.Завдання№21 || [0-Вихід]: \n")

    while choice != "0":
        if choice in task_list.keys():
          task_list[choice]()
        else:
          print("Такої відповіді немає!")

        choice = input("Оберіть завдання знову [0-Вихід]: ")
