
str1 = 'abccbc'

def palindrome(str1):
    return True


palindrome_ss_list = []
for i in range(len(str)):
    for j in range(i+1, len(str) + 1):
        if palindrome(str1[i: j]):
            palindrome_ss_list.append(str1[i: j])