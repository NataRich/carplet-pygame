import pygame
import time
import sys

from context import Context


class Engine:
    # pygame init
    WIN_WIDTH, WIN_HEIGHT = 900, 600
    context = None
    w = None
    clock = None

    # fonts
    screen_font = None
    i_name_font = None
    i_number_font = None
    e_title_font = None
    e_desc_font = None
    c_title_font = None
    c_desc_font = None
    c_cons_font = None

    # sounds
    start_soundtrack = None
    finish_soundtrack = None
    select_soundtrack = None

    # images of indexes
    I1_IMG = None
    I2_IMG = None
    I3_IMG = None
    I4_IMG = None

    # misc
    has_clicked = False
    FPS = 15
    E = 2.5
    counter = 0
    cons = ""
    popup = False

    @classmethod
    def register_context(cls, context: Context):
        cls.context = context

    @classmethod
    def init(cls):
        pygame.init()
        # Get window
        cls.w = pygame.display.set_mode((cls.WIN_WIDTH, cls.WIN_HEIGHT))
        # Set game name
        pygame.display.set_caption(cls.context.name)
        # Get clock
        cls.clock = pygame.time.Clock()
        # Set fonts
        cls.screen_font = pygame.font.Font('assets/font/Abel-Regular.ttf', 50)
        cls.i_number_font = pygame.font.Font('assets/font/Abel-Regular.ttf', 40)
        cls.e_title_font = pygame.font.Font('assets/font/Abel-Regular.ttf', 25)
        cls.c_title_font = pygame.font.Font('assets/font/Abel-Regular.ttf', 25)
        cls.e_desc_font = pygame.font.Font('assets/font/Abel-Regular.ttf', 20)
        cls.i_name_font = pygame.font.Font('assets/font/Abel-Regular.ttf', 20)
        cls.c_desc_font = pygame.font.Font('assets/font/Abel-Regular.ttf', 16)
        # Set soundtracks
        cls.start_soundtrack = pygame.mixer.Sound('assets/sound/start.wav')
        cls.finish_soundtrack = pygame.mixer.Sound('assets/sound/finish.wav')
        cls.select_soundtrack = pygame.mixer.Sound('assets/sound/card_select.wav')
        # Set index images
        cls.I1_IMG = pygame.transform.scale(pygame.image.load(cls.context.indexes[0].icon), (48, 48))
        cls.I2_IMG = pygame.transform.scale(pygame.image.load(cls.context.indexes[1].icon), (48, 48))
        cls.I3_IMG = pygame.transform.scale(pygame.image.load(cls.context.indexes[2].icon), (48, 48))
        cls.I4_IMG = pygame.transform.scale(pygame.image.load(cls.context.indexes[3].icon), (48, 48))

    @classmethod
    def play(cls):
        cls.__intro()

    @classmethod
    def __intro(cls):
        while True:
            cls.__draw_intro()
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if e.type == pygame.MOUSEBUTTONUP:
                    cls.has_clicked = False

            start_pressed = cls.__press_button(400, 320, 125, 70, cls.start_soundtrack)
            if start_pressed:
                cls.__body()

    @classmethod
    def __body(cls):
        time.sleep(0.5)
        pygame.mixer.music.load('assets/sound/background.mp3')
        pygame.mixer.music.set_volume(0.05)
        pygame.mixer.music.play(-1)

        while True:
            if cls.context.plot_finished():
                cls.context.next_plot()

            if cls.context.context_finished() or cls.context.is_game_over():
                cls.__end()

            if cls.popup:
                cls.counter += 1
                if cls.counter >= cls.FPS * cls.E:
                    cls.popup = False
                    cls.counter = 0

            cls.__draw_body()
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if e.type == pygame.MOUSEBUTTONUP:
                    cls.has_clicked = False

            if not cls.popup:
                l_btn_pressed = cls.__press_button(150, 450, 150, 200, cls.select_soundtrack)
                m_btn_pressed = cls.__press_button(400, 450, 150, 200, cls.select_soundtrack)
                r_btn_pressed = cls.__press_button(650, 450, 150, 200, cls.select_soundtrack)
                l_card, m_card, r_card = cls.context.curr_event().cards

                if l_btn_pressed:
                    cls.context.indexes[0].value = l_card.effects[0]
                    cls.context.indexes[1].value = l_card.effects[1]
                    cls.context.indexes[2].value = l_card.effects[2]
                    cls.context.indexes[3].value = l_card.effects[3]
                    cls.context.next_event()
                    cls.cons = l_card.cons
                    cls.popup = True
                    continue

                if m_btn_pressed:
                    cls.context.indexes[0].value = m_card.effects[0]
                    cls.context.indexes[1].value = m_card.effects[1]
                    cls.context.indexes[2].value = m_card.effects[2]
                    cls.context.indexes[3].value = m_card.effects[3]
                    cls.context.next_event()
                    cls.cons = m_card.cons
                    cls.popup = True
                    continue

                if r_btn_pressed:
                    cls.context.indexes[0].value = r_card.effects[0]
                    cls.context.indexes[1].value = r_card.effects[1]
                    cls.context.indexes[2].value = r_card.effects[2]
                    cls.context.indexes[3].value = r_card.effects[3]
                    cls.context.next_event()
                    cls.cons = r_card.cons
                    cls.popup = True
                    continue

    @classmethod
    def __end(cls):
        pygame.mixer.music.stop()

        while True:
            cls.__draw_end()
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if e.type == pygame.MOUSEBUTTONUP:
                    cls.has_clicked = False

            replay_pressed = cls.__press_button(350, 320, 170, 70, cls.start_soundtrack)
            if replay_pressed:
                cls.popup = False
                cls.counter = 0
                cls.context.reset()
                cls.__body()

    @classmethod
    def __draw_intro(cls):
        welcome_msg = "Welcome to " + cls.context.name
        creator_msg = "Created by " + cls.context.creator

        # Render texts
        cls.w.fill((139, 0, 18))
        cls.__render_center_text(welcome_msg, cls.screen_font, "White", 450, 200, 400)
        cls.__render_center_text(creator_msg, cls.screen_font, "White", 450, 250, 300)

        # Render button
        cls.__render_button(400, 320, 125, 70, (139, 0, 18), "White", "Start")

        # Update
        cls.__update()

    @classmethod
    def __draw_body(cls):
        # Get context
        e = cls.context.curr_event()
        indexes = cls.context.indexes

        # Fill messages
        names = [cls.i_name_font.render(i.name, True, "Black") for i in indexes]
        numbers = [cls.i_number_font.render(str(i.value), True, "Black") for i in indexes]
        cards = e.cards

        cls.w.fill((255, 255, 255))

        # Render first index
        cls.w.blit(cls.I1_IMG, (100, 25))
        cls.w.blit(names[0], (90, 78))
        cls.w.blit(numbers[0], (170, 30))

        # Render second index
        cls.w.blit(cls.I2_IMG, (300, 25))
        cls.w.blit(names[1], (300, 78))
        cls.w.blit(numbers[1], (370, 30))

        # Render third index
        cls.w.blit(cls.I3_IMG, (500, 25))
        cls.w.blit(names[2], (480, 78))
        cls.w.blit(numbers[2], (570, 30))

        # Render fourth index
        cls.w.blit(cls.I4_IMG, (700, 25))
        cls.w.blit(names[3], (690, 78))
        cls.w.blit(numbers[3], (770, 30))

        # Description Box
        pygame.draw.rect(cls.w, "Black", (120, 125, 710, 260))
        pygame.draw.rect(cls.w, "White", (125, 130, 700, 250))
        cls.__render_center_text(e.title, cls.e_title_font, "Black", 475, 140, 350)
        cls.__render_center_text(e.desc, cls.e_desc_font, "Black", 475, 250, 450)

        # Render cards
        cls.__render_card(150, 450, 150, 200, "White", "Black", cards[0].title, cards[0].desc)
        cls.__render_card(400, 450, 150, 200, "White", "Black", cards[1].title, cards[1].desc)
        cls.__render_card(650, 450, 150, 200, "White", "Black", cards[2].title, cards[2].desc)

        # Render consequence if popup
        if cls.popup:
            pygame.draw.rect(cls.w, "Red", (120, 125, 710, 260))
            pygame.draw.rect(cls.w, 'White', (125, 130, 700, 250))
            cls.__render_center_text(cls.cons, cls.e_desc_font, "Black", 475, 250, 450)

        # Update
        cls.__update()

    @classmethod
    def __draw_end(cls):
        i_index = cls.context.cause_index()
        end = cls.context.success if i_index == -1 else cls.context.indexes[i_index].end_str

        cls.w.fill((139, 0, 18))

        # Render texts
        cls.__render_center_text(end, cls.screen_font, "White", 450, 200, 700)

        # Render buttons
        cls.__render_button(350, 320, 170, 70, (139, 0, 18), "White", "Re-Play")

        # Update
        cls.__update()

    @classmethod
    def __update(cls):
        pygame.display.update()
        cls.clock.tick(cls.FPS)

    @classmethod
    def __is_hover(cls, x, y, width, height) -> bool:
        mouse_x = pygame.mouse.get_pos()[0]
        mouse_y = pygame.mouse.get_pos()[1]
        if (x + width) > mouse_x > x and (y + height) > mouse_y > y:
            return True
        return False

    @classmethod
    def __render_button(cls, x, y, width, height, hover_color, default_color, msg):
        s_bt = cls.screen_font.render(msg, True, hover_color)
        hover_s_bt = cls.screen_font.render(msg, True, default_color)
        rect_bt = s_bt.get_rect(midtop=(x + width / 2, y))

        if cls.__is_hover(x, y, width, height):
            pygame.draw.rect(cls.w, hover_color, (x, y, width, height))
            cls.w.blit(hover_s_bt, rect_bt)
        else:
            pygame.draw.rect(cls.w, default_color, (x, y, width, height))
            cls.w.blit(s_bt, rect_bt)

    @classmethod
    def __render_card(cls, x, y, width, height, hover_color, default_color, title, desc):
        float_height = 30

        s_ct = cls.c_title_font.render(title, True, hover_color)
        s_cd = cls.c_desc_font.render(desc, True, hover_color)
        hover_s_ct = cls.c_title_font.render(title, True, default_color)
        hover_s_cd = cls.c_desc_font.render(desc, True, default_color)
        rect_ct = s_ct.get_rect(midtop=(x + width / 2, y))
        rect_cd = s_ct.get_rect(midtop=(x + width / 2, y + height / 2))
        hover_rect_ct = s_ct.get_rect(midtop=(x + width / 2, y - float_height))
        hover_rect_cd = s_ct.get_rect(midtop=(x + width / 2, y + height / 2 - float_height))

        if cls.__is_hover(x, y, width, height):
            pygame.draw.rect(cls.w, hover_color, (x, y - float_height, width, height))
            cls.w.blit(hover_s_ct, hover_rect_ct)
            cls.w.blit(hover_s_cd, hover_rect_cd)
        else:
            pygame.draw.rect(cls.w, default_color, (x, y, width, height))
            cls.w.blit(s_ct, rect_ct)
            cls.w.blit(s_cd, rect_cd)

    @classmethod
    def __render_center_text(cls, msg, font, color, x, y, allowed_width):
        words = msg.split()
        lines = []
        while len(words) > 0:
            line_words = []
            while len(words) > 0:
                line_words.append(words.pop(0))
                w, h = font.size(' '.join(line_words + words[:1]))
                if w > allowed_width:
                    break
            line = ' '.join(line_words)
            lines.append(line)

        y_offset = 0
        for line in lines:
            w, h = font.size(line)
            fx = x - w / 2
            fy = y + y_offset

            s = font.render(line, True, color)
            cls.w.blit(s, (fx, fy))

            y_offset += h

    @classmethod
    def __press_button(cls, x, y, width, height, sound):
        click = pygame.mouse.get_pressed(3)
        if cls.__is_hover(x, y, width, height) and click[0] == 1 and not cls.has_clicked:
            cls.has_clicked = True
            pygame.mixer.Sound.play(sound)
            return True
        return False
