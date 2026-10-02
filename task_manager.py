# To-Do List
# إنشاء قائمة لتخزين المهام  
tasks = []
# إنشاء دالة لتحميل المهام من الملف
def load_tasks():
    try:
        with open ("tasks.txt", "r") as file:
            for line in file:
                tasks.append(line.strip())  # إزالة الفراغات الزائدة
    except FileNotFoundError:
        pass

# حفظ المهام في الملف
def save_tasks():
    with open("tasks.txt","w") as file:
        for task in tasks:
            file.write(task + "\n")  # حفظ كل مهمة في سطر منفصل

# إضافة مهمة جديدة
def add_task(task):
    tasks.append(task)
    save_tasks()
    print("The task has been added : {task} ")

#  عرض جميع المهام
def show_tasks():
    if not tasks:
        print("you don\'t has any task")
    else:
        print("To-do list \n")
        for i, task in enumerate(tasks,1):
            print(f"{i}. {tasks}")

# حذف مهمة
def remove_task(index):
    if not tasks:
        print("you don\'t has any task")
    else:
        try:
            remove_task = tasks.pop(index - 1)
            save_tasks()
        except IndexError:
            print("Invalid task number!")  # إذا كان الرقم غير موجود
        
# خيارات البرنامم
def main():
    load_tasks()
    # شرح الخيرات للمستخدم
    print("hi and walcome in simple task manager.")# ادخال اختيار المستحدمم
    while True:
        print("\n🔹Task Manager 🔹")
        print("1 : Important addition")
        print("2 : View tasks")
        print("3 : Delete a task")
        print("4 : Exit")
        try:
            choice = int(input("Please select the number to select the operation."))
        except ValueError:
            print("Enter a valid number")
        try:
            if choice in [1,2,3,4] : 
                if choice == 1:
                    task = input("Enter the task:")
                    add_task(task)
                elif choice == 2:
                    show_tasks()
                elif choice == 3:
                    show_tasks()                    
                    try:
                        task_num = int(input("Enter the task number to delete."))
                        remove_task(task_num)
                    except ValueError:
                        print(" Please enter a valid number")
                elif choice == 4:
                    print("good bay") 
        except ValueError:
            print("ijjff")
            continue
if __name__ == "__main__":
    main()