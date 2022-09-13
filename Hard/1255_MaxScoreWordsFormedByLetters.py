# Given a list of words, list of  single letters (might be repeating) and score of every character.

# Return the maximum score of any valid set of words formed by using the given letters (words[i] cannot be used two or more times).

# It is not necessary to use all characters in letters and each letter can only be used once. Score of letters 'a', 'b', 'c', ... ,'z' is given by score[0], score[1], ... , score[25] respectively.

class Solution(object):
    def maxScoreWords(self, words, letters, score):
        """
        :type words: List[str]
        :type letters: List[str]
        :type score: List[int]
        :rtype: int
        """
        def get_sum(word):
            Letter = Ls.copy()
            s = 0
            for i in word:
                if i in Letter.keys() and Letter[i] != 0:
                    s += score[ord(i) - 97]
                    Letter[i] -= 1
                else:
                    return 0
            return s
        
        def backtrack(res, cur, idx, di):
            if idx == len(valid_lst):
                res[0] = max(res[0], cur)
                return
            di_copy = di.copy()
            for i in range(idx, len(valid_lst)):
                br = False
                for ch in valid_lst[i]:
                    di[ch] = 1 if ch not in di.keys() else di[ch] + 1
                    if di[ch] > Ls[ch]:
                        res[0] = max(res[0], cur)
                        br = True
                        continue
                if not br:
                    cur += valid_dict[valid_lst[i]]
                    backtrack(res, cur, i+1, di)
                    cur -= valid_dict[valid_lst[i]]
                di = di_copy.copy()
                
        Ls = dict()
        for i in letters:
            if i in Ls.keys():
                Ls[i] += 1
            else:
                Ls[i] = 1

        valid_lst = []
        valid_dict = dict()
        for i in words:
            su = get_sum(i)
            if su > 0:
                valid_dict[i] = su
                valid_lst.append(i)

        res = [0]
        dic = dict()
        backtrack(res, 0, 0, dic)
        
        return res[0]