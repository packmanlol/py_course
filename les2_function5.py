#3. Написать функцию is_prime, принимающую 1 аргумент — число от 0 до 1000,
# и возвращающую True, если оно простое, и False - иначе.

def is_prime (x):
    for i in range(2, x-1):
        if x % i == 0:
            print("Составное")
            break
    else:
        print("Простое")

is_prime(462)