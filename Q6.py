# Sort odd positions in descending, even positions in ascending

def sort_odd_even(arr):
    odd_indices = arr[::2]
    even_indices = arr[1::2]

    odd_sorted = sorted(odd_indices, reverse=True)
    even_sorted = sorted(even_indices)

    result = []
    for i in range(len(arr)):
        if i % 2 == 0:
            result.append(odd_sorted[i // 2])
        else:
            result.append(even_sorted[i // 2])
    return result

# Sample test
arr = [13, 2, 4, 15, 12, 10, 5]
print(sort_odd_even(arr))