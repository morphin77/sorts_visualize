from sorts_visualize.sort_algorithms.base import BaseSortAlgorithm


class Default(BaseSortAlgorithm):
    def __init__(self, data):
        super().__init__(data)
        self.name = 'default'
        self.is_direct = True
        self.start_position = 0 if self.is_direct else len(self.data) - 1
        self.end_position = len(self.data) - 1 if self.is_direct else 0
        self.current_position = self.start_position

    def sort(self):
        if self.is_direct:
            if self.current_position < self.end_position:
                if self.data[self.current_position] > self.data[self.current_position + 1]:
                    self.data[self.current_position], self.data[self.current_position + 1] = self.data[self.current_position + 1], self.data[self.current_position]
                res = [self.current_position, self.current_position + 1]
                self.current_position += 1
            else:
                self.end_position -= 1
                self.is_direct = False
                res = [self.current_position]
        else:
            if self.current_position > self.start_position:
                if self.data[self.current_position] < self.data[self.current_position - 1]:
                    self.data[self.current_position], self.data[self.current_position - 1] = self.data[self.current_position - 1], self.data[self.current_position]
                res = [self.current_position, self.current_position - 1]
                self.current_position -= 1
            else:
                self.start_position += 1
                self.is_direct = True
                res = [self.current_position]
        return res

