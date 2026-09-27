#Entrada de dados

N1 = float(input("Digite o primeiro número: "))
N2 = float(input("Digite o segundo número: "))
N3 = float(input("Digite o terceiro número: "))
N4 = float(input("Digite o quarto número: "))

dados = [N1, N2, N3, N4]

#Exibir opcções para o usuário escolher
print("Escolha a operação que deseja realizar:")
print("1 - Média")
print("2 - Moda")
print("3 - Mediana")

#Receber a escolha do usuário
opcao = input("Digite o número da operação desejada:")
print("Você escolheu a opção:", opcao)

#Realizar a operação escolhida

if opcao == "1":
    #Soma dos numeros e dividir pela quantidade
    media = (N1 + N2 + N3 + N4) / 4
    print("A média dos números é:", media)

elif opcao == "2":
    #Verificar se os numeros são todos diferentes
    if len(set(dados)) == len(dados):
        print("Não há moda, todos os números são diferentes.")
    else:
        import statistics
        #Moda dos números
        moda = statistics.mode(dados)
        print("A moda dos números é:", moda)
elif opcao == "3":
    import statistics
    #Mediana dos números
    mediana = statistics.median(dados)
    print("A mediana dos números é:", mediana)

else:
    print("Opção inválida. Por favor, escolha uma opção válida.")
