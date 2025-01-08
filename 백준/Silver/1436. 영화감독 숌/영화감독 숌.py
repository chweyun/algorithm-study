n = int(input())
count = 0
result = 666

while True:
    if '666' in str(result):
        count += 1

    if count == n:
        print(result)
        break

    result += 1