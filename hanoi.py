def main():
    hanoi(15, 1, 2)

def hanoi(n, i, k):
    if n == 1:
        print(f"Move disk {n} from pin {i} to {k}")
    else:
        tmp = 6 - i - k
        hanoi(n - 1, i, tmp)
        print(f"Move disk {n} from pin {i} to {k}")
        hanoi(n - 1, tmp, k)
main()