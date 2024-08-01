from collections import Counter
def min_window(s, t):
    char_count = Counter(t)
    required_chars = len(char_count)
    formed_chars = 0
    left, right = 0, 0
    ans = float('inf')
    result = ""

    while right < len(s):
        char = s[right]
        char_count[char] -= 1
        if char_count[char] == 0:
            formed_chars += 1

        while formed_chars == required_chars:
            if right - left + 1 < ans:
                ans = right - left + 1
                result = s[left:right+1]

            char = s[left]
            char_count[char] += 1
            if char_count[char] > 0:
                formed_chars -= 1

            left += 1

        right += 1

    return result

# Example usage:
s = "ADOBECODEBANC"
t = "ABC"
result = min_window(s, t)
print(result)  # Output: "BANC"
