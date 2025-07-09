# Print only prime numbers from a list

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

count = int(input())
nums = list(map(int, input().split()))

for num in nums:
    if is_prime(num):
        print(num, end=" ")


print(is_prime(5))