import pandas as pd

#define all possible chords and non-chord values 
#for example, if the intro is really just the chorus, there will be no chords, just CHORUS

def transpose_chords(chords, capo):
    all_chords = ['A', 'A#', 'Bb', 'B', 'C', 'C#', 'Db', 'D', 'D#', 'Eb', 'E', 'F', 'F#', 'Gb', 'G', 'G#', 'Ab',
                'Am', 'A#m', 'Bbm', 'Bm', 'Cm', 'C#m', 'Dbm', 'Dm', 'D#m', 'Ebm', 'Em', 'Fm', 'F#m', 'Gbm', 'Gm', 'G#m', 'Abm',
                'Aadd9', 'A#add9', 'Bbadd9', 'Badd9', 'Cadd9', 'C#add9', 'Dbadd9', 'Dadd9', 'D#add9', 'Ebadd9', 'Eadd9', 'Fadd9', 'F#add9', 'Gbadd9', 'Gadd9', 'G#add9', 'Abadd9',
                'A7', 'A#7', 'Bb7', 'B7', 'C7', 'C#7', 'Db7', 'D7','D#7', 'Eb7', 'E7', 'F7', 'F#7', 'Gb7', 'G7', 'G#7', 'Ab7',
                'Am7', 'A#m7', 'Bbm7', 'Bm7', 'Cm7', 'C#m7', 'Dbm7','Dm7','D#m7', 'Ebm7', 'Em7', 'Fm7', 'F#m7', 'Gbm7', 'Gm7', 'G#m7', 'Abm7',
                'Asus2', 'A#sus2', 'Bbsus2', 'Bsus2', 'Csus2', 'C#sus2', 'Dbsus2', 'Dsus2', 'D#sus2', 'Ebsus2', 'Esus2', 'Fsus2', 'F#sus2', 'Gbsus2', 'Gsus2', 'G#sus2', 'Absus2',
                'Asus4', 'A#sus4', 'Bbsus4', 'Bsus4', 'Csus4', 'C#sus4', 'Dbsus4', 'Dsus4', 'D#sus4', 'Ebsus4', 'Esus4', 'Fsus4', 'F#sus4', 'Gbsus4', 'Gsus4', 'G#sus4', 'Absus4',
                'A9', 'A#9', 'Bb9', 'B9', 'C9', 'C#9', 'Db9', 'D9', 'D#9', 'Eb9', 'E9', 'F9', 'F#9', 'Gb9', 'G9', 'G#9', 'Ab9',
                'N.C','N.C','N.C','N.C','N.C','N.C','N.C','N.C','N.C','N.C','N.C','N.C','N.C','N.C','N.C','N.C','N.C',
                'NONE','NONE','NONE','NONE','NONE','NONE','NONE','NONE','NONE','NONE','NONE','NONE','NONE','NONE','NONE','NONE','NONE',
                'CHORUS','CHORUS','CHORUS','CHORUS','CHORUS','CHORUS','CHORUS','CHORUS','CHORUS','CHORUS','CHORUS','CHORUS','CHORUS','CHORUS','CHORUS','CHORUS','CHORUS','CHORUS',
                'BRIDGE', 'BRIDGE', 'BRIDGE', 'BRIDGE', 'BRIDGE', 'BRIDGE', 'BRIDGE', 'BRIDGE', 'BRIDGE', 'BRIDGE', 'BRIDGE', 'BRIDGE', 'BRIDGE', 'BRIDGE', 'BRIDGE', 'BRIDGE']

