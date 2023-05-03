from collections import Counter

def longerIdx(t1, t2):
    a = abs(t1[0] - t1[1])
    b = abs(t2[0] - t2[1])
    if a > b:
        return t1
    else:
        return t2

def longest_substring(s: str):
    idx = 0
    sdx = 0
    char_idx = {}
    longest = [0, 0]
    current = [0, 0]

    while idx < len(s):    
        c = s[idx] # current character
        if char_idx.get(c) is None: # check if char in dict
            char_idx[c] = idx   # add to dict
            current[1] += 1 # next char
            idx+=1 
            
        else: # repeated char
            longest = longerIdx(longest, current).copy() # compare substring
            current[0] = char_idx[c] + 1 # start after the previous repeated substring

            for i in range(sdx, current[0]): # remove previous substring from dict
                char_idx[s[i]] = None 

            sdx = current[0]

    longest = longerIdx(longest, current)
    return s[longest[0]:longest[1]]

def main():
    samples = [
        "a",
        "carbonara",
        "talong",
        "carboncarbont",
        "aranara",
        "wowdasurbwow"
    ]

    for str in samples:
        print(str, longest_substring(str))

if __name__ == "__main__":
    main()