class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        memoization = [amount + 1] * (amount + 1)
        
        memoization[0] = 0
        
        for num in range(1, amount + 1):
            for coin in coins:
                if num - coin >= 0:
                    memoization[num] = min(memoization[num], 1 + memoization[num-coin])
                    
        if memoization[amount] > amount:
            return -1
                    
        return memoization[amount]