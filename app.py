"""A simple status bar app in Mac OS using rumps.

The script mimics a real user moving the mouse pointer and clicking at random
locations on the screen. Great to fool Teams.

"""

from __future__ import annotations

import os
import random
import sys
from threading import Timer

import pyautogui as pag
import rumps


def get_resource_path(relative_path):
    """Get absolute path to a resource, works for PyInstaller onefile builds."""
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)


class StatusBarApp(rumps.App):
    def __init__(self):
        icon_path = get_resource_path("icon.png")
        super().__init__("AFK Bot", icon=icon_path)
        self.menu = ["Start", "Stop"]
        self.running = False
        self.timer = None

        # Disable "Stop" initially
        self.menu["Stop"].set_callback(None)

        # Get screen dimensions
        screen_size = pag.size()
        self.screen_width = screen_size[0]
        self.screen_height = screen_size[1]

    @rumps.clicked("Start")
    def start_bot(self, _):
        if not self.running:
            self.running = True
            self.menu["Start"].set_callback(None)
            self.menu["Stop"].set_callback(self.stop_bot)
            self.schedule_next_action()

    @rumps.clicked("Stop")
    def stop_bot(self, _):
        if self.running:
            self.running = False
            if self.timer:
                self.timer.cancel()
            self.menu["Stop"].set_callback(None)
            self.menu["Start"].set_callback(self.start_bot)

    def schedule_next_action(self):
        if self.running:
            interval = random.randint(10, 15)
            self.timer = Timer(interval, self.perform_action)
            self.timer.start()

    def perform_action(self):
        if self.running:
            # Perform random mouse movement
            x = random.randint(0, self.screen_width)
            y = random.randint(0, self.screen_height)
            pag.moveTo(x, y, duration=0.5)

            percent = random.random()
            if 0.4 <= percent <= 0.6:
                pag.moveTo(
                    self.screen_width + 5,
                    int(self.screen_height * percent),
                    duration=0.0,
                )
                pag.click()
                pag.moveTo(x, y, duration=0.0)

            # Schedule the next action
            self.schedule_next_action()


if __name__ == "__main__":
    StatusBarApp().run()
