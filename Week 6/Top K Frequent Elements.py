def topKFrequent(nums, k):
    freq_dict = {}
    for num in nums:
        freq_dict[num] = freq_dict.get(num, 0) + 1
    
    max_freq = len(nums)
    bucket = [[] for _ in range(max_freq + 1)]
    for num, freq in freq_dict.items():
        bucket[freq].append(num)
    
    result = []
    for freq in range(max_freq, 0, -1):
        if bucket[freq]:
            result.extend(bucket[freq])
            if len(result) >= k:
                break
    return result[:k]