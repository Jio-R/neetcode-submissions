#include <vector>
#include <unordered_set>
#include <algorithm>

using namespace std;

class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        int longest = 0;
        unordered_set<int> S(nums.begin(), nums.end());

        for (int n : S) {
            if (!S.count(n - 1)) {
                int cur = 1;
                while (S.count(n + cur)) {
                    cur++;
                }
                longest = max(longest, cur);
            }
        }
        return longest;
    }
};