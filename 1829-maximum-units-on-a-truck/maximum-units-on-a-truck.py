class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        sorted_pairs = sorted(boxTypes , key = lambda x: x[1], reverse = True)
        val= 0
        for x in sorted_pairs:
            if x[0]<= truckSize:
                truckSize -= x[0] #greedy
                val +=x[1]*x[0]
            else:
                val += truckSize*x[1]
                break
        return val            

        