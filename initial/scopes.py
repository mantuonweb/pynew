def scope_test():
    def do_local():
        # changing the local variable
        spam = "local spam"

    def do_nonlocal():
        # changing the nearby block variable
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        # changing the global scope
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)


scope_test()
# spam is accessible outside the scope
print("In global scope:", spam)
