def somar (a, b):
 return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Erro! Divisão por zero."
    return a / b

def sair():
    print("Saindo da calculadora...")
    exit()

def menu():
    while True:
        print("\nCalculadora - Escolha uma opção:")
        print("1️ Somar")
        print("2️ Subtrair")
        print("3️ Multiplicar")
        print("4️ Dividir")
        print("5️ Sair")

        opcao = input("Digite o número da opção desejada: ")

        if opcao == "5":
            calculadora.sair()

        if opcao in ["1", "2", "3", "4"]:
            a = float(input("Digite o primeiro número: "))
            b = float(input("Digite o segundo número: "))

            if opcao == "1":
                print(f"Resultado: {calculadora.somar(a, b)}")
            elif opcao == "2":
                print(f"Resultado: {calculadora.subtrair(a, b)}")
            elif opcao == "3":
                print(f"Resultado: {calculadora.multiplicar(a, b)}")
            elif opcao == "4":
                print(f"Resultado: {calculadora.dividir(a, b)}")
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
