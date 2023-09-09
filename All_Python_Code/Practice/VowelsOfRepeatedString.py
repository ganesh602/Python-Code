import re
def find_vowel_substrings(s, k):
    vowels = 'AEIOUaeiou'
    consonants = 'QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm'
    
    substrings = re.findall(f'(?<=[{consonants}])([{vowels}]{{{k},}})(?=[{consonants}])', s)
    
    return substrings if substrings else -1

if __name__ == '__main__':
    s = input()
    k = 2  # Minimum length of vowels sequence
    
    result = find_vowel_substrings(s, k)
    
    if result == -1:
        print(result)
    else:
        for substring in result:
            print(substring)
