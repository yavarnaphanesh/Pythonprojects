def count_sequences(lst):
    count = 0
    i = 0
    max_len = 0
    while i < len(lst):
        # Check if current element is the start of a sequence
        if i == 0 or lst[i] <= lst[i-1]:
            # Look for the end of the sequence
            j = i + 1
            seq_len = 1
            while j < len(lst) and lst[j] > lst[j-1]:
                j += 1
                seq_len += 1
            # Update count and max_len
            count += 1
            max_len = max(max_len, seq_len)
        i = j
    return count, max_len


n = [5, 15, 1, 11, 3, 13, 2, 12, 4, 14, 1]
N = sorted(n)
print(count_sequences(N))
