s = "program"

''' Print given word in a x shaped pattern.
    It's just spaces. play around until you find the perfect spacing.
    space-word-space-word '''

def print_x(s):
    l = len(s)
    for i in range(l - 1):
        if s[i] == s[-i - 1]:
            print(f'{" " * i}{s[i]}')
            continue
        while i <= l // 2:
            print(f'{" " * i}{s[i]}{" "*(l - 2 * i - 2)}{s[-1-i]}')
            break
        while i > l // 2:
            print(f'{" "* (l - i - 1)}{s[-i-1]}{" "*((2 * i)-l)}{s[i]}')
            break

print_x(s)
