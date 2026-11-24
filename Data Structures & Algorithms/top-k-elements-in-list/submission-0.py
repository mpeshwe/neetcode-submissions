class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        for n in nums :
            freq[n]+=1
        
        heap = []
        for element,frequency in freq.items() : 
            heapq.heappush(heap , (frequency,element)) 
            if len(heap) > k :
                heapq.heappop(heap)
        return [x for _,x in heap]