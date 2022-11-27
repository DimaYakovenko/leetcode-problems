class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        return len(set([l for l in sentence])) == 26
        