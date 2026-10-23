from collections import defaultdict,deque
class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        chars = set("".join(words))
        graph = {ch:set() for ch in chars}
        indegree={ch:0 for ch in chars}

        for i in range(len(words)-1):
            w1=words[i]
            w2=words[i+1]
            min_len = min(len(w1),len(w2))
            if  len(w1)>len(w2) and w1[:min_len] == w2[:min_len]:
                return ""
            for j in range(min_len):
                if w1[j] != w2[j]:
                    a=w1[j]
                    b=w2[j]

                    if b not in graph[a]:
                        graph[a].add(b)
                        indegree[b] +=1
                    break
        queue = deque(ch for ch in chars if indegree[ch]==0)
        order = []

        while queue:
            ch = queue.popleft()
            order.append(ch)
            for neighbor in graph[ch]:
                indegree[neighbor]-=1
                if indegree[neighbor]==0:
                    queue.append(neighbor)
        if len(order) != len(chars):
            return ""
        return "".join(order)
        