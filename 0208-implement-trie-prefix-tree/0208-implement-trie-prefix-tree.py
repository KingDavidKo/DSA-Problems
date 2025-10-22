class Trie:

    def __init__(self):
        self.root = [None] * 27

    def insert(self, word: str) -> None:
        node = self.root
        for i in word:
            if node[ord(i) - ord('a')] is None:
                node[ord(i) - ord('a')] = [None] * 27
            node = node[ord(i) - ord('a')]
        node[-1] = 0

    def search(self, word: str) -> bool:
        node = self.root
        for i in word:
            if node[ord(i) - ord('a')] is None:
                return False
            node = node[ord(i) - ord('a')]
        return node[-1] is not None
        

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for i in prefix:
            if node[ord(i) - ord('a')] is None:
                return False
            node = node[ord(i) - ord('a')]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)