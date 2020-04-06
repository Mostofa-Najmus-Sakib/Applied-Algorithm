/*
LeetCode Problem 122. Best Time to Buy and Sell Stock II
Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
Written by: Mostofa Adib Shakib
Language: C++

*/

class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int ans = 0;
        
        for(int i = 1; i < prices.size(); i++){
            if ( prices[i] - prices[i-1] > 0){
                ans += prices[i] - prices[i-1];
            }
        }
     return ans;
    }
};