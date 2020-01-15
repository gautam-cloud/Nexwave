"""
This is a program for the assignment 1, where we have to perform
various operations on list.
This is the functional implementaion of the assignment.
>>> l=[10,20,30]
>>> dev_id_search(50,l)
'Dev ID Found, Dev ID = 20Index =1'
>>> dev_id_search(20)
Traceback (most recent call last):
  File "<input>", line 1, in <module>
TypeError: dev_id_search() missing 1 required positional argument: 'dev_list'
"""
def dev_id_search(dev_id, dev_list):
    if dev_id in dev_list:
        return 'Dev ID Found, Dev ID = ' + str(dev_id) + 'Index =' + str(dev_list.index(dev_id))
    elif dev_id > max(dev_list):
        return 'Not Found'
    else:
        for i in dev_list:
            if i > dev_id:
                return 'val =' + str(i) + 'index = ' + str(dev_list.index(i))


def main():
    L1 = [1, 3, 5, 16, 8]
    L2 = [6, 5, 9, 4, 13, 12]
    L3 = list(set(L1 + L2))
    L3.sort()
    while True:
        i = input('Enter Device Id to search')
        i = eval(i)
        r = dev_id_search(i, L3)
        print(r)
        ch = input('Do you want to quit (Y/N)?');
        if ch == 'y':
            break


if __name__ == '__main__':
    main()
    import doctest
    doctest.testmod()