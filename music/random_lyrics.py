c = l.random_chorus()

chords = [keys for keys in s.is_pop()]

for i in l.random_verse():
    r = random.randrange(0, len(chords))
    print(chords[r])
    print(i)

print("\n")

for i in c:
    print(chords[0], chords[1], chords[2], chords[3])
    print(i)

print("\n")
    
for i in l.random_verse():
    r = random.randrange(0, len(chords))
    print(chords[r])
    print(i)
    
print("\n")

for i in c:
    print(i)