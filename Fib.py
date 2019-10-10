class Solution(object):
    def fib(self, N):
        if(N == 0):
            return 0
        elif(N == 1 or N == 2):
            return 1
        else:
            return self.fib(N - 1) + self.fib(N - 2)

S = Solution().fib(1)

for i in range(10):
    S = Solution().fib(i)
    print(f"{i}: {S}")
