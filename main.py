from sorts_visualize.application.state import State
from sorts_visualize.config.config import Config
from sorts_visualize.ui.main_window import MainWindow

# init data
config = Config()
state = State(config=config)

window = MainWindow(config=config)

if __name__ == '__main__':
    running = True
    while running:
        running = window.run(state=state)





