

def calcular_x1_x2(a1,b1,c1):
    calc = b1 * b1
    calc1 = 4 * a1 * c1
    raiz1 = calc + calc1
    calc2 = b1 * -1
    calc3 = raiz1 ** 0.5
    calc4 = calc2 + calc3
    x1 = calc4 / 2
    return x1


a1 = int(input("Valor do a: "))

b1 = int(input("Valor do b: "))

c1 = int(input("Valor do c: "))

print(calcular_x1_x2(a1,b1,c1))
