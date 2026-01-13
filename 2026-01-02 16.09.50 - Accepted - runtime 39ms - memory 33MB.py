class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        from collections import Counter
        count = Counter(tasks)
        result = 0
        for freq in count.values():
            if freq == 1:
                return -1
            # Use as many 3s as possible
            result += (freq + 2) // 3
        return result