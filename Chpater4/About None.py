thing = None
if thing:
    print("There's something")
else:
    print("Empty")

#區分None與False
if thing is None:
    print("It's nothing")
else:
    print("It's something")

def is_none(thing):
    if thing is None:
        print("It's None")
    elif thing:
        print("It's True")
    else:
        print("It's False")
is_none(None)
is_none(True)
is_none(False)
is_none(11)  
is_none("")
is_none(0)
is_none([])