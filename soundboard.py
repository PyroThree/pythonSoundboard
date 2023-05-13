import pygame.mixer


class SoundBoard:
    """
    Class for sound file objects
    """
    def __init__(self):
        """
        Ties strings to sound files
        """
        pygame.mixer.init()
        self.sounds = {
            "Sound 1": pygame.mixer.Sound("sound1.wav"),
            "Sound 2": pygame.mixer.Sound("sound2.wav"),
            "Sound 3": pygame.mixer.Sound("sound3.wav"),
            "Sound 4": pygame.mixer.Sound("sound4.wav"),
            "Sound 5": pygame.mixer.Sound("sound5.wav"),
            "Sound 6": pygame.mixer.Sound("sound6.wav"),
        }
        self.current_sound = None

    def play_sound(self, sound_name: str, volume: int):
        """
        Method that plays sound based on button clicked (name of button)
        :param sound_name: name of button that was clicked
        :param volume: integer value divided by 100 essentially for % volume to play sound at
        :return: sound
        """
        if self.current_sound:
            self.current_sound.stop()
        self.current_sound = self.sounds[sound_name]
        self.current_sound.set_volume(volume)
        self.current_sound.play()

    def stop_sounds(self):
        """
        Method to stop any currently playing sounds
        """
        if self.current_sound:
            self.current_sound.stop()
        self.current_sound = None
