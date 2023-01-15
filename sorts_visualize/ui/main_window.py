import pygame


class MainWindow:
    def __init__(self, config):
        self.cnf = config
        self.chart_width = self.cnf['window']['width'] - self.cnf['margins']['left_padding'] - self.cnf['margins'][
            'right_padding']
        self.chart_height = self.cnf['window']['height'] - self.cnf['margins']['bottom_padding'] - self.cnf['margins'][
            'top_padding']
        self.main_font = self.cnf['window']['main_font']['font']
        self.main_font_color = [int(el) for el in self.cnf['window']['main_font']['color'].replace(' ', '').split(',')]
        self.main_font_size = self.cnf['window']['main_font']['size']
        self.secondary_font = self.cnf['window']['secondary_font']['font']
        self.secondary_font_color = [int(el) for el in
                                     self.cnf['window']['secondary_font']['color'].replace(' ', '').split(',')]
        self.secondary_font_size = self.cnf['window']['secondary_font']['size']
        self.background_color = [int(el) for el in self.cnf['window']['background_color'].replace(' ', '').split(',')]
        self.chart_color = [int(el) for el in self.cnf['figure']['chart_color'].replace(' ', '').split(',')]
        self.chart_border_color = [int(el) for el in self.cnf['figure']['border_color'].replace(' ', '').split(',')]

        pygame.init()
        pygame.display.set_caption("Sorts")
        self.screen = pygame.display.set_mode((self.cnf['window']['width'], self.cnf['window']['height']))
        self.clock = pygame.time.Clock()

    def run(self, state):
        self.screen.fill(self.background_color)  # clear screen

        if state.is_worked and not state.is_sorted:  # check statuses and run iteration of sorting
            state.positions = state.algorithm.sort()
        state.is_sorted = state.algorithm.is_sorted()  # update statuses

        self.__render_layout(state=state)
        self.__render_array_elements(state=state)

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
                if event.key == pygame.K_UP:
                    state.next_algorithm()
                if event.key == pygame.K_DOWN:
                    state.previous_algorithm()

        return True

    def __render_array_elements(self, state):
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
                        self.cnf['window']['height'] - self.cnf['margins']['bottom_padding'] - bar_height -
                        self.cnf['figure']['border_width'],
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

    def __render_layout(self, state):
        font_main = pygame.font.Font(self.main_font, self.main_font_size)
        font_secondary = pygame.font.Font(self.secondary_font, self.secondary_font_size)

        self.__aside(state=state, font=font_secondary)
        self.__header(state=state, font=font_main)
        self.__footer(state=state, font=font_main)

    def __header(self, state, font):
        text_header = font.render(
            'Sorted Successfully' if state.is_sorted else 'Not sorted',
            True,
            self.main_font_color,
            self.background_color
        )
        text_rect_header = text_header.get_rect()
        text_rect_header.center = (
            (self.cnf['margins']['left_padding'] + (self.cnf['window']['width']-self.cnf['margins']['left_padding'])) // 2,
            self.cnf['margins']['top_padding'] // 2
        )
        self.screen.blit(text_header, text_rect_header)

    def __footer(self, state, font):
        text_footer = font.render(
            ' '.join(
                f"""
                    Space: {'Pause' if state.is_worked else 'Start'}, 
                    UP: Next algorythm, 
                    DOWN: Previous algorythm, 
                    R: Reset, 
                    Q: Exit
                """.split()
            ),
            True,
            self.main_font_color,
            self.background_color
        )
        text_rect_footer = text_footer.get_rect()
        text_rect_footer.center = (
            self.cnf['window']['width'] // 2,
            self.cnf['window']['height'] - (self.cnf['margins']['bottom_padding'] // 2)
        )
        self.screen.blit(text_footer, text_rect_footer)

    def __aside(self, state, font):
        self.__aside_header(state=state, font=font)
        self.__aside_body(state=state, font=font)

    def __aside_header(self, state, font):
        text_aside_header = font.render(
            state.algorithm.name,
            True,
            self.secondary_font_color,
            self.background_color
        )
        text_rect_aside_header = text_aside_header.get_rect()
        text_rect_aside_header.center = (
            (self.cnf['margins']['left_padding'] - (self.cnf['margins']['inner_padding'] * 2)) // 2,
            self.cnf['margins']['top_padding'] // 2
        )

        self.screen.blit(text_aside_header, text_rect_aside_header)

    def __aside_body(self, state, font):
        start_y = self.cnf['margins']['top_padding'] + self.cnf['margins']['inner_padding']
        height = self.secondary_font_size
        start_x = 10
        width = self.cnf['margins']['left_padding'] - self.cnf['margins']['inner_padding'] * 2
        lines = []
        arr = []

        for word in state.algorithm.description.split():
            arr.append(word)
            if font.size(' '.join(arr))[0] > width:
                arr.pop()
                lines.append(' '.join(arr))
                arr = [word]
        if len(arr) > 0:
            lines.append(lines.append(' '.join(arr)))

        for line in lines:
            text_aside_body = font.render(
                line,
                True,
                self.secondary_font_color,
                self.background_color
            )
            text_rect_aside_body = text_aside_body.get_rect()
            text_rect_aside_body.topleft = (
                start_x,
                start_y + height
            )
            self.screen.blit(text_aside_body, text_rect_aside_body)
            start_y += height
