import math
u = []
s = []
operatororder = ['d', '=', '^', '/', '*', '+', '-']
order = {k: i for i,k in enumerate(operatororder)}

def popcommand(s):
    #function to pop the last 2 elements from the stack and return them
    b = s.pop()
    a = s.pop()
    return a,b

def check(m):
    #function to check if value is in the range of signed 32-bit integer
    if m>2147483647:
        m=2147483647
    if m<-2147483648:
        m=-2147483648
    return m

def operator(n):
    if n=="+":
        if len(s)>=2:
            a,b = popcommand(s)
            m = a+b
            s.append(check(m))
        else:
            print("Stack underflow.")
    if n=="-":
        if len(s)>=2:
            a,b = popcommand(s)
            m = a-b
            s.append(check(m))
        else:
            print("Stack underflow.")
    if n=="*":
        if len(s)>=2:
            a,b = popcommand(s)
            m = a*b
            s.append(check(m))
        else:
            print("Stack underflow.")
    if n=="/":
        if len(s)>=2:
            a,b = popcommand(s)
            if b!=0:
                m = a//b
                s.append(check(m))
            else:
                print("Divide by 0.")
        else:
            print("Stack underflow.")
    if n=="%":
        if len(s)>=2:
            a,b = popcommand(s)
            m = a%b
            s.append(check(m))
        else:
            print("Stack underflow.")
    if n=="^":
        if len(s)>=2:
            a,b = popcommand(s)
            if b>0:
                m = int(math.pow(a,b))
                s.append(check(m))
            else:
                print("Negative power.")
                s.append(a)
                s.append(b)
        else:
            print("Stack underflow.")
    if n=="=":
        try:
            print(s[-1])
        except IndexError:
            print("Stack empty.")         
    if n=="d":
        if len(s)>0:
            for i in s:
                print(i)
        else:
            print(-2147483648)

def main():
    while True:
        try:
            u = input().split()
            if u.count("#")%2==0:
                flag=0
                for j in u:
                    if j=="#":
                        flag+=1
                    if flag%2==0:
                        try:
                            j = int(j)
                            if len(s)<23:
                                s.append(check(j))
                            else:
                                print("Stack overflow.")
                        except ValueError:
                            if len(j)>1:
                                z=[]
                                for i in j:
                                    z.append(i)
                                y=[]
                                for i in z:
                                    try:
                                        y.append(order[i])
                                    except KeyError:
                                        y.append(int(i))          
                                y.sort()
                                for i in y:
                                    x=list(order.keys())
                                    y[y.index(i)] = x[list(order.values()).index(i)]
                                p=[]
                                for i in y:
                                    p.append(i)
                                for i in p:
                                    operator(i)
                            else:
                                operator(j)
        except EOFError:
            break

main()
