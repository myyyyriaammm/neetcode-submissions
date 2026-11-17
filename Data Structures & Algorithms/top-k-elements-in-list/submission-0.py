class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        l = []
        for i in nums:
            d[i] = 1 + d.get(i, 0)    

        d2 = dict(sorted(d.items(), key=lambda x: x[1], reverse=True))
        
        for key in d2.keys():
            if k == 0 :
                break

            l.append(key)
            k -= 1

        return l    



        