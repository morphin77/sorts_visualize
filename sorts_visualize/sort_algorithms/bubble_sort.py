from sorts_visualize.sort_algorithms.base import BaseSortAlgorithm


class BubbleSort(BaseSortAlgorithm):
    def __init__(self, data):
        super().__init__(data)
        self.name = 'Bubble sort'
        self.description = """
            Try to sorting neighbor elements again and again while some neighbor elements a change places.
        """
        self.start_position = 0
        self.end_position = len(self.data) - 1
        self.current_position = self.start_position

    def sort(self):
        if self.current_position < self.end_position:
            if self.data[self.current_position] > self.data[self.current_position + 1]:
                self.data[self.current_position], self.data[self.current_position + 1] = self.data[self.current_position + 1], self.data[self.current_position]
            self.current_position += 1
        else:
            self.current_position = self.start_position
            self.end_position -= 1
        return [self.current_position, self.current_position + 1]




