import sys
input = sys.stdin.readline

while True:
    result = True
    vowel = {'a':0, 'e':0, 'i':0, 'o':0, 'u':0}
    pw = input().strip()
    stack = []
    
    if pw == 'end':
        break

    for i in pw:
        if len(stack) != 0:
            last = stack[-1]
            if i not in ['e', 'o'] and last == i:
                result = False
                break

            if len(stack) > 1:
                a, b = stack[-2], stack[-1]
                if a in vowel and b in vowel and i in vowel:
                    result = False
                    break
                if a not in vowel and b not in vowel and i not in vowel:
                    result = False
                    break

        if i in vowel:
            vowel[i] = vowel[i]+1
        stack.append(i)

    total = sum(vowel.values())
    if total == 0:
        result = False

    print(f'<{pw}> is acceptable.') if result else print(f'<{pw}> is not acceptable.')
