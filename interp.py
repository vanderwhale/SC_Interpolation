A = matrix(RR,11,11)
for row_num in range(0,11):
    for col_num in range(0,11):
        entry = row_num*(0.2)-1
        print(row_num,'coulmn', col_num,'entry', entry**col_num)
        A[row_num, col_num] = n(entry**col_num)

def f(x):
    return(1/(1+25*x**2))

v = vector(RR,11)
for row_num in range(0,11):
    entry = row_num*(0.2)-1
    v[row_num] = f(entry)

w=A\v

def p(x):
    return(w[0]
        +w[1]*x
        +w[2]*x**2
        +w[3]*x**3
        +w[4]*x**4
        +w[5]*x**5
        +w[6]*x**6
        +w[7]*x**7
        +w[8]*x**8
        +w[9]*x**9
        +w[10]*x**(10))

pl1=plot(f,(-1,1))
pl2=plot(p,(-1,1),color='red')

pl1+pl2

test
