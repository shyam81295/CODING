class Solution:
    def firstMissingPositive(self, A):
        """
            :param A: list of integers
            :return missing_positive: integer
        """
        for i in range(len(A)):
            if A[i] <= 0:
                A[i] = 2*len(A)

        for i in range(len(A)):
            if 1 <= A[i] <= len(A):
                # repeated values ke liye multiple baar nhi hona chahiye
                if A[A[i]-1] > 0:
                    A[A[i]-1] *= -1
            elif -len(A) <= A[i] <= -1:
                # repeated values ke liye multiple baar nhi hona chahiye
                if A[-A[i]-1] > 0:
                    A[-A[i]-1] *= -1

        missing_positive = 0
        is_all_in_range = True
        for i in range(len(A)):
            missing_positive += 1
            if A[i] >= 0:
                is_all_in_range = False
                break

        return missing_positive if not is_all_in_range else len(A)+1
