for n in range(1000):
    m = bin(n)[2:]
    if n % 3 == 0:
        m += m[-3::]
    else:
        m += str(bin(3 * (n % 3))[2:4])
    if int(m, 2) >= 200:
        print(int(m, 2))
        print(n)
        break
