class Solution(object):
    def countCharacters(self, words, chars):
        # create an array
        # loop through words
        # loop through word
        # loop though chars
        # if char != char in word
        # break
        # else put word in array
        
        isGoodString = True
        count = 0
        for word in words:
            tempChars = chars
            for char in word:
                if(char not in tempChars):
                    isGoodString = False
                else:
                    tempChars = tempChars.replace(char, '', 1)

            if(isGoodString):
                count += len(word)
            else:
                isGoodString = True
        
        return count

words = ["cat","bt","hat","tree"]
chars = "atach"
S = Solution().countCharacters(words, chars)

print(S)


### Solution

class Solution(object):
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """
        total = 0
        for word in words:
            valid = True
            i = 0
            while i<len(word) and valid:
                x = chars.count(word[i])
                valid = x > 0 and word.count(word[i]) <= x
                i+=1
            if valid:
                total+=len(word)
        return total