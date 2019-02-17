import random

class Notes(object):
    notes = ["C","C#/Db","D","D#/Eb","E","F","F#/Gb","G","G#/Ab","A","A#/Bb","B"]

    def calculate_total_notes(self):
        return len(self.notes)

class Music(Notes):
    def __init__(self, scale):
        self.scale = scale

    def __str__(self):
        return f'Class for the {self.scale} scale. Also has these notes from the chromatic scale: {self.notes}'

    def __repr__(self):
        return f'<Music for the {self.scale}>'

    def major(self):
        if self.scale == "major":
            scale_list = []
            for note in self.notes:
                if "/" in note:
                    pass
                else:
                    scale_list.append(note)
            return scale_list
        else:
            return None

class Song(Music):
    def __init__(self, progression):
        self.progression = progression
    
    def is_pop(self):
        if self.progression == "pop":
            notes = self.major()
            prog_dict = {}
            for note in notes:
                if note == "C":
                    prog_dict["CMaj"] = 1
                elif note == "F":
                    prog_dict["FMaj"] = 4
                elif note == "G":
                    prog_dict["GMaj"] == 5
                elif note == "A":
                    prog_dict["Amin"] == 6
                else:
                    pass
            return prog_dict
        else:
            return None

class Lyrics(object):
    adjective = ["everyday", "sometimes", "occasionally", "significantly", "excited"]
    verbs = ["excuse", "absorb", "kiss", "drop", "isolate", "fling"]
    nouns = ["head", "heart", "skin", "air", "chair", "carpet"]
    adverbs = ["dutifully", "crazily", "realistically", "heartfully", "foolishly"]
    contractions = ["don't", "can't", "won't", "hasn't", "must've"]
    identifier = ["I", "She", "He", "They", "We"]

    def random_verse(self, bars=8):
        verses = []
        for i in range(bars):
            random_num = random.randrange(0, len(self.adjective))
            rand_verse = self.identifier[random_num] + ' ' + self.contractions[random_num] + ' ' + self.adverbs[random_num] +' ' + self.nouns[random_num] + ' ' + self.verbs[random_num] + ' ' + self.adjective[random_num]
            verses.append(rand_verse)
        return verses


    def random_chorus(self, bars=4): 
        random_num = random.randrange(0, len(self.adjective))
        chorus = self.identifier[random_num] + ' ' + self.contractions[random_num] + ' ' + self.adverbs[random_num] +' ' + self.nouns[random_num] + ' ' + self.verbs[random_num] + ' ' + self.adjective[random_num] 
        rand_chorus = []
        for i in range(bars):
            rand_chorus.append(chorus)
        return rand_chorus
 


                    

            
