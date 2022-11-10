                                                
                                                # LIST  EDITOR
                                                
                                                
arr = [10, 2, 1, "c", 7, 4, "b", 1, "a"]
login_password = ['admin', '12345']
print(
    f"\nProgram is start...\nWrite <end> or <exit> for stop programm\nWrite <back> to return to the main menu\n")
lst = arr[::]
new_lst = list()
copy_list = list()


while True: 
    q = input("Please take mode: guest | admin\n")
    if q.lower() == 'guest':
        if len(lst) == 0:
            if len(new_lst) > 0:
                if len(copy_list) > 0:
                    print(f"\nThe start list is empty {lst}")
                    print(f"New list - {new_lst}")
                    print(f"Copy list -  {copy_list}")
                else:
                    print(f"\nThe start list is empty <<<<{lst}")
                    print(f"New list - <<<<{new_lst}\n")
            elif len(copy_list) > 0:
                if len(new_lst) > 0:
                    print(f"\nThe start list is empty {lst}")
                    print(f"Copy list -  {copy_list}")
                    print(f"New list - {new_lst}")
                else:
                    print(f"\nThe start list is empty <<<<{lst}")
                    print(f"Copy list - <<<<{copy_list}\n")
            else:
                print(f"\nThe start list is empty {lst}\n")
        elif len(lst) > 0:
            if len(new_lst) > 0:
                if len(copy_list) > 0:   
                    print(f"\nThe start list - {lst}")
                    print(f"New list - {new_lst}")
                    print(f"Copy list - {copy_list}\n")
                else:    
                    print(f"\nThe start list - {lst}")
                    print(f"New list - {new_lst}\n")
            elif len(copy_list) > 0:
                if len(new_lst) > 0:
                    print(f"\nThe start list - {lst}")
                    print(f"New list - {new_lst}")
                    print(f"Copy list - {copy_list}\n")
                else:
                    print(f"\nThe start list - {lst}")
                    print(f"Copy list - {copy_list}\n")
            else:                                    
                print(f"\nyour list - {lst}\n")

    elif q.lower() == 'admin':
        while q:
            if q == False:
                break
            else: 
                user_login_password = input("Please enter login: ").split() + input("Please enter password: ").split()
                if login_password != user_login_password:
                    print(f"\nLogin or Password invalid!\nTry again\n")
                else:
                    print("\nLog In to admin panel successfully!\n")
                    q = False       
                    while True:
                        if len(lst) == 0: 
                            if len(new_lst) > 0:
                                if len(copy_list) > 0:
                                    print(f"\nThe start list is empty {lst}")
                                    print(f"New list - {new_lst}")
                                    print(f"Copy list -  {copy_list}")
                                else:
                                    print(f"\nThe start list is empty <<<<{lst}")
                                    print(f"New list - <<<<{new_lst}\n")
                            elif len(copy_list) > 0:
                                if len(new_lst) > 0:
                                    print(f"\nThe start list is empty {lst}")
                                    print(f"Copy list -  {copy_list}")
                                    print(f"New list - {new_lst}")
                                else:
                                    print(f"\nThe start list is empty <<<<{lst}")
                                    print(f"Copy list - <<<<{copy_list}\n")
                            else:
                                print(f"\nThe start list is empty {lst}\n")
                        elif len(lst) > 0:
                            if len(new_lst) > 0:
                                if len(copy_list) > 0:   
                                    print(f"\nThe start list - {lst}")
                                    print(f"New list - {new_lst}")
                                    print(f"Copy list - {copy_list}\n")
                                else:    
                                    print(f"\nThe start list - {lst}")
                                    print(f"New list - {new_lst}\n")
                            elif len(copy_list) > 0:
                                if len(new_lst) > 0:
                                    print(f"\nThe start list - {lst}")
                                    print(f"New list - {new_lst}")
                                    print(f"Copy list - {copy_list}\n")
                                else:
                                    print(f"\nThe start list - {lst}")
                                    print(f"Copy list - {copy_list}\n")
                            else:                                    
                                print(f"\nyour list - {lst}\n")
                        menu = input("Please take operation from list:\nappend | extend | insert | remove | index | count | pop \
| sort | reverse | copy | clear:  |<< back \n")
                        user_variant = menu
                        if user_variant.lower() == "append":
                            while True:
                                print(lst)
                                type_element = input("What type do you want to add from list: string or number? | back\n")
                                if type_element == "string":
                                    element = input("Please write string item here: \n")
                                    if element in lst:
                                        print("This item already exist in the list\n")
                                        q = input("Do you want add this item in the list: yes or not ? | back\n")
                                        if q.lower() == 'yes':
                                            lst.append(element)
                                    lst.append(element)   
                                elif type_element == "number":
                                    try:            
                                        element = input("Please write integer item here: \n")
                                        element = int(element)
                                        
                                        if element in lst:
                                            print("This item already exist in the list\n")
                                            q = input(
                                                "Do you want add this item in the list: yes or not ? | back\n")
                                            
                                            if q.lower() == 'yes':
                                                lst.append(int(element))
                                        else:                        
                                            lst.append(int(element))
                                                            
                                    except ValueError:
                                        print(f"<{element}> is not integer item\n")      
                                elif type_element.lower() == "back":
                                    break         
                                else:
                                    print("Please take valid type to add from list: string or number\n") 
                                    
                        elif user_variant.lower() == "extend":
                            while True:
                                print(lst)
                                type_element = input("What items type do you want to add from list: string or number? | back\n")            
                                if type_element.lower() == "string":
                                    element = input("Enter string items using <space> here: ").split()
                                    for i in element:
                                        if i in lst:
                                            print(lst)
                                            print(f"\n<{i}> already exist in your list\n")
                                            q = input("Do you want add this item in the list: yes or not ? | back\n")
                                            if q.lower() == 'yes':
                                                lst.append(i)
                                            if q.lower() == 'not':
                                                continue
                                            elif q.lower() == 'back':
                                                break
                                            else:
                                                print(f"\nOops! I don't understand you <{q}>\nTry again please\n")
                                        else:
                                            lst.append(i)
                                
                                elif type_element.lower() == 'number':
                                    element = input("Enter string items using <space> here: ").split()
                                    print(element)
                                    for i in element:
                                        if not i.isdigit(): 
                                            print(
                                                f"<{i}> is not integer item\n")
                                        elif i.isdigit():
                                            if int(i) in lst:
                                                print(lst)
                                                print(f"\n<{i}> already exist in your list\n")
                                                q = input("Do you want add this item in the list: yes or not ? | back\n")
                                                if q.lower() == 'yes':
                                                    lst.append(int(i))
                                                if q.lower() == 'not':
                                                    continue
                                                elif q.lower() == 'back':
                                                    break
                                                else:
                                                    print(f"\nOops! I don't understand you <{q}>\nTry again please\n")
                                            else:
                                                lst.append(int(i))    
                                
                                elif type_element.lower() == 'back':
                                    break
                                else: print("Please take valid type to add from list: string or number\n")
                                        
                        elif user_variant.lower() == "insert":
                            while True:
                                print(lst)
                                type_element = input(
                                    "What type do you want to add from list: string or number? | back\n")
                                try:
                                    if type_element == "string":
                                        element = input("Please write string item here: \n")
                                        index = input("Write index number where nedeed paste this item in list: \n")
                                        if element in lst:
                                            print("This item already exist in the list\n")
                                            q = input("Do you want add this item in the list: yes or not ? | back\n")
                                            if q.lower() == 'yes':
                                                lst.insert(int(index), element)
                                        else:
                                            lst.insert(int(index), element)

                                    elif type_element == "number":
                                        try:       
                                            element = input("Please write number item here: \n")
                                            index = input("Write index number where nedeed paste this item in list now: \n")
                                            if int(element) in lst:
                                                print("This item already exist in the list\n")
                                                q = input(
                                                    "Do you want add this item in the list: yes or not ? | back\n")
                                                if q.lower() == 'yes':
                                                    lst.insert(int(index), int(element))
                                            else:        
                                                lst.insert(int(index), int(element))
                                        except ValueError:
                                            if not element.isdigit():
                                                if not index.isdigit():
                                                    print(
                                                        f"<{element}> and <{index}> is not number items\nTry again please\n")
                                                    continue
                                                print(
                                                    f"<{element}> is not number element\nTry again please\n")
                                            elif not index.isdigit():
                                                print(
                                                    f"<{index}> is not number index\nTry again please\n")                                                            
                                            else:
                                                print("Please take valid type to add from list: string or number\n")
                                    elif type_element.lower() == "back":
                                        break            
                                except IndexError:
                                    print(f"Please enter valid number index: ")         

                        elif user_variant.lower() == "remove":
                            while True:
                                print(lst)
                                remove_item = input("Which item do you want to remove from the list? | back\n")
                                if remove_item.lower() == "back":
                                    break
                                try:
                                    if remove_item.isdigit():
                                        lst.remove(int(remove_item))
                                    else:
                                        lst.remove(remove_item)    
                                except ValueError:
                                        print(f"Oops! <{remove_item}> not in list\nTry again please\n")
                                                
                        elif user_variant.lower() == "index":
                            while True:
                                print(lst)
                                try:
                                    print(f"Lenght of the list equal {len(lst)} items")
                                    q = input(
                                        "You are want find index of string or number: string or number? | back\n")
                                    if q.lower() == "string":
                                        item = input("\nThe index of which string item do you want to know? | back\n")
                                        if item not in lst:
                                            print(f"Oops! <{item}> not in list\nPlease enter exist list 'string' item\n")
                                            continue
                                        for i, x in enumerate(lst):
                                            if x == item:
                                                print(f"<{x}> has index {i} in the list")
                                        
                                    elif q.lower() == "number":
                                        item = int(input("\nThe index of which number item do you want to know? | back\n"))
                                        if item not in lst:
                                            print(
                                                f"Oops! <{item}> is not in list\nPlease enter exist list integer item\n")
                                            continue
                                        for i, x in enumerate(lst):
                                            if x == item:
                                                print(f"<{x}> has index {i} in the list")
                                                continue               
                                    elif q.lower() == "back":
                                        break
                                except ValueError:
                                    print(f"<{q}> is not correctly\nTry again please")
                                    continue
                                        
                        elif user_variant.lower() == 'count':
                            while True:
                                print(lst)
                                type_element = input("What type element you want count: string or number? | back\n")
                                if type_element.lower() == 'string':
                                    str_item = input("Enter string item from counting: ")
                                    if str_item in lst:
                                        print(f"\nIn list {lst.count(str_item)} item == <{str_item}>\n")
                                    else:
                                        print(
                                            f"<{str_item}> not in list\nTry again please\n")
                                
                                elif type_element.lower() == 'number':
                                    try:
                                        num_item = int(input("Enter number item from counting: \n"))
                                        if num_item in lst:
                                            print(f"\nIn list {lst.count(num_item)} item == <{num_item}>\n")
                                        else:
                                            print(
                                                f"<{num_item}> not in list\nTry again please\n")        
                                    except ValueError:
                                        print(f"Not integer item\nPlease try again\n")
                                elif type_element.lower() == 'back':
                                    break
                                else:
                                    print(f"<{type_element}> is not correctly\nTry again please\n")
                        
                        elif user_variant.lower() == 'pop':
                            while True:
                                if len(new_lst) > 0:
                                    print(f"new list - {new_lst}")
                                print(lst)
                                try:
                                    index = input("Enter Index from get item in new list:  | back\n")
                                    if index == 'back':
                                        break    
                                    elif int(index) <= len(lst):
                                        new_lst.append(lst.pop(int(index)))
                                    else:print(f"\nItem with this Index <{index}> don't exist in the list\n")
                                except ValueError:
                                    print(f"Oops! Index <{index}> invalid\nPlease write integer Index...\n")
                                                    
                        elif user_variant.lower() == 'sort':
                            count = 0
                            while True:
                                if count > 0:
                                    print(f"\nsorted list {lst}\n")
                                else: print(lst)    
                                sort_lst_int = [i for i in lst if type(i) == int]
                                sort_lst_str = [i for i in lst if type(i) == str]
                                q = input("Start sort with max or min item: max or min? | back\n")
                                if q.lower() == 'max':
                                    sort_lst_int.sort(reverse=True)
                                    sort_lst_int.extend(sort_lst_str)
                                    lst = sort_lst_int
                                    count += 1
                                elif q.lower() == 'min':
                                    sort_lst_int.sort()
                                    sort_lst_int.extend(sort_lst_str)
                                    lst = sort_lst_int
                                    count += 1
                                elif q.lower() == 'back':
                                    break
                                else: 
                                    print(f"<{q}> not max or min\nPlease try again\n")
                                    
                        elif user_variant.lower() == "reverse":
                            while True:
                                q = input("Reverse you list: yes or not? | back\n")
                                if q.lower() == 'yes': 
                                    lst.reverse()
                                    print(f"list was reversed\n{lst}\n")
                                elif q.lower() == 'not':
                                    print(f"list wasn't reversed\n{lst}\n")
                                elif q.lower() == 'back':
                                    break                                 
                                else:
                                    print(f"Oops! I don't understand you <{q}>\nTry again please\n")
                                    
                        elif user_variant.lower() == 'copy':
                            while True:
                                if len(copy_list) > 0:
                                    print(f"\nnew copy list - {copy_list}")
                                    print(f"start list - {lst}")
                                else: print(lst)               
                                                    
                                q = input("\nCopy your list?: yes or not | back\n")           
                                if q.lower() == 'yes':
                                    copy_list = lst.copy()
                                    continue
                                elif q.lower() == 'not':
                                    continue
                                elif q.lower() == 'back':
                                    break
                                else:
                                    print(f"<{q}> is not correctly!\nTry again please")     
        
                        elif user_variant.lower() == 'clear':
                            while True:
                                q = input(f"Are you sure you want to delete the entire list: yes or not ? | back\n")
                                if q.lower() == 'yes':
                                    lst.clear()
                                    break
                                elif q.lower() == 'not': break
                                elif q.lower() == 'back': break
                                else: print(f"I don't understand you <{q}>!(\nTry again please\n") 
   
                        elif user_variant == '':
                            continue        
                        elif  user_variant.lower() == 'back':
                            q = False
                            break
                        else: print("\nOops! Please take valid operation from list\n")   
    elif q.lower() in ['end', 'back', 'exit']:
        print("\nThe program has finished work!\nGood day")
        break
    else:
        print(f"Oops! Please take valid mode from list\n")