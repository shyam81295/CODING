class Solution:
    def __init__(self):
        self.spiral_matrix = [[]]

        self.top = 0
        self.bottom = 0
        self.left = 0
        self.right = 0

        self.dir_change = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        self.direction = 0
        self.current_x = 0
        self.current_y = -1
        self.value = 0

    def generateMatrix(self, n: int):

        def init_spiral_matrix(n):
            self.spiral_matrix = [[0 for i in range(n)] for j in range(n)]

        def init_direction_ptrs(n):
            self.top = 0
            self.bottom = n-1
            self.left = 0
            self.right = n-1

        def get_moves_count():
            total_moves = 0
            if self.direction in (0, 2):
                total_moves = self.right-self.left+1
            elif self.direction in (1, 3):
                total_moves = self.bottom-self.top+1
            return total_moves

        def increment(moves_count):
            for i in range(moves_count):
                self.value += 1
                self.current_x = self.current_x + \
                    self.dir_change[self.direction][0]
                self.current_y = self.current_y + \
                    self.dir_change[self.direction][1]
                self.spiral_matrix[self.current_x][self.current_y] = self.value

        def update_markers():
            if self.direction == 0:
                self.top += 1
            elif self.direction == 1:
                self.right -= 1
            elif self.direction == 2:
                self.bottom -= 1
            elif self.direction == 3:
                self.left += 1

        def main():
            init_spiral_matrix(n)
            init_direction_ptrs(n)
            while (self.top <= self.bottom and self.left <= self.right):
                self.direction = self.direction % 4
                moves_count = get_moves_count()
                increment(moves_count)
                update_markers()
                self.direction += 1

        main()
        return self.spiral_matrix

# flake8: noqa
