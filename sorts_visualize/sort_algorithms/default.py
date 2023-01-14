from sorts_visualize.sort_algorithms.base import BaseSortAlgorithm


class Default(BaseSortAlgorithm):
    def __init__(self, data):
        super().__init__(data)
        self.name = 'default'
        self.is_direct = True
        self.position = 0

    def sort(self):
        if self.is_direct:
            if self.data[self.position] > self.data[self.position + 1]:
                self.data[self.position], self.data[self.position + 1] = self.data[self.position + 1], self.data[
                    self.position]
            self.position += 1
            if self.position == len(self.data) - 1:
                self.is_direct = False
            return [self.position, self.position + 1]
        else:
            if self.data[self.position] < self.data[self.position - 1]:
                self.data[self.position], self.data[self.position - 1] = self.data[self.position - 1], self.data[
                    self.position]
            self.position -= 1
            if self.position == 0:
                self.is_direct = True
            return [self.position, self.position - 1]

