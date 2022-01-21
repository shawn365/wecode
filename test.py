def even(num):
    answer = []
    for i in range(1, num + 1):
        if i % 2 == 0:
            answer.append(i)
    return answer

print(even(50))
