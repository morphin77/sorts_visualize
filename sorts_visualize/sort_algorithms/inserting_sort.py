from sorts_visualize.sort_algorithms.base import BaseSortAlgorithm


class InsertingSort(BaseSortAlgorithm):
    def __init__(self, data):
        super().__init__(data)
        self.name = 'Inserting sort'
        self.description = """
            A simple sorting algorithm that builds the final sorted array one item at a time by comparisons
        """
        self.start_position = 0
        self.current_position = self.start_position

    def sort(self):

        if self.current_position > self.start_position:
            if self.data[self.current_position - 1] > self.data[self.current_position]:
                self.data[self.current_position], self.data[self.current_position - 1] = self.data[self.current_position - 1], self.data[self.current_position]
                self.current_position = self.current_position - 1
            else:
                self.current_position += 1
        else:
            self.current_position = self.current_position + 1
        return [self.current_position - 1, self.current_position]





