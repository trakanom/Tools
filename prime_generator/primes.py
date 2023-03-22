import time

# Prints all primes up to an integer input.
def primes_to_n(n):
    p = []
    for i in range(2, int(n)):
        if all(i % x for x in p):
            p += [i]
    return p


if __name__ == "__main__":
    n = int(input("Please enter a number: "))
    result = primes_to_n(n)
    print(f"There are {len(result)} prime numbers under {n}.")
    choices = input("Would you like to see them all? (y/n)")
    match choices.lower()[0]:
        case "y":
            print(*result, sep=", ")
            input("\nPress the enter key to exit.")
        case "n":
            input("\nPress the enter key to exit.")
        case _:
            print("Okay, bye!")
            time.sleep(1)
