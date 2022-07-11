// Given two strings s and t, return true if t is an anagram of s, and false otherwise.
class Solution {
    private HashMap<Character, Integer> prequenceS = new HashMap<>();
    private HashMap<Character, Integer> prequenceT = new HashMap<>();
    
    public boolean isAnagram(String s, String t) {
        putString(prequenceS, s);
        putString(prequenceT, t);
        return prequenceS.equals(prequenceT);
    }
    
    public void putString(HashMap<Character, Integer> h, String s) {
        for (int i = 0; i < s.length(); i++) {
            if (h.get(s.charAt(i)) == null) {
                h.put(s.charAt(i), 1);
            } else {
                h.put(s.charAt(i), h.get(s.charAt(i)) + 1);
            }
        }
    }
}
