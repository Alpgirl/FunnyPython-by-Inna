alphabet = 'abcdefg'
result = [str(alphabet), alphabet[::-1], alphabet[::2], alphabet[1::2], alphabet[:1], alphabet[-1:-2:-1], alphabet[3:4],
          alphabet[-3::1], alphabet[3:5], alphabet[-3:-5:-1]]

print("Результаты работы программы:\n")
for i in range(1, len(result) + 1):
    print(i, ": ", result[i-1], sep="")