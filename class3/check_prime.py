def check_prime(parameter):
    i = 2
    while i < parameter:
        if (parameter % i) == 0:
            print("Not a Prime Number")
            break

        i = i + 1

check_prime(12)
