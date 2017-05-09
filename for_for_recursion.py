def func(x, y, incx=True):
    if len(x) == 0:
        return
    elif len(y) == 0:
        return
    else:
        print('x:', x[0], 'y:',y[0])
    func(x, y[1:], False)
    if incx:
        func(x[1:], y, True)
    
print(func([1,2,3,4], [5,6,7,8,9]))