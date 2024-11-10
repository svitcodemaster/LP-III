'''
NAME: UGALE GANESH DHONDIRAM
CLASS: BE (COMP)
ROLL NO: 35
SUB: DAA
EXPERIMENT NO: MINI- PROJECT
'''

import time

# Naive String Matching Algorithm
def naive_string_matching(text, pattern):
    m = len(pattern)
    n = len(text)
    matches = []
    for i in range(n - m + 1):
        if text[i:i + m] == pattern:
            matches.append(i)
    return matches

# Rabin-Karp Algorithm
def rabin_karp(text, pattern, d=256, q=101):
    m = len(pattern)
    n = len(text)
    p = 0  # hash value for pattern
    t = 0  # hash value for text
    h = 1
    matches = []

    # The value of h would be "pow(d, m-1)%q"
    for i in range(m - 1):
        h = (h * d) % q

    # Calculate the hash value of pattern and first window of text
    for i in range(m):
        p = (d * p + ord(pattern[i])) % q
        t = (d * t + ord(text[i])) % q

    # Slide the pattern over text one by one
    for i in range(n - m + 1):
        # Check the hash values of the current window of text and pattern.
        if p == t:
            # Check for characters one by one
            if text[i:i + m] == pattern:
                matches.append(i)

        # Calculate hash value for next window of text: Remove leading digit,
        # add trailing digit
        if i < n - m:
            t = (d * (t - ord(text[i]) * h) + ord(text[i + m])) % q
            # We might get negative value of t, converting it to positive
            if t < 0:
                t += q

    return matches

# Main
if __name__ == "__main__":
    text = "ABABDABACDABABCABAB"
    pattern = "ABAB"
    
    # Naive String Matching
    start_time = time.time()
    naive_matches = naive_string_matching(text, pattern)
    print("Naive String Matching Matches at indices:", naive_matches)
    print("\n")
    print("Time taken by Naive String Matching: %s seconds" % (time.time() - start_time))
    print("\n")
    # Rabin-Karp Algorithm
    start_time = time.time()
    rabin_karp_matches = rabin_karp(text, pattern)
    print("Rabin-Karp Matches at indices:", rabin_karp_matches)
    print("\n")
    print("Time taken by Rabin-Karp Algorithm: %s seconds" % (time.time() - start_time))
    print("\n")
    

'''
OUTPUT:
Naive String Matching Matches at indices: [0, 10, 15]


Time taken by Naive String Matching: 0.0 seconds


Rabin-Karp Matches at indices: [0, 10, 15]


Time taken by Rabin-Karp Algorithm: 0.0 seconds
'''