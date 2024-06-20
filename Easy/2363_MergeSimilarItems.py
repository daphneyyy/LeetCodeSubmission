class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        weights = dict()
        for i in items1:
            weights[i[0]] = i[1]
        for i in items2:
            if i[0] in weights:
                weights[i[0]] += i[1]
            else:
                weights[i[0]] = i[1]
        sorted_items = sorted(weights.items())
        return [list(item) for item in sorted_items]
