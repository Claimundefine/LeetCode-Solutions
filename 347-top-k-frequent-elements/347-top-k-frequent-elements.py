class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        
        arr = [[] for i in range(len(nums) + 1)] 
        
        for num in nums:
            if num not in hashmap:
                hashmap[num] = 0
            hashmap[num] += 1
        
        for n,c in hashmap.items():
            arr[c].append(n)
            
        ans = []
            
        for i in range(len(nums), -1, -1):
            for val in arr[i]:
                ans.append(val)
                if len(ans) == k:
                    return ans