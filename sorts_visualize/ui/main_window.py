import pygame


class MainWindow:
    def __init__(self, config):
        self.cnf = config

        pygame.init()
        pygame.display.set_caption("Sorts")
        self.screen = pygame.display.set_mode((self.cnf.window.width, self.cnf.window.height))
        self.clock = pygame.time.Clock()

    def run(self, state):
        self.screen.fill(self.cnf.window.background)  # clear screen

        if state.is_worked and not state.is_sorted:  # check statuses and run iteration of sorting
            state.positions = state.algorithm.sort()
        state.is_sorted = state.algorithm.is_sorted()  # update statuses

        self._render_layout(state=state)
        self._render_array_elements(state=state)

        pygame.display.flip()

        self.clock.tick(self.cnf.main_loop.fps)

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

    def _render_array_elements(self, state):
        chart_width = self.cnf.window.width - self.cnf.paddings.left - self.cnf.paddings.right
        chart_height = self.cnf.window.height - self.cnf.paddings.bottom - self.cnf.paddings.top
        offset_x = self.cnf.paddings.left
        bar_width = (chart_width - self.cnf.paddings.inner * len(state.data) - 1) / len(state.data)

        for index, el in enumerate(state.data):
            # bars
            bar_height = el * chart_height / state.max_el
            rect = pygame.Rect(
                offset_x,
                self.cnf.window.height - self.cnf.paddings.bottom - bar_height,
                bar_width,
                bar_height
            )
            # borders
            if index in state.positions:
                pygame.draw.rect(
                    self.screen,
                    self.cnf.figure.border_color,
                    pygame.Rect(
                        offset_x - self.cnf.figure.border_width,
                        self.cnf.window.height - self.cnf.paddings.bottom - bar_height - self.cnf.figure.border_width,
                        bar_width + self.cnf.figure.border_width + self.cnf.figure.border_width,
                        bar_height + self.cnf.figure.border_width
                    )
                )

            pygame.draw.rect(
                self.screen,
                self.cnf.figure.bar_color,
                rect
            )

            offset_x = offset_x + self.cnf.paddings.inner + bar_width

    def _render_layout(self, state):
        font_main = pygame.font.Font(
            'freesansbold.ttf',
            self.cnf.window.main_font.size,
        )
        font_secondary = pygame.font.Font(
            'freesansbold.ttf',
            self.cnf.window.secondary_font.size,
        )

        self._aside(state=state, font=font_secondary)
        self._header(state=state, font=font_main)
        self._footer(state=state, font=font_main)

    def _header(self, state, font):
        text_header = font.render(
            'Sorted Successfully' if state.is_sorted else 'Not sorted',
            True,
            self.cnf.window.main_font.color,
            self.cnf.window.background
        )
        text_rect_header = text_header.get_rect()
        text_rect_header.center = (
            (self.cnf.paddings.left + (self.cnf.window.width - self.cnf.paddings.left)) // 2,
            self.cnf.paddings.top // 2
        )
        self.screen.blit(text_header, text_rect_header)

    def _footer(self, state, font):
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
            self.cnf.window.main_font.color,
            self.cnf.window.background
        )
        text_rect_footer = text_footer.get_rect()
        text_rect_footer.center = (
            self.cnf.window.width // 2,
            self.cnf.window.height - (self.cnf.paddings.bottom // 2)
        )
        self.screen.blit(text_footer, text_rect_footer)

    def _aside(self, state, font):
        self._aside_header(state=state, font=font)
        self._aside_body(state=state, font=font)

    def _aside_header(self, state, font):
        text_aside_header = font.render(
            state.algorithm.name,
            True,
            self.cnf.window.secondary_font.color,
            self.cnf.window.background
        )
        text_rect_aside_header = text_aside_header.get_rect()
        text_rect_aside_header.center = (
            (self.cnf.paddings.left - (self.cnf.paddings.inner * 2)) // 2,
            self.cnf.paddings.top // 2
        )

        self.screen.blit(text_aside_header, text_rect_aside_header)

    def _aside_body(self, state, font):
        start_y = self.cnf.paddings.top + self.cnf.paddings.inner
        height = self.cnf.window.secondary_font.size
        start_x = self.cnf.paddings.inner
        width = self.cnf.paddings.left - self.cnf.paddings.inner * 2
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
                self.cnf.window.secondary_font.color,
                self.cnf.window.background
            )
            text_rect_aside_body = text_aside_body.get_rect()
            text_rect_aside_body.topleft = (
                start_x,
                start_y + height
            )
            self.screen.blit(text_aside_body, text_rect_aside_body)
            start_y += height
