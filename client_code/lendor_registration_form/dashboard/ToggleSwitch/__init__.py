from ._anvil_designer import ToggleSwitchTemplate
from anvil import *
import math

class ToggleSwitch(ToggleSwitchTemplate):
    def __init__(self, **properties):
        # Any code you write here will run when the form opens.
        self._checked = properties.get('checked', False)
        self._mouseclicked = False
        self._pi = math.pi

        self._enabled = properties.get('enabled', False)  # Provide a default value
        self._visible = True

        self._ball_x_checked = 0
        self._ball_x_unchecked = 0

        self._ball_current_x = 0
        self._ball_current_y = 0
        self._ball_destination_x = 0
        self._ball_destination_y = 0
        self._ball_velocity = 1
        self._ball_colour = "white"
        self._ball_enabled_colour = properties.get('enabled_colour', 'white')  # Provide a default value
        self._ball_disabled_colour = properties.get('disabled_colour', 'gray')  # Provide a default value
        self._animating = False

        self._lozenge_background_unchecked = properties.get('unchecked_colour', 'lightgray')  # Provide a default value
        self._lozenge_background_checked = properties.get('checked_colour', 'lightgreen')  # Provide a default value
        self._lozenge_width = 30
        self._lozenge_height = 30
        self._lozenge_radius = self._lozenge_height / 2

        self.init_components(**properties)

    def form_show(self, **event_args):
        self.update()

    @property
    def checked(self):
        return self._checked

    @checked.setter
    def checked(self, value):
        if type(value) is bool:
            self._checked = value
            self.update()

    @property
    def enabled(self):
        return self._enabled

    @enabled.setter
    def enabled(self, value):
        if type(value) is bool:
            self._enabled = value
            self.update()

    @property
    def visible(self):
        return self._visible

    @visible.setter
    def visible(self, value):
        if type(value) is bool:
            self._visible = value
            self.canvas_1.visible = self._visible

    # This is the ball_x position when unchecked.
    def get_unchecked_x(self):
        return self._lozenge_radius + 2

    # This is the ball_x position when checked.
    def get_checked_x(self):
        return self._lozenge_width + self.get_unchecked_x()

    def update(self, **sponge):
        c = self.canvas_1
        c.clear_rect(0, 0, c.get_width(), c.get_height())
        self.draw_lozenge()
        self.draw_ball(self.get_unchecked_x() if not self.checked else self.get_checked_x())

    def draw_lozenge(self):
        c = self.canvas_1
        c.background = "transparent"
        c.stroke_style = "transparent"  # border colour

        if self._lozenge_height <= 0: self._lozenge_height = c.get_height()
        self._lozenge_radius = self._lozenge_height / 2

        c.fill_style = (self._lozenge_background_checked if self.checked and self.enabled else self._lozenge_background_unchecked)
        c.begin_path()

        x = self.get_unchecked_x()
        y = self._lozenge_height / 2
        r = self._lozenge_radius
        c.arc(x, y, r, 0.5 * self._pi, 1.5 * self._pi)
        c.arc(x + self._lozenge_width, y, r, 1.5 * self._pi, 0.5 * self._pi)
        c.line_to(x, y + r)

        c.close_path()
        c.fill()

    def draw_ball(self, x):
        c = self.canvas_1
        c.fill_style = (self._ball_enabled_colour if self.enabled else self._ball_disabled_colour)

        if self._lozenge_height <= 0: self._lozenge_height = c.get_height()
        self._lozenge_radius = self._lozenge_height / 2
        c.begin_path()

        y = self._lozenge_height / 2
        r = self._lozenge_radius
        c.arc(x, y, r - 2)

        c.fill()
        c.close_path()

    def timer_1_tick(self, **event_args):
        self._ball_current_x = self._ball_current_x + self._ball_move_x
        c = self.canvas_1

        if self._ball_current_x <= self.get_unchecked_x():
            self._ball_current_x = self.get_unchecked_x()
            self._animating = False
            self.timer_1.interval = 0
            self.checked = False
            self.raise_event("x_change")

        if self._ball_current_x >= self.get_checked_x():
            self._ball_current_x = self.get_checked_x()
            self._animating = False
            self.timer_1.interval = 0
            self.checked = True
            self.raise_event("x_change")

        self.draw_lozenge()
        self.draw_ball(self._ball_current_x)

    def toggle_switch(self, **event_args):
        self._animating = True
        if self.checked == False:
            self._ball_move_x = self._ball_velocity
            self._ball_current_x = self.get_unchecked_x()
        else:
            self._ball_move_x = -self._ball_velocity
            self._ball_current_x = self.get_checked_x()

        self.timer_1.interval = 0.001

    def canvas_1_mouse_down(self, x, y, button, **event_args):
        # Potential click
        if self.enabled: self._mouseclicked = True

    def canvas_1_mouse_up(self, x, y, button, **event_args):
        # Did we previously go down?
        if self._mouseclicked:
            self._mouseclicked = False
            # Are we already in an animation?
            if self._animating: return
            # Do it!
            self.toggle_switch()

    def canvas_1_mouse_leave(self, x, y, **event_args):
        # Abandon the click if the mouse leaves the control.
        self._mouseclicked = False

    def check_box_1_change(self, **event_args):
      """This method is called when this checkbox is checked or unchecked"""
      pass
