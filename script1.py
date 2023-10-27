# Python program to print all prime numbers in an interval

if __name__ == '__main__':
    x = input("\nEnter start of range: ")
    y = input("\nEnter end of range: ")

    x = int(x)
    y = int(y)

    prime_list = []

    for i in range(x, y):
        if i == 0 or i == 1:
            continue
        else:
            for j in range(2, int(i/2)+1):
                if i % j == 0:
                    break
            else:
                prime_list.append(i)

    if len(prime_list) == 0:
        print("\nThere are no prime numbers in this range")
    else:
        print("\nThe prime numbers in this range are: ", prime_list)
        