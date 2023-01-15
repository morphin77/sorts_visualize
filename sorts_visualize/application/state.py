import random
from sorts_visualize.application.values import Values
from sorts_visualize.sort_algorithms.base import BaseSortAlgorithm
from sorts_visualize.sort_algorithms.bubble_sort import BubbleSort
from sorts_visualize.sort_algorithms.bidirection_bubble_sort import BiDirectionBubbleSort
from sorts_visualize.sort_algorithms.improvement_bidirection_bubble_sort import ImprovementBiDirectionBubbleSort
from sorts_visualize.sort_algorithms.inserting_sort import InsertingSort


class State:
    def __init__(self, config):
        self.algorithm = None
        self.config = config
        self.algorithms = BaseSortAlgorithm.__subclasses__()
        self._initialize()

    def reset(self):
        alg = self.algorithm
        self._initialize()
        self.algorithm = alg.__class__(self.data)

    def next_algorithm(self):
        idx = self.algorithms.index(self.algorithm.__class__)
        if idx < len(self.algorithms) - 1:
            self._initialize()
            self.algorithm = self.algorithms[idx + 1](data=self.data)

    def previous_algorithm(self):
        idx = self.algorithms.index(self.algorithm.__class__)
        if idx > 0:
            self._initialize()
            self.algorithm = self.algorithms[idx - 1](data=self.data)

    @staticmethod
    def _init_data(items_count):
        arr = [el for el in range(1, items_count)]
        random.shuffle(arr)
        return Values(data=arr)

    def _initialize(self):
        init_data = self._init_data(items_count=self.config.data.count)
        self.data = init_data.data
        self.max_el = init_data.maximum
        self.positions = []
        self.is_worked = False
        self.is_sorted = False
        self.algorithm = self.algorithms[0](data=self.data)
        self.iterations = 0
