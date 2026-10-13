import sys

def main():
    input = sys.stdin.buffer.readline

    n = int(input())
    a = list(map(int, input().split()))
    count = 0

    for i in range(n - 2, -1, -1):
        if a[i] > a[i + 1]:
            a[i] = a[i + 1]
            count += 1

    print(count)
    print(*a)

if __name__ == "__main__":
    main()
