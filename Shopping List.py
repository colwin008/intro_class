shopping_list = ['apple', 'pear', 'orango']

def sort():
    shopping_list.sort()

def add(item1):
    global shopping_list
    item1 = item1.lower()
    if item1 in shopping_list:
    #     shopping_list.remove(item1)
        print item1, "is already in the list."
    else:
        shopping_list = shopping_list + [item1]
    # shopping_list.upper('apple')
    # shopping_list.lower()


def remove(item1):
    if item1 not in shopping_list:
        print item1, "this item is not in the list"
    else:
        shopping_list.remove(item1)


def main():

    # add('pink', 'red', 'yellow', 'blue')

    item1 = raw_input("What do you like to add to the shopping list?")
    # add(item1)
    add('pink')
    add('orange')
    add('blue')
    add('yellow')
    add('apple')
    remove('blue')
    remove('sdlkfs;d')
    print shopping_list



if __name__=='__main__':
    main()
