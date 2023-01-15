from dataclasses import dataclass
import random
from sorts_visualize.sort_algorithms.bubble_sort import BubbleSort
from sorts_visualize.sort_algorithms.bidirection_bubble_sort import BiDirectionBubbleSort
from sorts_visualize.sort_algorithms.improvement_bidirection_bubble_sort import ImprovementBiDirectionBubbleSort


@dataclass()
class State:
    def __init__(self, config):
        self.config = config
        self.algorithms = [
            BubbleSort,
            BiDirectionBubbleSort,
            ImprovementBiDirectionBubbleSort
        ]
        self.__initialize()

    @staticmethod
    def init_data(items_count):
        arr = [el for el in range(1, items_count)]
        random.shuffle(arr)
        return {
            'data': arr,
            'maximum': max(arr),
        }

    def reset(self):
        alg = self.algorithm
        self.__initialize()
        self.algorithm = alg.__class__(self.data)

    def next_algorithm(self):
        idx = self.algorithms.index(self.algorithm.__class__)
        if idx < len(self.algorithms) - 1:
            self.algorithm = self.algorithms[idx + 1](data=self.data)

    def previous_algorithm(self):
        idx = self.algorithms.index(self.algorithm.__class__)
        if idx > 0:
            self.algorithm = self.algorithms[idx - 1](data=self.data)

    def __initialize(self):
        init_data = self.init_data(items_count=self.config['data']['count'])
        self.data = init_data['data']
        self.max_el = init_data['maximum']
        self.positions = []
        self.is_worked = False
        self.is_sorted = False
        self.algorithm = self.algorithms[0](data=self.data)
