from dataclasses import dataclass
import random


@dataclass()
class State:
    def __init__(self, config):
        self.config = config
        self.__initialize()

    @staticmethod
    def init_data(cnt):
        arr = [el for el in range(1, cnt)]
        random.shuffle(arr)
        return {
            'data': arr,
            'maximum': max(arr),
        }

    def reset(self):
        self.__initialize()

    def __initialize(self):
        init_data = self.init_data(self.config['data']['count'])
        self.data = init_data['data']
        self.max_el = init_data['maximum']
        self.positions = []
        self.is_worked = False
        self.is_sorted = False
