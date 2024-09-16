class Solution:
    def numberOfBeautifulIntegers(self, low: int, high: int, k: int) -> int:
        from functools import lru_cache

        def solve(N):
            N = str(N)
            n = len(N)
            
            from sys import setrecursionlimit
            setrecursionlimit(10000)

            @lru_cache(None)
            def dfs(pos, count_even, count_odd, mod, tight, leading_zero):
                if pos == n:
                    if leading_zero == False and count_even == count_odd and mod == 0:
                        return 1
                    else:
                        return 0
                ans = 0
                max_digit = int(N[pos]) if tight else 9
                for d in range(0, max_digit + 1):
                    new_tight = tight and (d == max_digit)
                    new_leading_zero = leading_zero and (d == 0)
                    new_count_even = count_even
                    new_count_odd = count_odd
                    new_mod = mod
                    if new_leading_zero == False:
                        if d % 2 == 0:
                            new_count_even += 1
                        else:
                            new_count_odd += 1
                        new_mod = (mod * 10 + d) % k
                    ans += dfs(pos + 1, new_count_even, new_count_odd, new_mod, new_tight, new_leading_zero)
                return ans

            return dfs(0, 0, 0, 0, True, True)

        # Compute the count up to high and subtract the count up to low - 1
        result = solve(high) - solve(low - 1)
        return result
        