#in order to prevent G with capo 5 from transposing to A#m I added custom transpositions for the last 6 chords of each line up to capo 5

    chord_index = {chord: i for i, chord in enumerate(all_chords)}
    custom_transpositions = {
        ('F', 5): 'A#',
        ('F#',5): 'B',
        ('Fm',5): 'A#m',
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
        ('F#m7',5): 'Bm7',
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

#since G# and Ab are different notation of the same chord, clarify all same chord instances

same_chords_indices = {
        chord_index['A#'] : chord_index['Bb'],
        chord_index['C#'] : chord_index['Db'],
        chord_index['D#'] : chord_index['Eb'],
        chord_index['F#'] : chord_index['Gb'],
        chord_index['G#'] : chord_index['Ab'],
        chord_index['A#m'] : chord_index['Bbm'],
        chord_index['C#m'] : chord_index['Dbm'],
        chord_index['F#m'] : chord_index['Gbm'],
        chord_index['G#m'] : chord_index['Abm'],
        chord_index['A#add9'] : chord_index['Bbadd9'],
        chord_index['C#add9'] : chord_index['Dbadd9'],
        chord_index['D#add9'] : chord_index['Ebadd9'],
        chord_index['F#add9'] : chord_index['Ebadd9'],
        chord_index['G#add9'] : chord_index['Abadd9'],
        chord_index['A#7'] : chord_index['Bb7'],
        chord_index['C#7'] : chord_index['Db7'],
        chord_index['D#7'] : chord_index['Eb7'],
        chord_index['F#7'] : chord_index['Gb7'],
        chord_index['G#7'] : chord_index['Ab7'],
        chord_index['A#m7'] : chord_index['Bbm7'],
        chord_index['C#m7'] : chord_index['Dbm7'],
        chord_index['D#m7'] : chord_index['Ebm7'],
        chord_index['F#m7'] : chord_index['Gbm7'],
        chord_index['G#m7'] : chord_index['Abm7'],
        chord_index['A#sus2'] : chord_index['Bbsus2'],
        chord_index['C#sus2'] : chord_index['Dbsus2'],
        chord_index['D#sus2'] : chord_index['Ebsus2'],
        chord_index['F#sus2'] : chord_index['Gbsus2'],
        chord_index['G#sus2'] : chord_index['Absus2'],
        chord_index['A#sus4'] : chord_index['Bbsus4'],
        chord_index['C#sus4'] : chord_index['Dbsus4'],
        chord_index['D#sus4'] : chord_index['Ebsus4'],
        chord_index['F#sus4'] : chord_index['Gbsus4'],
        chord_index['G#sus4'] : chord_index['Absus4'],
        chord_index['A#9'] : chord_index['Bb9'],
        chord_index['C#9'] : chord_index['Db9'],
        chord_index['D#9'] : chord_index['Eb9'],
        chord_index['F#9'] : chord_index['Gb9'],
        chord_index['G#9'] : chord_index['Ab9'],
    }

 #transpose chords
   
 transposed_chords = []

    for chord in chords:
        if chord == 'N.C' or chord == 'NONE' or chord == 'CHORUS' or chord == 'BRIDGE':
            transposed_chords.append(chord)
            continue

        root_note = chord[:-1]  # Extract the root note
        chord_type = chord[-1]  # Extract the chord type

        # The capo position is an integer from 0-5, so first transpose the chord based on the capo position in customer_transpositions
        transposed_root = custom_transpositions.get((root_note, capo), root_note)
        transposed_chord = transposed_root + chord_type

        # If the chord is not one of the custom_transpositions, use regular all_chords transpositions
        if transposed_chord not in all_chords:
            transposed_index = (chord_index[transposed_root] + capo) % len(all_chords)
            transposed_chord = all_chords[transposed_index] + chord_type

        # Check if the chord index needs to be replaced with a different index for same_chord equivalents
        if chord_index.get(transposed_chord) in same_chords_indices:
            transposed_chord = all_chords[same_chords_indices[chord_index[transposed_chord]]] + chord_type

        transposed_chords.append(transposed_chord)

    return transposed_chords

#indicate the csv to transpose
df=pd.read_csv('ts_all_albums_chords.csv') 

# Read the CSV file and indicate the relevent columns to be transposed
columns_to_transpose = ['intro_chords', 'verse_chords', 'pre_chorus_chords', 'chorus_chords', 'post_chorus_chords', 'bridge_chords', 'outro_chords']  # Modify as needed

# Iterate over each column and transpose chords based on capo number found in the 'capo' column
for column in columns_to_transpose:
    df[column + ' (Transposed)'] = df.apply(lambda row: ' '.join(transpose_chords(row[column].split('-'), row['capo'])), axis=1)

# Save the updated DataFrame to a new CSV file
df.to_csv('ts_all_albums_transposed.csv', index=False)

print("Transposed chord progressions saved to transposed_all.csv")

