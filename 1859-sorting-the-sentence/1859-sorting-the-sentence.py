class Solution:
    def sortSentence(self, s: str) -> str:
        words = s.split()
        res = len(words) * ['']
        for word in words:
            index = int(word[-1]) - 1
            res[index]= word[:-1]
        return ' '.join(res)
        