class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        l = []
        for i in nums:
            if i not in d:
                d[i] = 1
            else :
                d[i] +=1    

        d2 = dict(sorted(d.items(), key=lambda x: x[1], reverse=True))
        
        for key in d2.keys():
            if k == 0 :
                break

            l.append(key)
            k -= 1

        return l    



        