def inc_unless_five(arg):
    if len(arg)==5:
        return arg
    else:
        arg.append(1)
        return arg

x = [42]
old_x = -99
print "before entering", old_x, x
while not (old_x == x):
    old_x = x
    print "after backup", old_x, x
    x = inc_unless_five(x)
    print "after first inc", old_x, x
    x = inc_unless_five(x)
    print "after second inc", old_x, x
