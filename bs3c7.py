n=raw_input()
try:
    int(n)
    print('yes')
except ValueError:
    print('not')
