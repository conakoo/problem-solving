class Node:
    def __init__(self):
        self.child = {}
        self.sentences = defaultdict(int) # sentence -> degree

class AutocompleteSystem:

    def _insert(self, sentence, count):
        node = self.root
        for c in sentence:
            if c not in node.child:
                node.child[c] = Node()
            node = node.child[c]
            node.sentences[sentence] += count

    def __init__(self, sentences: List[str], times: List[int]):
        self.root = Node()
        n = len(sentences)
        for i in range(n):
            sentence = sentences[i]
            time = times[i]
            self._insert(sentence, time)
            
        self.prefix = ''
        self.cur = self.root
        self.end = Node()

    def input(self, c: str) -> List[str]:
        if c == '#':
            self._insert(self.prefix, 1)
            self.prefix = ''
            self.cur = self.root
            return []
        
        self.prefix += c
        if c not in self.cur.child:
            self.cur = self.end
            return []
        
        self.cur = self.cur.child[c]
        sentences = self.cur.sentences
        sentences = sorted(sentences.items(), key= lambda x: (-x[1], x[0]))

        ans = []
        for i in range(min(3, len(sentences))):
            ans.append(sentences[i][0])
        return ans


# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)
