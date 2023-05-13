from tkinter import *
import soundboard


class GUI:
    def __init__(self, window):
        self.window = window
        self.sound_player = soundboard.SoundBoard()

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

        self.button1 = Button(sound_column1, text="Sound 1", command=lambda: self.play_sound('Sound 1'))
        self.button2 = Button(sound_column1, text="Sound 3", command=lambda: self.play_sound('Sound 3'))
        self.button3 = Button(sound_column1, text="Sound 5", command=lambda: self.play_sound('Sound 5'))

        self.button1.pack(pady=10)
        self.button2.pack(pady=10)
        self.button3.pack(pady=10)

        sound_column2 = Frame(sound_frame)
        sound_column2.pack(side=LEFT, padx=10)

        self.button4 = Button(sound_column2, text="Sound 2", command=lambda: self.play_sound('Sound 2'))
        self.button5 = Button(sound_column2, text="Sound 4", command=lambda: self.play_sound('Sound 4'))
        self.button6 = Button(sound_column2, text="Sound 6", command=lambda: self.play_sound('Sound 6'))

        self.button4.pack(pady=10)
        self.button5.pack(pady=10)
        self.button6.pack(pady=10)

        stop_frame = Frame(self.window)
        stop_frame.pack(pady=20)

        self.stop_button = Button(stop_frame, text="Stop Sounds", command=lambda: self.stop_sounds())
        self.stop_button.pack()

        quit_frame = Frame(self.window)
        quit_frame.pack(pady=20)
        self.quit_button = Button(quit_frame, text="Quit", command=lambda: self.window.destroy())
        self.quit_button.pack()

    def play_sound(self, sound_name: str):
        """
        Method to call play_sound from soundboard.py for playing sound based on button clicked
        :param sound_name: sound file to be played
        :return: sound file to be played and volume % to be played at
        """
        self.stop_sounds()

        volume = self.volume_slider.get() / 100
        self.sound_player.play_sound(sound_name, volume)

    def stop_sounds(self):
        """
        Method to call stop_sounds from soundboard.py which stops all currently playing sounds
        """
        self.sound_player.stop_sounds()


