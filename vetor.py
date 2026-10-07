estojo = []
print('oi,voce quer coloca algo no estojo')
objeto =""
while objeto != 0:
    objeto = int(input('deseja colocar um objeto(1 pra sim e 0 pra não): '))
    if objeto ==1:
        item = input("digite qual o item que voce quer coloca: ")
        estojo.append(item)
        for item in estojo:
            print(item)
    else:
        print("pronto,aqui estão seus item")
        for item in estojo:
            print(item)