class Solution(object):
    def sortArrayByParityII(self, A):
        myArr = []
        for i in range(len(A)):
            if(i % 2 == A[i] % 2):
               myArr.append(A[i])
            else:
                if(i % 2 == 1):
                    for j in range(i + 1, len(A)):
                        if(A[j] % 2 == 1):
                            A[i], A[j] = A[j], A[i]
                            break

                elif(i % 2 == 0):
                    for j in range(i + 1, len(A) ):
                        if(A[j] % 2 == 0):
                            A[i], A[j] = A[j], A[i]
                            break

                myArr.append(A[i])
        return myArr
                

A = [4,2,5,7,4,2,5,7,4,2,5,7,4,2,5,7]

S = Solution().sortArrayByParityII(A)

print(S)

#################
#    Solution   #
#################

class Solution(object):
    def sortArrayByParityII(self, A):
        N = len(A)
        ans = [None] * N

        t = 0
        for i, x in enumerate(A):
            if x % 2 == 0:
                ans[t] = x
                t += 2

        t = 1
        for i, x in enumerate(A):
            if x % 2 == 1:
                ans[t] = x
                t += 2

        # We could have also used slice assignment:
        # ans[::2] = (x for x in A if x % 2 == 0)
        # ans[1::2] = (x for x in A if x % 2 == 1)

        return ans