pi = 3.141592653589793

def f1(a1,b1,a2,b2,h):
    return (pi*h/12)*((a1*b1)+(a2*b2)+((a1*a2*b1*b2)**(0.5)))

def f2(a1,b1,a2,b2,h):
    return (pi*h/12)*((a1*b1)+(a2*b2/2)+((a1*a2*b1*b2/2)**(0.5)))

def f3(a1,b1,a2,b2,h):
    return (pi*h/12)*((a1*b1)+(a2*b2/3)+((a1*a2*b1*b2/3)**(0.5)))

def volume(ls,h):
 v = 0
 for i in range(1,len(ls)):
    a1 = ls[i-1][0]
    b1 = ls[i-1][1]
    a2 = ls[i][0]
    b2 = ls[i][1]

    a1l = a1[len(a1) - 1]
    b1l = b1[len(b1) - 1]
    a2l = a2[len(a2)-1]
    b2l = b2[len(b2)-1]

    if a1l == 'x' and b1l == 'x' and a2l != 'x' and b2l != 'x' and a2l != 't' and b2l != 't':
        a1 = float(a1.replace('x',''))
        b1 = float(b1.replace('x',''))
        v += f2(float(a1), float(b1), float(a2), float(b2),h)
    elif a2l == 'x' and b2l == 'x' and a1l != 'x' and b1l != 'x' and a1l != 't' and b1l != 't':
        a2 = float(a2.replace('x',''))
        b2 = float(b2.replace('x',''))
        v += f2(float(a1), float(b1), float(a2), float(b2),h)
    elif a2l == 'x' and b2l == 'x' and a1l == 'x' and b1l == 'x':
        a1 = float(a1.replace('x', ''))
        b1 = float(b1.replace('x', ''))
        a2 = float(a2.replace('x', ''))
        b2 = float(b2.replace('x', ''))
        v += f1(float(a1), float(b1), float(a2), float(b2),h)
    elif a1l == 't' and b1l == 't' and a2l != 'x' and b2l != 'x' and a2l != 't' and b2l != 't':
        a1 = float(a1.replace('t',''))
        b1 = float(b1.replace('t',''))
        v += f3(float(a1), float(b1), float(a2), float(b2),h)
    elif a2l == 't' and b2l == 't' and a1l != 'x' and b1l != 'x' and a1l != 't' and b1l != 't':
        a2 = float(a2.replace('t',''))
        b2 = float(b2.replace('t',''))
        v += f3(float(a1), float(b1), float(a2), float(b2),h)
    elif a2l == 't' and b2l == 't' and a1l == 't' and b1l == 't':
        a1 = float(a1.replace('t', ''))
        b1 = float(b1.replace('t', ''))
        a2 = float(a2.replace('t', ''))
        b2 = float(b2.replace('t', ''))
        v += f1(float(a1), float(b1), float(a2), float(b2),h)
    else:
        v += f1(float(a1), float(b1), float(a2), float(b2),h)
 return v


ls1 = [('0.5', '0.5'),('0.5','0.7'),('0.9', '0.7'),('1.3t','5.0t'),('5.3t','2.5t')]
ls2 = [('0.5', '0.3'),('0.5','0.6'),('0.7', '0.8'),('1.3t','5.0t')]
ls3 = [('0.3', '0.8'),('0.9','0.8'),('1.0', '1.0'),('1.3t','5.0t')]

h1 = 12.8/len(ls1)
h2 = 11.5/len(ls1)
h3 = 14.8/len(ls1)

print(volume(ls1,h1)+volume(ls2,h2)+volume(ls3,h3))


