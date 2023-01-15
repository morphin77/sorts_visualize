import yaml
from sorts_visualize.config.config_items.font import Font
from sorts_visualize.config.config_items.window import Window
from sorts_visualize.config.config_items.paddings import Paddings
from sorts_visualize.config.config_items.figure import Figure
from sorts_visualize.config.config_items.data import Data
from sorts_visualize.config.config_items.main_loop import MainLoop


class Config:
    def __init__(self):
        self.window = None
        self.paddings = None
        self.figure = None
        self.data = None
        self.main_loop = None
        self._read_config()

    def _read_config(self):
        with open('sorts_visualize/config/config.yaml') as f:
            cnf = yaml.load(f, Loader=yaml.Loader)
            main_font = Font(
                name=cnf['window']['main_font']['name'],
                color=self._normalize_color(cnf['window']['main_font']['color']),
                size=cnf['window']['main_font']['size']
            )
            secondary_font = Font(
                name=cnf['window']['secondary_font']['name'],
                color=self._normalize_color(cnf['window']['secondary_font']['color']),
                size=cnf['window']['secondary_font']['size']
            )
            self.window = Window(
                width=cnf['window']['width'],
                height=cnf['window']['height'],
                background=self._normalize_color(cnf['window']['background']),
                main_font=main_font,
                secondary_font=secondary_font
            )
            self.paddings = Paddings(
                left=int(cnf['paddings']['left']),
                right=int(cnf['paddings']['right']),
                bottom=int(cnf['paddings']['bottom']),
                top=int(cnf['paddings']['top']),
                inner=int(cnf['paddings']['inner']),
            )
            self.figure = Figure(
                border_width=int(cnf['figure']['border_width']),
                bar_color=self._normalize_color(cnf['figure']['chart_color']),
                border_color=self._normalize_color(cnf['figure']['border_color']),
            )
            self.data = Data(count=int(cnf['data']['count']))
            self.main_loop = MainLoop(fps=int(cnf['main_loop']['fps']))

    @staticmethod
    def _normalize_color(color):
        return [int(el) for el in color.replace(' ', '').split(',')]
