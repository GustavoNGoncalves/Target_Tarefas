def inverte_string(string):
    nova_string = ""
    for i in range(len(string)-1, -1, -1):
        nova_string += string[i]
    return nova_string

def main():
    string = input("Digite uma string: ")
    nova_string = inverte_string(string)
    print(f"A string invertida é: {nova_string}")

main()
