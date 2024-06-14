#updated, more efficient code that handles all flats and sharps correctly

import pandas as pd

table = {
    'capo':[2],
    'Chords':['G-D-A-Bm-C#sus2-Eb-Ab-Ab7-Bbm']
}
df = pd.DataFrame(data=table)

natural_chords = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
chord_index = {chord: i for i, chord in enumerate(natural_chords)}

custom_transpositions = {
    ('F', 5): 'A#',
    ('F#', 5): 'B',
    ('Fm', 5): 'A#m',
    ('Gb', 5): 'B',
    ('G', 5): 'C',
    ('G#', 5): 'C#',
    ('Ab', 5): 'Db',
    ('F#m', 5): 'Bm',
    ('Gbm', 5): 'Bm',
    ('Gm', 5): 'Cm',
    ('G#m', 5): 'C#m',
    ('Abm', 5): 'C#m',
    ('Fadd9', 5): 'A#add9',
    ('F#add9', 5): 'Badd9',
    ('Gbadd9', 5): 'Badd9',
    ('Gadd9', 5): 'Cadd9',
    ('G#add9', 5): 'C#add9',
    ('Abadd9', 5): 'Dbadd9',
    ('F7', 5): 'A#7',
    ('F#7', 5): 'B7',
    ('Gb7',5): 'B7',
    ('G7', 5): 'C7',
    ('G#7', 5): 'C#7',
    ('Ab7', 5): 'Db7',
    ('Fm7', 5): 'A#m7',
    ('F#m7', 5): 'Bm7',
    ('Gbm7', 5): 'Bm7',
    ('Gm7', 5): 'Cm7',
    ('G#m7', 5): 'C#m7',
    ('Abm7', 5): 'Dbm7',
    ('Fsus2', 5): 'A#sus2',
    ('F#sus2', 5): 'Bsus2',
    ('Gbsus2', 5): 'Bsus2',
    ('Gsus2', 5): 'Csus2',
    ('G#sus2', 5): 'C#sus2',
    ('Absus2', 5): 'Dbsus2',
    ('Fsus4', 5): 'A#sus4',
    ('F#sus4', 5): 'Bsus4',
    ('Gbsus4', 5): 'Bsus4',
    ('Gsus4', 5): 'Csus4',
    ('G#sus4', 5): 'C#sus4',
    ('Absus4', 5): 'Dbsus4',
    ('F9', 5): 'A#9',
    ('F#9', 5): 'B9',
    ('Gb9', 5): 'B9',
    ('G9', 5): 'C9',
    ('G#9', 5): 'C#9',
    ('Ab9', 5): 'Db9',
    ('F', 4): 'A',
    ('F#',4): 'A#',
    ('Fm',4): 'Am',
    ('Gb', 4): 'Bb',
    ('G', 4): 'B',
    ('G#', 4): 'C',
    ('Ab', 4): 'C',
    ('F#m', 4): 'A#m',
    ('Gbm', 4): 'Bbm',
    ('Gm', 4): 'Bm',
    ('G#m', 4): 'Cm', 
    ('Abm', 4): 'Cm',
    ('Fadd9', 4): 'Aadd9',
    ('F#add9', 4): 'A#add9',
    ('Gbadd9', 4): 'Bbadd9',
    ('Gadd9', 4): 'Badd9',
    ('G#add9', 4): 'Cadd9',
    ('Abadd9', 4): 'Cadd9',
    ('F7', 4): 'A7',
    ('F#7', 4): 'A#7',
    ('Gb7',4): 'Bb7',
    ('G7', 4): 'B7',
    ('G#7', 4): 'C7',
    ('Ab7', 4): 'C7',
    ('Fm7', 4): 'Am7',
    ('F#m7',4): 'A#m7',
    ('Gbm7', 4): 'Bbm7',
    ('Gm7', 4): 'Bm7',
    ('G#m7', 4): 'Cm7',
    ('Abm7', 4): 'Cm7',
    ('Fsus2', 4): 'Asus2',
    ('F#sus2', 4): 'A#sus2',
    ('Gbsus2', 4): 'Bbsus2',
    ('Gsus2', 4): 'Bsus2',
    ('G#sus2', 4): 'Csus2',
    ('Absus2', 4): 'Csus2',
    ('Fsus4', 4): 'Asus4',
    ('F#sus4', 4): 'A#sus4',
    ('Gbsus4', 4): 'Bbsus4',
    ('Gsus4', 4): 'Bsus4',
    ('G#sus4', 4): 'Csus4',
    ('Absus4', 4): 'Csus4',
    ('F9', 4): 'A9',
    ('F#9', 4): 'A#9',
    ('Gb9', 4): 'Bb9',
    ('G9', 4): 'B9',
    ('G#9', 4): 'C9',
    ('Ab9', 4): 'C9',
    ('F', 3): 'Ab',
    ('F#',3): 'A',
    ('Fm',3): 'Abm',
    ('Gb', 3): 'A',
    ('G', 3): 'Bb',
    ('G#', 3): 'B',
    ('Ab', 3): 'B',
    ('F#m', 3): 'Am',
    ('Gbm', 3): 'Am',
    ('Gm', 3): 'Bbm',
    ('G#m', 3): 'Bm', 
    ('Abm', 3): 'Bm',
    ('Fadd9', 3): 'Bbadd9',
    ('F#add9', 3): 'Aadd9',
    ('Gbadd9', 3): 'Aadd9',
    ('Gadd9', 3): 'Bbadd9',
    ('G#add9', 3): 'Badd9',
    ('Abadd9', 3): 'Badd9', 
    ('F7', 3): 'Ab7',
    ('F#7', 3): 'A7',
    ('Gb7',3): 'A7',
    ('G7', 3): 'Bb7',
    ('G#7', 3): 'B7',
    ('Ab7', 3): 'B7',
    ('Fm7', 3): 'Bbm7',
    ('F#m7',3): 'Am7',
    ('Gbm7', 3): 'Am7',
    ('Gm7', 3): 'Bbm7',
    ('G#m7', 3): 'Bm7',
    ('Abm7', 3): 'Bm7',
    ('Fsus2', 3): 'Absus2',
    ('F#sus2', 3): 'Asus2',
    ('Gbsus2', 3): 'Asus2',
    ('Gsus2', 3): 'Bbsus2',
    ('G#sus2', 3): 'Bsus2',
    ('Absus2', 3): 'Bsus2',
    ('Fsus4', 3): 'Absus4',
    ('F#sus4', 3): 'Asus4',
    ('Gbsus4', 3): 'Asus4',
    ('Gsus4', 3): 'Bbsus4',
    ('G#sus4', 3): 'Bsus4',
    ('Absus4', 3): 'Bsus4',
    ('F9', 3): 'Ab9',
    ('F#9', 3): 'A9',
    ('Gb9', 3): 'A9',
    ('G9', 3): 'Bb9',
    ('G#9', 3): 'B9',
    ('Ab9', 3): 'B9',
    ('G', 2): 'A',
    ('G#', 2): 'A#',
    ('Ab', 2): 'Bb',
    ('Gm', 2): 'Am',
    ('G#m', 2): 'A#m', 
    ('Abm', 2): 'Bbm',
    ('Gadd9', 2): 'Aadd9',
    ('G#add9', 2): 'A#add9',
    ('Abadd9', 2): 'Bbadd9',
    ('G7', 2): 'A7',
    ('G#7', 2): 'A#7',
    ('Ab7', 2): 'Bb7',
    ('Gm7', 2): 'Am7',
    ('G#m7', 2): 'A#m7',
    ('Abm7', 2): 'Bbm7',
    ('Gsus2', 2): 'Asus2',
    ('G#sus2', 2): 'A#sus2',
    ('Absus2', 2): 'Bbsus2',
    ('Gsus4', 2): 'Asus4',
    ('G#sus4', 2): 'A#sus4',
    ('Absus4', 2): 'Bbsus4',
    ('G9', 2): 'A9',
    ('G#9', 2): 'A#9',
    ('Ab9', 2): 'Bb9',
    ('G#', 1): 'A',
    ('Ab', 1): 'A',
    ('G#m', 1): 'Am', 
    ('Abm', 1): 'Am',
    ('G#add9', 1): 'Aadd9',
    ('Abadd9', 1): 'Aadd9',
    ('G#7', 1): 'A7',
    ('Ab7', 1): 'A7',
    ('G#m7', 1): 'A7',
    ('Abm7', 1): 'A7',
    ('G#sus2', 1): 'Asus2',
    ('Absus2', 1): 'Asus2',
    ('G#sus4', 1): 'Asus4',
    ('Absus4', 1): 'Asus4',
    ('G#9', 1): 'A9',
    ('Ab9', 1): 'A9',
    }

