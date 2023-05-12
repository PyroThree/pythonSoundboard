from tkinter import *
import soundboard


class GUI:
    def __init__(self, window):
        self.window = window

        title_label = Label(self.window, text="Sound Board", font=("Arial", 20))
        title_label.pack(pady=10)

        volume_frame = Frame(self.window)
        volume_frame.pack()

        self.volume_slider = Scale(volume_frame, from_=0, to=100, orient=HORIZONTAL, length=200)
        self.volume_slider.set(50)
        self.volume_slider.pack(side=LEFT)

        volume_label_frame = Frame(self.window)
        volume_label_frame.pack()

        volume_label = Label(volume_label_frame, text="Volume")
        volume_label.pack(side=LEFT, padx=10)

        sound_frame = Frame(self.window)
        sound_frame.pack()

        sound_column1 = Frame(sound_frame)
        sound_column1.pack(side=LEFT, padx=10)

        self.button1 = Button(sound_column1, text="Sound 1")
        self.button2 = Button(sound_column1, text="Sound 3")
        self.button3 = Button(sound_column1, text="Sound 5")

        self.button1.pack(pady=10)
        self.button2.pack(pady=10)
        self.button3.pack(pady=10)

        sound_column2 = Frame(sound_frame)
        sound_column2.pack(side=LEFT, padx=10)

        self.button4 = Button(sound_column2, text="Sound 2")
        self.button5 = Button(sound_column2, text="Sound 4")
        self.button6 = Button(sound_column2, text="Sound 6")

        self.button4.pack(pady=10)
        self.button5.pack(pady=10)
        self.button6.pack(pady=10)

        stop_and_quit_frame = Frame(self.window)
        stop_and_quit_frame.pack(pady=20)

        self.stop_button = Button(stop_and_quit_frame, text="Stop Sounds")
        self.stop_button.pack()
        self.quit_button = Button(stop_and_quit_frame, text="Quit")
        self.quit_button.pack()



