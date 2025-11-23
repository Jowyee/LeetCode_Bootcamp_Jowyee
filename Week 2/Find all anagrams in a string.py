def findAnagrams(s: str, p: str) -> list[int]:
    len_s, len_p = len(s), len(p)
    if len_s < len_p:
        return []
    
    p_count = [0] * 26
    s_count = [0] * 26
    
    for i in range(len_p):
        p_count[ord(p[i]) - ord('a')] += 1
        s_count[ord(s[i]) - ord('a')] += 1
    
    result = []
    if p_count == s_count:
        result.append(0)
    
    for i in range(len_p, len_s):
        left_char = s[i - len_p]
        s_count[ord(left_char) - ord('a')] -= 1
        right_char = s[i]
        s_count[ord(right_char) - ord('a')] += 1
        if p_count == s_count:
            result.append(i - len_p + 1)
    
    return result