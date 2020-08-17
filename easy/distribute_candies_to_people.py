class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        ans = [0] * num_people
        count = 1
        curr_person = 0
        while candies > count:
            ans[curr_person] += count
            candies -= count
            count += 1
            curr_person = (curr_person + 1) % num_people
        ans[curr_person] += candies
        return ans
