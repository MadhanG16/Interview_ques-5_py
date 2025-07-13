n = int(input("Enter the Range: "))

for i in range(n):
    if i <= n // 2:
        b_count = n // 2 - i
    else:
        b_count = i - n // 2
    star_count = n - 2 * b_count
    print('b'* b_count +'*' * star_count + 'b' * b_count)