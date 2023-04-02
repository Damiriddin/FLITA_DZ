#ЗАДАЁМ ДВА МНОЖЕСТВА
set1 = {}
set2 = {}

#ФУНКЦИЯ ЗАДАЮЩАЯ ЭЛЕМЕНТЫ МНОЖЕСТВА
def create(set_is_arg):
    size = int(input("Введите мошность множества size = "))
    set_is_arg = set(input("Введите элементы множества: ") for i in range(size))
    return set_is_arg


#ФУНКЦИЯ ДЛЯ ВЫВОДА МНОЖЕСТВА
def output(set_is_arg):
    print(set_is_arg)
    return None 
    
#ФУНКЦИЯ ДОБАВЛЕНИЯ ЭЛЕМЕНТА МНОЖЕСТВУ
def add_el(set_is_arg):
    add_size = int(input("Сколько элементов хотите добавить add_size = "))
    for i in range(add_size):
        add_el = input("Введите добавляемый элемент: ")
        set_is_arg.add(add_el)
    return set_is_arg


#ФУНКИЯ УДАЛЕНИЯ ЭЛЕМЕНТА МНОЖЕСТВА
def del_el(set_is_arg):
    am_del=int(input("Сколько элементов хотите удалить из множества: "))
    for i in range(am_del):
        del_el = input("Введите удаляемый элемент: ")
        set_is_arg.discard(del_el)
    return set_is_arg



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
    #РЕАЛИЗАЦИЯ ФУНКЦИИ CREATE() 
    print("Задаём первое множество")
    set1 = create(set1)
    print("Задаём второе множество")
    set2 = create(set2)
    #VIVOD()
    print("Первое множество: ")
    output(set1)
    print("Второе множество: ")
    output(set2)


    #РЕАЛИЗАЦИЯ ФУНКЦИИ ADD_EL()
    print("Добавляем элементы в первое множество: ")
    set1 = add_el(set1)
    print("Добавляем элементы во второе множество: ")
    set2=add_el(set2)


    #РЕАЛИЗАЦИЯ ФУНКЦИИ DEL_EL()
    print("Удаляем из первого множества: ")
    set1 = del_el(set1)
    print("Удаляем из второго множества: ")
    set2 = del_el(set2)


    #РЕАЛИЗАЦИЯ ФУНКЦИИ OUTPUT()
    print("Изменённое первое множество: ")
    output(set1)
    print("Изменённое второе множество: ")
    output(set2)
    answ_func()
    
                
            








