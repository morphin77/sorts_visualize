import pygame


class MainWindow:
    def __init__(self, config):
        self.cnf = config
        self.chart_width = self.cnf['window']['width'] - self.cnf['margins']['left_padding'] - self.cnf['margins']['right_padding']
        self.chart_height = self.cnf['window']['height'] - self.cnf['margins']['bottom_padding'] - self.cnf['margins']['top_padding']
        self.font_color = [int(el) for el in self.cnf['window']['font']['color'].replace(' ', '').split(',')]
        self.font_size = self.cnf['window']['font']['size']
        self.background_color = [int(el) for el in self.cnf['window']['background_color'].replace(' ', '').split(',')]
        self.chart_color = [int(el) for el in self.cnf['figure']['chart_color'].replace(' ', '').split(',')]
        self.chart_border_color = [int(el) for el in self.cnf['figure']['border_color'].replace(' ', '').split(',')]

        pygame.init()
        pygame.display.set_caption("Sorts")
        self.screen = pygame.display.set_mode((self.cnf['window']['width'], self.cnf['window']['height']))
        self.clock = pygame.time.Clock()

    def run(self, state):
        self.screen.fill(self.background_color)
        if state.is_worked and not state.is_sorted:
            state.positions = state.algorithm.sort()
        state.is_sorted = state.algorithm.is_sorted()

        self.render_main_window(state=state)
        self.render_elements(state=state)

        pygame.display.flip()

        self.clock.tick(self.cnf['main_loop']['fps'])

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    state.is_worked = not state.is_worked
                if event.key == pygame.K_r:
                    state.reset()
                if event.key == pygame.K_q:
                    return False
        return True

    def render_main_window(self, state):
        font = pygame.font.Font('freesansbold.ttf', self.font_size)
        text_header = font.render(
            'Не отсортирован(((' if not state.is_sorted else 'Отсортирован)))',
            True,
            self.font_color,
            self.background_color
        )
        text_rect_header = text_header.get_rect()
        text_rect_header.center = (
            self.cnf['window']['width'] // 2,
            self.cnf['margins']['top_padding'] // 2
        )
        self.screen.blit(text_header, text_rect_header)

        text_footer = font.render(
            'Space: начать, R: новый массив, Q: выход',
            True,
            self.font_color,
            self.background_color
        )
        text_rect_footer = text_footer.get_rect()
        text_rect_footer.center = (
            self.cnf['window']['width'] // 2,
            self.cnf['window']['height'] - (self.cnf['margins']['bottom_padding'] // 2)
        )
        self.screen.blit(text_footer, text_rect_footer)

    def render_elements(self, state):
        offset_x = self.cnf['margins']['left_padding']
        bar_width = (self.chart_width - self.cnf['margins']['inner_padding'] * len(state.data) - 1) / len(state.data)

        for index, el in enumerate(state.data):
            # bars
            bar_height = el * self.chart_height / state.max_el
            rect = pygame.Rect(
                offset_x,
                self.cnf['window']['height'] - self.cnf['margins']['bottom_padding'] - bar_height,
                bar_width,
                bar_height
            )
            # borders
            if index in state.positions:
                pygame.draw.rect(
                    self.screen,
                    self.chart_border_color,
                    pygame.Rect(
                        offset_x - self.cnf['figure']['border_width'],
                        self.cnf['window']['height'] - self.cnf['margins']['bottom_padding'] - bar_height - self.cnf['figure']['border_width'],
                        bar_width + self.cnf['figure']['border_width'] + self.cnf['figure']['border_width'],
                        bar_height + self.cnf['figure']['border_width']
                    )
                )

            pygame.draw.rect(
                self.screen,
                self.chart_color,
                rect
            )

            offset_x = offset_x + self.cnf['margins']['inner_padding'] + bar_width
