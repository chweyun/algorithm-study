alphas = input()
list_ = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
result = 0

for i in list_:
    if i in alphas:
        result += alphas.count(i)
        alphas = alphas.replace(i, ';')

alphas = alphas.replace(';', '')

print(result+len(alphas))
