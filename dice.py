
def numRollsToTarget(self, n: int, k: int, target: int) -> int:
    memory = {}

    def dp(n, target):
        if n == 0:
            return 0 if target > 0 else 1
        if (n, target) in memory:
            return memory[(n, target)]
        to_return = 0
        for i in range(max(0, target-k), target):
            to_return += dp(n-1, i)
        memory[(n, target)] = to_return
        return to_return
    return dp(n, target) % (10**9 + 7)
