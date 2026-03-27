class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        
        # intution 
        
        # use sliding window so and check the sum of the element inside the window 
        # if there are no same elements in the window get the sum and check if its the max we get 
        #  do this until we hit the end of the array and return the max sum

        
        # left = 0
        # win_sum = 0
        # max_win_sum = 0
        
        # for right in range(len(nums)):

        #     win_sum += nums[right]

        #     if right - left + 1 > k:
        #         win_sum -= nums[left]
        #         left += 1

        #     if right - left + 1 == k:
        #         elements = nums[left: right + 1]
                
        #         if len(set(elements)) == k:
        #             max_win_sum = max(max_win_sum, win_sum)
        
        # return max_win_sum

        # the above soln hit TLE

        count = defaultdict(int)
        left = 0
        win_sum = 0
        max_win_sum = 0

        for right in range(len(nums)):
            
            count[nums[right]] += 1
            win_sum += nums[right]

            
            if right - left + 1 > k:
                count[nums[left]] -= 1
                win_sum -= nums[left]

                if count[nums[left]] == 0:
                    del count[nums[left]]

                left += 1

            
            if right - left + 1 == k and len(count) == k:
                max_win_sum = max(max_win_sum, win_sum)

        return max_win_sum
