from sorts_visualize.application.state import State
from sorts_visualize.config.config import read_config
from sorts_visualize.ui.main_window import MainWindow

# init data
config = read_config()
state = State(config=config)

window = MainWindow(config=config)

if __name__ == '__main__':
    running = True
    while running:
        running = window.run(state=state)





