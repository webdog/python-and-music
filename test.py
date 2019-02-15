import time
import rtmidi

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
e = [0x90, 64, 112]
g = [0x90, 67, 112]
bmaj7 = [0x90, 71, 112] 

chord = (c, e, g)

for iterable in chord:
    midiout.send_message(iterable)


#midiout.send_message(chord)
#time.sleep(0.25)
#midiout.send_message(e)
#time.sleep(0.25)
#midiout.send_message(g)

del midiout