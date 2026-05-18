def tabuada(a):
    for i in range(1, 11):
        print(f'{a} × {i} = {a * i}') 

tab = int(input("Select a number to see its multiplication table from 1 to 10: "))
print(tabuada(tab))