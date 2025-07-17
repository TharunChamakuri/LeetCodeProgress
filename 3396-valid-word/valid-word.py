class Solution(object):
    def isValid(self, word):
        vowels = {'A' , 'E' , 'I' , 'O' , 'U' , 'a' , 'e' , 'i' , 'o' , 'u'}
        digits = {'0' , '1' , '2' , '3' , '4' , '5' , '6' , '7' , '8' , '9'}
        if len(word) < 3:
            return False
        consonant = 0
        vowel = 0
        digit = 0
        for ch in word:
            if ch in vowels:
                vowel += 1
            elif ch not in vowels and ch.isalpha():
                consonant += 1
            elif ch in digits:
                digit += 1
            else:
                return False
        if consonant >= 1 and vowel >= 1:
            return True
        else:
            return False

        