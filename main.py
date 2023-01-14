from sorts_visualize.application.state import State
from sorts_visualize.config.config import read_config
from sorts_visualize.sort_algorithms.default import Default
from sorts_visualize.ui.main_window import MainWindow


config = read_config()
state = State(config=config)

algorithm = Default(state.data)
window = MainWindow(state=state, config=config, algorithm=algorithm)

if __name__ == '__main__':
    window.run()



