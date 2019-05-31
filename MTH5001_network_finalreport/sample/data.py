def data_linear(id):
    import random
    random.seed(id)
    n = random.randint(50,100)
    a0 = random.randint(-10,10)
    a1 = random.randint(1,20)
    eps = 0.05*a1
    x = [random.random() for i in range(n)]
    return [[x[i], a0 + a1*x[i] + random.gauss(0,eps)] for i in range(n)]

def data_quadratic(id):
    import random
    random.seed(id)
    random.random() #ensure different n
    n = random.randint(50,100)
    a0 = random.randint(-10,10)
    a1 = random.randint(-10,10)
    a2 = random.randint(-10,10)
    eps = 0.2*a2
    x = [random.uniform(-1,2) for i in range(n)]
    return [[x[i], a0 + a1*x[i] + a2*x[i]**2 + random.gauss(0,eps)] for i in range(n)]

def data_polynomial(id):
    import random
    random.seed(id)
    random.random() #ensure different n
    random.random() #ensure different n
    n = random.randint(100,200)
    m = 1+random.randint(2,4)
    a=[]
    for i in range(m):
        a.append(random.randint(-10,10))
    a.append(random.randint(2,5))
    eps = 2.0*a[m]
    x = [random.uniform(-3,3) for i in range(n)]
    return [[x[i], sum([a[j]*x[i]**j for j in range(m+1)]) + random.gauss(0,eps)] for i in range(n)]