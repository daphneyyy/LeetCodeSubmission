//  1346. Check If N and Its Double Exist
// Given an array arr of integers, check if there exists two integers N and M such that N is the double of M ( i.e. N = 2 * M).

import java.util.*;
class Solution {
    public boolean checkIfExist(int[] arr) {
        Hashtable<Integer, Integer> ht = new Hashtable<>();
        for (int i = 0; i < arr.length; i++) {
            if (ht.get(arr[i]) == null) {
                ht.put(arr[i], 1);
            } else {
                ht.put(arr[i], ht.get(arr[i]) + 1);
            }
        }
        for (int i = 0; i < arr.length; i++) {
            int doub = arr[i] * 2;
            if (doub == arr[i]) {
                if (ht.get(doub) > 1) {
                    return true;
                }
            } else if (ht.get(doub) != null) {
                return true;
            }
        }
        return false;
    }
}
