#include <unordered_map>
#include <vector>

using namespace std;

int count_pairs(vector<int> data, int target) {
    int result = 0;
    unordered_map<int, int> counter;
    
    for (int num : data) {
        // Check if num + target is in the counter
        int complement = num + target;
        
        // If num + target has been seen before, increment the result
        if (counter.find(complement) != counter.end()) {
            result += counter[complement];
        }
        
        // Add or update the current number in the counter unordered_map
        counter[num]++;
    }
    
    return result;
}
