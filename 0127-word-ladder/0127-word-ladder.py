class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        dictionary = {}
        for i in wordList:
            dictionary[i] = 0

        queue = []
        word = beginWord
        dictionary[beginWord] = 1

        while word != endWord:

            for i in range(len(word)):
                for j in range(26):
                    newWord = word[:i] + chr(j + ord("a")) + word[i + 1 :]

                    if newWord != word[0] and newWord in dictionary:
                        
                        if dictionary[newWord] == 0:
                            dictionary[newWord] = dictionary[word] + 1
                            queue.append(newWord)

            if len(queue):
                word = queue.pop(0)
            else:
                return 0

        return dictionary[word]
