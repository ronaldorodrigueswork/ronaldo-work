def Adição(x, y):
    return x + y

def Subtração(x, y):
    return x - y

def Multiplicação(x, y):
    return x * y

def Divisão(x, y):
    return "Erro." if y == 0 else x / y 

print('''
1 - Adição (+)
2 - Subtração (-)
3 - Multiplicação (*)
4 - Divisão (/)
''')

print("Digiti um número: ")
o = int(input(""))

if o in [1, 2, 3, 4]:
    print("número¹:")
    x = int(input(""))
    print("número²:")
    y = int(input(""))

    if o == 1:
        print(f"resuldato:\n{Adição(x, y)}")
    elif o == 2:
        print(f"resuldato:\n{Subtração(x, y)}")
    elif o == 3:
        print(f"resuldato:\n{Multiplicação(x, y)}")
    elif o == 4:
        print(f"resuldato:\n{Divisão(x, y)}")
