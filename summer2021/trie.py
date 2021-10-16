class TrieNode: 
      
    # Trie node class 
    def __init__(self): 
        self.children = [None]*26
  
        # isEndOfWord is True if node represent the end of the word 
        self.endOfWord = False
    
class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def add_word(self, word):
        node = self.root
        for c in word:
            i = ord(c) - 97
            if not node.children[i]:
                node.children[i] = TrieNode()
            node = node.children[i]

        node.endOfWord = True

    def search_word(self, word):
        node = self.root
        for c in word:
            i = ord(c) - 97
            if node.children[i]:
                node = node.children[i]
            else:
                return False

        return node.endOfWord

t = Trie()
t.add_word("the")
t.add_word("their")
print(t.search_word("then"))
print(t.search_word("their"))
t.add_word("then")
print(t.search_word("th"))
