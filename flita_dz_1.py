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
        add_el = input("Enter the adding element: ")
        if add_el == '':
            return set_arg
        else:
            set_arg.add(add_el)
        
#deleting of a element of set


def del_el(set_arg):        
    del_el=1
    while del_el != '':
        del_el=input("Enter the deleting element: ")
        if del_el in set_arg:
            set_arg.discard(del_el)
        elif not (del_el in set_arg) and del_el != '':
            print("Ivalid input! There is no such element in th set! Try again!")
    else:
        return set_arg
    
    
        
# recursive FUCTION
def answ_func():
        global answ   
        answ = input("Do you want to continue: ")
        if answ == 'No' or answ == 'no':
            answ = False
        elif answ == 'Yes' or answ == 'yes':
            answ = True
        else: 
            print("Incorrect input repeat again!")
            answ_func()



        
answ = True
while answ:    
    #CREATE() 
    print(" Entering of first set. ")
    set1 = create(set1)
    print("Enterof second set.")
    set2 = create(set2)
    #OUTPUT()
    print("First set: ")
    output(set1)
    print("Second set: ")
    output(set2)


    #ADD_EL()
    print("Adding elements to set1: ")
    set1 = add_el(set1)
    print("Adding elements to set2: ")
    set2=add_el(set2)


    #DEL_EL()
    print("Deleting elements from set1: ")
    set1 = del_el(set1)
    print("Deleting elements from set2:")
    set2 = del_el(set2)


    #OUTPUT()
    print("Modified first set: ")
    output(set1)
    print("Modified second set: ")
    output(set2)
    answ_func()




        
        
    


        
