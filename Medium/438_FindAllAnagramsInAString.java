// Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

// An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

import java.util.HashMap;
import java.util.ArrayList;
import java.util.List;

class Solution {
    public HashMap<Character, Integer> hashString(String str) {
        HashMap<Character, Integer> char_cnt = new HashMap<>();
        for (int i = 0; i < str.length(); i++) {
            if (!char_cnt.containsKey(str.charAt(i)))  {
                char_cnt.put(str.charAt(i), 1);
            } else {
                int cnt = char_cnt.get(str.charAt(i));
                char_cnt.put(str.charAt(i), cnt + 1);
            }
        }
        return char_cnt;
    }

    public List<Integer> findAnagrams(String s, String p) {
        if (s.length() < p.length()) {
            return new ArrayList<Integer>();
        }
        List<Integer> res = new ArrayList<>();
        HashMap<Character, Integer> char_cnt = hashString(p);
        HashMap<Character, Integer> second_cnt = hashString(s.substring(0, p.length()));
        for (int i = 0; i < s.length(); i++) {
            if (char_cnt.equals(second_cnt)) {
                res.add(i);
            }
            char c = s.charAt(i);
            int cnt = second_cnt.get(c);
            if (cnt > 1) {
                second_cnt.put(c, cnt-1);
            } else {
                second_cnt.remove(c);
            }
            if (i + p.length() > s.length()-1) {
                break;
            }
            char ch = s.charAt(i+p.length());
            if (!second_cnt.containsKey(ch))  {
                second_cnt.put(ch, 1);
            } else {
                int cnnt = second_cnt.get(ch);
                second_cnt.put(ch, cnnt + 1);
            }
        }
        return res;
    }
}
