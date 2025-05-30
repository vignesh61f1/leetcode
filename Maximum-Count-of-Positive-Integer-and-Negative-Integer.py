class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        c1,c2=0,0
        for num in nums:
            if num<0:
                c1+=1
            elif num>0:
                c2+=1
            else:
                continue
        return max(c1,c2)


        