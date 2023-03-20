produtos = {"Hamburgue": "5.00", "Xburgue": "7:00", "Pizza": "25.00",
            "Fanta": "3.50", "Coca-Cola": "3.50", "Refri": "2.50"}
x = int(input("\nDigite a opção desejada\n1-Hamburgue\n2-Xburgue\n3-Pizza M\n"))
if x == 1:
    x = float(produtos["Hamburgue"])
    print(f"\nvocê selecionou o Hamburgue\n ")
elif x == 2:
    x = float(produtos["Xburgue"])
    print(f"\nvocê selecionou o Xburgue\n")
elif x == 3:
    x = float(produtos["Pizza"])
    print(f"\nvocê selecionou a Pizza\n")
else:
    print("Opção Invalida")
y = int(input("\nDigite a opção de bebida :\n1-Fanta\n2-Coca-Cola\n3-Refri\n"))
if y == 1:
    y = float(produtos["Fanta"])
    print(f"\nvocê selecionou a Fanta\n")
elif y == 2:
    y = float(produtos["Coca-Cola"])
    print(f"\nvocê selecionou a Coca-Cola\n")
elif x == 3:
    y = float(produtos["Refri"])
    print(f"\nvocê selecionou o Refri\n")
else:
    print("Opção Invalida")
total = y+x

print(f"\nObrigado por sua compra o Total foi de: R${total}")
