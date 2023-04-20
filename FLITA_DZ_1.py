set1=set()
set2=set()

#creating a set
def create(set_arg):
    while True:
        
        set_el = input("Enter the set_el: ")
        if (set_el != ''):
            set_arg.add(set_el)
        else:
            return set_arg
   

#output of set

def output(set_arg):
    print(set_arg)
    return None

#adding to  set

def add_el(set_arg):
    while True:
        add_el = input("Enter adding element: ")
        if add_el == '':
            return set_arg
        else:
            set_arg.add(add_el)
        
#deleting of a element of set


def del_el(set_arg):        
    del_el=1
    while del_el != '':
        del_el=input("Enter deleting element: ")
        if del_el in set_arg:
            set_arg.discard(del_el)
        elif not (del_el in set_arg) and del_el != '':
            print("Ivalid input! There is no such element in th set! Try again!")
    else:
        return set_arg
    
    
        
# recursive FUCTION
def answ_func():
        global answ   
        answ = input("Хотите продолжить 'да'или'нет': ")
        if answ == 'нет' or answ == 'НЕТ':
            answ = False
        elif answ == 'да' or answ == 'ДА':
            answ = True
        else: 
            print("Неверный ввод ответа! Повторите ещё раз!")
            answ_func()



        
answ = True
while answ:    
    #CREATE() 
    print("Задаём первое множество")
    set1 = create(set1)
    print("Задаём второе множество")
    set2 = create(set2)
    #OUTPUT()
    print("Первое множество: ")
    output(set1)
    print("Второе множество: ")
    output(set2)


    #ADD_EL()
    print("Добавляем элементы в первое множество: ")
    set1 = add_el(set1)
    print("Добавляем элементы во второе множество: ")
    set2=add_el(set2)


    #DEL_EL()
    print("Удаляем из первого множества: ")
    set1 = del_el(set1)
    print("Удаляем из второго множества: ")
    set2 = del_el(set2)


    #OUTPUT()
    print("Изменённое первое множество: ")
    output(set1)
    print("Изменённое второе множество: ")
    output(set2)
    answ_func()




        
        
    


        
