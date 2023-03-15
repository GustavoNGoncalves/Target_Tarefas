def fibo(r):
    if r == 0:
        return 0
    elif r == 1:
        return 1
    else:
        return fibo(r-1) + fibo(r-2)

def pert_fibonacci(num):
    i = 0
    while fibo(i) <= num:
        if fibo(i) == num:
            return True
        i += 1
    return False

def main():
    num = int(input("Digite um número inteiro: "))
    if pert_fibonacci(num):
        print(f"O número {num} pertence à sequência de Fibonacci.")
    else:
        print(f"O número {num} não pertence à sequência de Fibonacci.")

main()
