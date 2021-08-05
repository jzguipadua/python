from decimal import Decimal as dec
print('Fibonacci calculator. \n')

pos = int(input("Insert a integer scale position.\n "))


def fib(a):

    val1 = 1
    val2 = 1

    for i in range(a-2):

        val3 = val1 + val2
        val1 = val2
        val2 = val3
        if i == a:

            break
    return print(f'Fibo {a}ª: ', dec(val3))


fib(pos)
