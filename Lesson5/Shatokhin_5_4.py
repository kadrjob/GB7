src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
# result = [12, 44, 4, 10, 78, 123]

tmp_result = (src[idx] for idx in range(1, len(src)) if src[idx] > src[idx - 1])

print(list(tmp_result))