#separate the root note 
def pull_root_and_type(chord): 
    for i in range(1, 4):
        possible_root = chord[:i]
        if possible_root in chord_index:
            return possible_root, chord[i:]
    return chord, ''

#the root will be transposed separately this treats all bs as sharps 
def handle_flats(chords): 
    handled_flats = []
    for chord in chords:
        chord.replace('b', '#')
    return handled_flats

def transpose_individual(chord, capo):
    if chord in ['N.C', 'NONE', 'CHORUS', 'BRIDGE']: #this is from the full CSV file I will transpose later
        return chord
    if chord in custom_transpositions:
        if capo in custom_transpositions[chord]:
            return custom_transpositions[chord][capo]
    
    root, type = pull_root_and_type(chord)

    root_index = chord_index[root]
    transposed_index = (root_index +capo) %len(natural_chords)
    transposed_chord = natural_chords[transposed_index]

    return transposed_chord + type
    
#this returns the original suffix to the root which sometimes includes b & #
#to avoid 'Eb' capo 2 returning as 'F#b' negate redundancies 

def redundancies(chord):
    return chord.replace('#b', '')

def transpose_chords(chords, capo):
    handled_flats = handle_flats(chords)
    transposed_chords = []
    for chord in chords:
        transposed_chords.append(redundancies(transpose_individual(chord, capo)))
    return transposed_chords

columns_to_transpose = ['Chords']

for column in columns_to_transpose:
    df[column + 'Transposed'] = df.apply(lambda row:'-'.join(transpose_chords(row[column].split('-'), row['capo'])), axis=1)

print(df)

#this returns    
#capo            Chords                 ChordsTransposed
#  2  G-D-A-Bm-C#sus2-Eb-Ab-Ab7-Bbm  A-E-B-C#m-D#sus2-F-Bb-Bb7-Cm
