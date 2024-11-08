from __future__ import annotations

from misc.path import resourcepath
from ._utils import seticon

import tkinter.ttk as ttk
import tkinter as tk


_BG_GREY = "#333333"
_BUTTON_GREY = "#555555"
_BUTTON_RED = "#BB0000"


class ProgressWindow:
    def __init__(
        self,
        master: tk.Misc,
        progress_length: int | None,
        modelname: str,
    ) -> None:
        self.progress_length = progress_length
        self.modelname = modelname

        self.window = tk.Toplevel(master, background=_BG_GREY)
        self.window.wm_geometry("500x300")
        self.window.wm_title(f"Loading model {modelname}")
        seticon(self.window, resourcepath("settings.png"))

        self.loading_label = tk.Label(
            self.window, text=f"Downloading model {modelname}", font=("Arial", 15)
        )
        self.loading_label.place(relx=0.5, rely=0.2, anchor=tk.CENTER)

        target_video_width = int(500 / 10)
        target_video_height = int(500 / 10)

        my_label = tk.Label(master)
        my_label.place(
            relx=0.5,
            rely=0.5,
            relwidth=target_video_width,
            relheight=target_video_height,
            anchor=tk.CENTER,
        )

        if self.progress_length != None:
            self.progress_bar = ttk.Progressbar(
                self.window, maximum=self.progress_length
            )
            self.progress_bar.place(
                relx=0.5, rely=0.7, relwidth=0.8, relheight=0.1, anchor=tk.CENTER
            )
            self.progress_label = tk.Label(self.window)
            self.progress_label.place(relx=0.5, rely=0.85, anchor=tk.N)

    def startunzip(self) -> None:
        if self.progress_length == None:
            return

        self.progress_bar.place_forget()
        self.progress_label.place_forget()

        self.loading_label.configure(text=f"Extracting model {self.modelname}")

    def close(self) -> None:
        self.window.wm_withdraw()
