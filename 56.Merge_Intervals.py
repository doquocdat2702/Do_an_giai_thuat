class Solution:
    def merge(self, intervals):

        # Sort theo start
        intervals.sort(key=lambda x: x[0])

        merged = []

        for interval in intervals:

            # Nếu chưa có hoặc không overlap
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)

            else:
                # Merge interval
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged