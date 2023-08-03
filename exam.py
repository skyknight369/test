from collections import Counter
from typing import List
def sumOfPower( nums: List[int]) -> int:
    MOD=10**9+7
    cnt=Counter(nums)
    vals=sorted(cnt.keys())
    n=len(vals)
    ans=0
    for i in range(n-1,-1,-1):
        num=0
        cal=vals[i]**2
        for j in range(i,-1,-1):
            num+=cnt[vals[j]]
            ans+=(2**num-1)*cal*vals[j]
        ans%=MOD
    return ans 

print(sumOfPower([2,1,4]))