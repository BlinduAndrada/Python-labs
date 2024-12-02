def compose(notes, moves, start):
    song = []
    song.append(notes[start])
    for i in moves:
        if start+i<len(notes):
            start=start+i
        else:
            start=start+i-len(notes)
        song.append(notes[start])
    return song




notes = ["do", "re", "mi", "fa", "sol"]
moves = [1, -3, 4, 2]
start = 2
print(compose(notes, moves, start))

# ["mi", "fa", "do", "sol", "re"]
