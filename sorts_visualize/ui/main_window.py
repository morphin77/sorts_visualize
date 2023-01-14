import pygame


class MainWindow:
    def __init__(self, state, config, algorithm):
        self.cnf = config
        pygame.init()
        pygame.display.set_caption("Sorts")
        self.screen = pygame.display.set_mode((self.cnf['window']['width'], self.cnf['window']['height']))
        self.clock = pygame.time.Clock()
        self.state = state
        self.algorithm = algorithm
        self.chart_width = self.cnf['window']['width'] - self.cnf['margins']['left_padding'] - self.cnf['margins']['right_padding']
        self.chart_height = self.cnf['window']['height'] - self.cnf['margins']['bottom_padding'] - self.cnf['margins']['top_padding']
        self.font_color = [int(el) for el in self.cnf['window']['font']['color'].replace(' ', '').split(',')]
        self.font_size = self.cnf['window']['font']['size']
        self.background_color = [int(el) for el in self.cnf['window']['background_color'].replace(' ', '').split(',')]
        self.chart_color = [int(el) for el in self.cnf['figure']['chart_color'].replace(' ', '').split(',')]
        self.chart_border_color = [int(el) for el in self.cnf['figure']['border_color'].replace(' ', '').split(',')]

    def run(self):
        running = True

        while running:
            self.screen.fill(self.background_color)
            if self.state.is_worked and not self.state.is_sorted:
                self.state.positions = self.algorithm.sort()
            self.state.is_sorted = self.algorithm.is_sorted()

            self.render_main_window()
            self.render_elements()

            pygame.display.flip()

            self.clock.tick(self.cnf['main_loop']['fps'])

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.state.is_worked = not self.state.is_worked
                    if event.key == pygame.K_r:
                        self.state.reset()
                    if event.key == pygame.K_q:
                        running = False

    def render_main_window(self):
        font = pygame.font.Font('freesansbold.ttf', self.font_size)
        text_header = font.render(
            'Не отсортирован(((' if not self.state.is_sorted else 'Отсортирован)))',
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

    def render_elements(self):
        offset_x = self.cnf['margins']['left_padding']
        bar_width = (self.chart_width - self.cnf['margins']['inner_padding'] * len(self.state.data) - 1) / len(self.state.data)

        for index, el in enumerate(self.state.data):
            # bars
            bar_height = el * self.chart_height / self.state.max_el
            rect = pygame.Rect(
                offset_x,
                self.cnf['window']['height'] - self.cnf['margins']['bottom_padding'] - bar_height,
                bar_width,
                bar_height
            )
            # borders
            if index in self.state.positions:
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
