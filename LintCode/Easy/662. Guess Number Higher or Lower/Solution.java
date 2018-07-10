/* The guess API is defined in the parent class GuessGame.
   @param num, your guess
   @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
      int guess(int num); */

public class Solution extends GuessGame {
    /**
     * @param n an integer
     * @return the number you guess
     */
    public int guessNumber(int n) {
        // Write your code here
        
        int start = 0, end = n;
        while(start + 1 < end) {
            int mid = start + (end - start) / 2;
            if(guess(mid) < 0) {
                end = mid;
            }else if(guess(mid) > 0) {
                start = mid;
            }else{
                return mid;
            }
        }
        
        if (guess(start) == 0) {
            return start;
        } else {
            return end;
        }

    }
}