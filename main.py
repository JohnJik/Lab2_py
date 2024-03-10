import random
DATABASE = []

def create_record(a,b):
    try:
        if b:
            r={}
            for i in range(len(a)):
                r[a[i]]=b[i]
            DATABASE.append(r)
            print("Успішно створено")
    except Exception as err:
        print("Помилка при створенні:",err)

def create_user(a,b):
    try:
        if b:
            u={}
            for i in range(len(a)):
                u[a[i]]=b[i]
            DATABASE.append(u)
            print("Успішно створено")
    except Exception as err:
        print("Помилка при створенні:",err)

def update_record(r):
    try:
        b=r.split(",")
        for i,q in enumerate(DATABASE):
            if q.get("i")==int(b[0]):
                for j in range(1,len(b)):
                    q[list(q.keys())[j]]=b[j]
                print("Успішно оновлено")
                return
        print("Не знайдено")
    except Exception as err:
        print("Помилка при оновленні:",err)

def read_record(c):
    try:
        f=[]
        for r in DATABASE:
            if r.get("1")==c or r.get("2")==c:
                f.append(r)
        if f:
            print("Результат:",f)
        else:
            print("Не знайдено")
    except Exception as err:
        print("Помилка при читанні:",err)

def delete_record(i):
    try:
        for j,r in enumerate(DATABASE):
            if r.get("i")==int(i):
                del DATABASE[j]
                print("Успішно видалено")
                return
        print("Не знайдено")
    except Exception as err:
        print("Помилка при видаленні:",err)

def main():
    while True:
        print("\nМеню:")
        print("1.Дія 1")
        print("2.Дія 2")
        print("3.Дія 3")
        print("4.Дія 4")
        print("5.Дія 5")
        print("6.Вийти")
        c=input("Виберіть дію")
        if c=="1":
            a=input("Введіть поля:")
            b=input("Введіть дані:")
            create_record(a.split(","),b.split(","))
        elif c=="2":
            a=input("Введіть поля:")
            b=input("Введіть дані:")
            create_user(a.split(","),b.split(","))
        elif c=="3":
            r=input("Введіть дані:")
            update_record(r)
        elif c=="4":
            d=input("Введіть вміст:")
            read_record(d)
        elif c=="5":
            i=input("Введіть id:")
            delete_record(i)
            break
        else:
            print("Невідома дія")

main()
