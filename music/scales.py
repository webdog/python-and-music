from .notes import Notes

class MajorScale(Notes):
    valid_keys = ["A", "B", "C", "D", "E", "F", "G"]
    
    def __init__(self, scale_key):
        self.scale_key = scale_key

    def ionian(self):
        tones = (1, 1, 0.5, 1, 1, 0.5)
    
    def dorian(self):
        pass

    def phrygian(self):
        pass

    def lydian(self):
        pass

    def mixolydian(self):
        pass

    def aeolian(self):
        pass

    def locrian(self):
        pass

    

        