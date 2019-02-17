import time
import rtmidi
from rtmidi.midiconstants import NOTE_OFF, NOTE_ON

midiout = rtmidi.MidiOut()
available_ports = midiout.get_ports()
print(available_ports)

if available_ports:
    print('did this')
    midiout.open_port(0)
else:
    print('no did this')
    midiout.open_virtual_port("My virtual output")


c = [0x90, 60, 112] # channel 1, middle C, velocity 112
d = [0x90, 62, 112]
e = [0x90, 64, 112]
f = [0x90, 65, 112]
g = [0x90, 67, 112]
a = [0x90, 69, 112]


chord1 = [c, e, g]
chord4 = [f, a, c]
chord5 = [g, c, d]

def play_chord(chord):
    for notes in chord:
        midiout.send_message(notes)
        # time.sleep plays the notes individually
        #time.sleep(0.5)
        notes[0], notes[2] = NOTE_OFF, 0
        midiout.send_message(notes)
    return True

def play_notes():
    midiout.send_message([0x90, 60, 112])
    midiout.send_message([0x90, 64, 112])
    midiout.send_message([0x90, 67, 112])

for _ in range(8):
    play_chord(chord1)
def num_times(count):
    for times in range(count):
        play_chord(chord1)
        time.sleep(0.5)
        play_chord(chord4)

#play_chord(chord1)
del midiout