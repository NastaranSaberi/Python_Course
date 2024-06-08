def rug(size):

    pattern = ["🔴", "🟠", "🟡", "🟢", "🔵", "🟣", "⚪️", "🟤", "⚫️"]
    half_size = size // 2
    rug = [["" for _ in range(size)] for _ in range(size)]

    for i in range(half_size + 1):
        for j in range(i, size - i):
            rug[i][j] = pattern[i % 9]
            rug[size - 1 - i][j] = pattern[i % 9]
            rug[j][i] = pattern[i % 9]
            rug[j][size - 1 - i] = pattern[i % 9]

    for row in rug:
        print(" ".join(row))


while True :
    n = int(input("Please enter an odd number to make the rug :"))
    if n % 2 != 0 :
        rug(n)
        break
    else :
        print("Please enter an odd number.")