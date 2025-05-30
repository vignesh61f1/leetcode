class Solution:
    def mostPoints(self, questions):
        n = len(questions)
        memo = [-1] * n
        return self.helper(questions, 0, n, memo)

    def helper(self, questions, i, n, memo):
        if i >= n:
            return 0
        if memo[i] != -1:
            return memo[i]

        skip = self.helper(questions, i + 1, n, memo)  # Skip the current question
        take = questions[i][0] + self.helper(questions, i + questions[i][1] + 1, n, memo)  # Take the current question

        memo[i] = max(skip, take)
        return memo[i]
