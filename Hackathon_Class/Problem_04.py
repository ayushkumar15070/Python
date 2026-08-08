s = '1231'
k = 3
n = len(s)

def highest_value_palindrome(s: str, k: int) -> str:
    s_list = list(s)
    n = len(s)
    changed = [False] * n

    # First pass: make palindrome with minimal changes
    for i in range(n // 2):
        j = n - 1 - i
        if s_list[i] != s_list[j]:
            if s_list[i] > s_list[j]:
                s_list[j] = s_list[i]
            else:
                s_list[i] = s_list[j]
            changed[i] = True
            k -= 1

    if k < 0:
        return "-1"

    # Second pass: maximize digits to 9
    for i in range(n // 2):
        if k <= 0:
            break
        j = n - 1 - i
        if s_list[i] != '9':
            cost = 1 if changed[i] else 2
            if k >= cost:
                s_list[i] = '9'
                s_list[j] = '9'
                k -= cost

    # If there is a middle digit in odd-length string
    if n % 2 == 1 and k > 0:
        s_list[n // 2] = '9'

    return "".join(s_list)

result = highest_value_palindrome(s, k)
print(result)
