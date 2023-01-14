class BaseSortAlgorithm:
    # data - array of values
    def __init__(self, data):
        self.name = ''
        self.data = data

    # store his inner state work step by step
    # return [] - positions of processed values
    def sort(self):
        pass

    # return Boolean
    # True if array of values is sorted
    # False if array of values is unsorted
    def is_sorted(self):
        i = 1
        while i < len(self.data):
            if self.data[i - 1] > self.data[i]:
                return False
            i += 1
        return True
