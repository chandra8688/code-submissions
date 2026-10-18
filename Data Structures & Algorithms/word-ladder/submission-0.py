from collections import deque 
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_set = set(wordList)

        if endWord not in word_set:
            return 0

        queue = deque([(beginWord, 1)])
        word_set.discard(beginWord)
        while queue:
            word, steps = queue.popleft()
            if word == endWord:
                return steps

            for i in range(len(word)):
                for ch in "abcdefghijklmnopqrstuvwxyz":
                    if ch == word[i]:
                        continue

                    next_word = word[:i] +ch+word[i+1:]

                    if next_word in word_set:
                        word_set.remove(next_word)
                        queue.append((next_word, steps+1))
        return 0