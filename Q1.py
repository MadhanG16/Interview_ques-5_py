# Remove vowels unless they appear together

def remove_single_vowels(s):
    result = ""
    i = 0
    vowels = "aeiouAEIOU"

    while i < len(s):
        if s[i] in vowels:
            while i < len(s) and s[i] in vowels:
                i += 1
        else:
            result += s[i]
            i += 1
    return result

# Test examples
print(remove_single_vowels("Cat"))
print(remove_single_vowels("Compuuter"))  
