from sorts_visualize.sort_algorithms.base import BaseSortAlgorithm


class BiDirectionBubbleSort(BaseSortAlgorithm):
    def __init__(self, data):
        super().__init__(data)
        self.name = 'BiDirectionBubbleSort'
        self.description = """
            Try to sorting neighbor elements again and again while some neighbor elements a change places.
            Goes forward and backward 
        """
        self.is_direct = True
        self.start_position = 0
        self.end_position = len(self.data) - 1
        self.current_position = self.start_position

    def sort(self):
        if self.is_direct:
            if self.current_position < self.end_position:
                if self.data[self.current_position] > self.data[self.current_position + 1]:
                    self.data[self.current_position], self.data[self.current_position + 1] = self.data[self.current_position + 1], self.data[self.current_position]
                res = [self.current_position, self.current_position + 1]
                self.current_position += 1
            else:
                self.is_direct = False
                res = [self.current_position]
        else:
            if self.current_position > self.start_position:
                if self.data[self.current_position] < self.data[self.current_position - 1]:
                    self.data[self.current_position], self.data[self.current_position - 1] = self.data[self.current_position - 1], self.data[self.current_position]
                res = [self.current_position, self.current_position - 1]
                self.current_position -= 1
            else:
                self.is_direct = True
                res = [self.current_position]
        return res

