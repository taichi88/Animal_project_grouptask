class SoundMixin:
    def make_sound(self, sound):
        return f"The  {self.__class__.__name__} Sound is '{sound}'"


