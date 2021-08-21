from math import cos


class Weld:

    def __init__(self, Length, Thickness, Weld_Leg_Height_Horizontal, Weld_Leg_Height_Vertical, Penetration_Depth,
                 Angle):
        self.Length = Length
        self.t = Thickness
        self.r = Weld_Leg_Height_Horizontal
        self.h = Weld_Leg_Height_Vertical
        self.s = Penetration_Depth
        self.ALPHA = Angle

    @property
    def t(self):
        return self.__t

    @t.setter
    def t(self, val):
        if type(val) is float and val > 0:
            self.__t = val
        else:
            raise TypeError

    @property
    def s(self):
        return self._s

    @s.setter
    def s(self, val):
        raise NotImplementedError

    @property
    def weldthroatthickness(self):
        raise NotImplementedError

    @property
    def ALPHA(self):
        return self._alpha

    @ALPHA.setter
    def ALPHA(self, val):
        raise NotImplementedError


class WeldDoubleFillet(Weld):

    @property
    def ALPHA(self):
        return self._alpha

    @ALPHA.setter
    def ALPHA(self, val):
        self._alpha = 45

    @property
    def s(self):
        return self._s

    @s.setter
    def s(self, val):
        self._s = 0

    @property
    def weldthroatthickness(self):
        return self.r * cos(self.ALPHA)


class WeldPartialPenetration(Weld):
    @property
    def ALPHA(self):
        return self._alpha

    @ALPHA.setter
    def ALPHA(self, val):
        self._alpha = 0

    @property
    def s(self):
        return self.t / 2

    @s.setter
    def s(self, val):
        self.t = val * 2


class WeldFullPenetration(Weld):
    @property
    def ALPHA(self):
        return self._alpha

    @ALPHA.setter
    def ALPHA(self, val):
        if 0 <= val <= 360:
            self._alpha = val
        else:
            raise ValueError
