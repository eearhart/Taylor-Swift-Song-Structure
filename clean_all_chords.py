#I cleaned the CSV files I generated using VS Code extension "Data Wrangler"

import pandas as pd

def clean_data(df): 
    def change():
        df.astype({'Album': 'string'})
        df.astype({'Track': 'string'})
        df.change
    # Change column type to object for column: 'Album'
    df = df.astype({'Album': 'string'})
    # Change column type to object for column: 'Track'
    df = df.astype({'Track': 'string'})
    # Change column type to object for column: 'Writer(s)'
    df = df.astype({'Writer(s)': 'string'})
    # Replace all instances of "" with "" in column: 'Writer(s)'
    df['Writer(s)'] = df['Writer(s)'].str.replace("Writer/s:", "", case=False, regex=False)
    # Replace all instances of "" with "" in column: 'Capo'
    df['Capo'] = df['Capo'].str.replace("NO CAPO", "0", case=False, regex=False)
    # Replace all instances of "" with "" in column: 'Capo'
    df['Capo'] = df['Capo'].str.replace("CAPO", "", case=False, regex=False)
    # Replace all instances of "" with "" in column: 'Capo'
    df['Capo'] = df['Capo'].str.replace(":", "", case=False, regex=False)
    # Sort by column: 'Capo' (ascending)
    df = df.sort_values(['Capo'], na_position='first')
    for col in df:
        print(df['Capo'].unique())
    # Replace all instances of "" with "" in column: 'Capo'
    df['Capo'] = df['Capo'].str.replace("0G", "0", case=False, regex=False)
    # Change column type to object for column: 'Capo'
    df = df.astype({'Capo': 'string'})
    # Replace missing values with "" in column: 'Capo'
    df = df.fillna({'Capo': "0"})
    # Replace missing values with "" in column: 'Capo'
    df = df.fillna({'Capo': "0"})
    # Remove leading and trailing whitespace in column: 'Capo'
    df['Capo'] = df['Capo'].str.strip()
    # Replace missing values with "" in column: 'Capo'
    df = df.fillna({'Capo': "0"})
    # Convert text to uppercase in column: 'Capo'
    df['Capo'] = df['Capo'].str.upper()
    # Replace all instances of "" with "" in column: 'Capo'
    df['Capo'] = df['Capo'].str.replace("", "x", case=False, regex=False)
    # Replace all instances of "" with "" in column: 'Capo'
    df['Capo'] = df['Capo'].str.replace("x", " ", case=False, regex=False)
    # Replace all instances of "" with "" in column: 'Capo'
    df['Capo'] = df['Capo'].str.replace(" ", "0", case=False, regex=False)
    # Replace all instances of "" with "" in column: 'Capo'
    df['Capo'] = df['Capo'].str.replace("010", "1", case=False, regex=False)
    # Replace all instances of "" with "" in column: 'Capo'
    df['Capo'] = df['Capo'].str.replace("020", "2", case=False, regex=False)
    # Replace all instances of "" with "" in column: 'Capo'
    df['Capo'] = df['Capo'].str.replace("030", "3", case=False, regex=False)
    distinct_values = df['Capo'].unique()
    # Print distinct values
    print("Distinct values in column 'Capo':")
    print(distinct_values)
    # Replace all instances of "000" with "0" in column: 'Capo'
    df.loc[df['Capo'].str.lower() == "000".lower(), 'Capo'] = "0"
    # Replace all instances of "" with "" in column: 'Capo'
    df['Capo'] = df['Capo'].str.replace("040", "4", case=False, regex=False)
    # Change column type to object for column: 'Capo'
    df = df.astype({'Capo': 'int'})
    # Change column type to object for column: 'Intro_Chords'
    df = df.astype({'Intro_Chords': 'string'})
    # Change column type to object for column: 'Verse_Chords'
    df = df.astype({'Verse_Chords': 'string'})
    # Change column type to object for column: 'Verse_Lyrics'
    df = df.astype({'Verse_Lyrics': 'string'})
    # Change column type to object for columns: 'Pre_Chorus_Chords', 'Pre-Chorus_Lyrics' and 2 other columns
    df = df.astype({'Pre_Chorus_Chords': 'string', 'Pre-Chorus_Lyrics': 'string', 'Chorus_Chords': 'string', 'Chorus_Lyrics': 'string', 'Post_Chorus_Chords': 'string', 'Post_Chorus_Lyrics': 'string', 'Bridge_Chords': 'string', 'Bridge_Lyrics': 'string', 'Outro_Chords': 'string', 'Outro_Lyrics': 'string'})
    # Sort by column: 'PreChorus_Lyrics' (descending)
    df = df.sort_values(['PreChorus_Lyrics'], ascending=[False])
    # Drop column: 'PreChorus_Lyrics'
    df = df.drop(columns=['PreChorus_Lyrics'])
    # Replace all instances of "" with "" in column: 'Multi-Verse'
    df['Multi-Verse'] = df['Multi-Verse'].str.replace("N", "", case=False, regex=False)
    # Change column type to object for column: 'Multi-Verse'
    df = df.astype({'Multi-Verse': 'bool'})
    # Replace all instances of "" with "" in column: 'Multi-Bridge'
    df['Multi-Bridge'] = df['Multi-Bridge'].str.replace("N", "", case=False, regex=False)
    # Change column type to object for column: 'Multi-Bridge'
    df = df.astype({'Multi-Bridge': 'bool'})
    # Replace all instances of "" with "" in column: 'Outro_Chords'
    df['Outro_Chords'] = df['Outro_Chords'].str.replace("]", "", case=False, regex=False)
    # Replace all instances of "" with "" in column: 'Outro_Chords'
    df['Outro_Chords'] = df['Outro_Chords'].str.replace(".", "", case=False, regex=False)
    # Replace all instances of "" with "" in column: 'Track'
    df['Track'] = df['Track'].str.replace(".", "", case=False, regex=False)
    # Capitalize the first character in column: 'Track'
    df['Track'] = df['Track'].str.title()
    # Replace all instances of 0 with 0 in column: 'Capo'
    df.loc[df['Capo'] == 50, 'Capo'] = 5
    # Sort by column: 'Album' (ascending)
    df = df.sort_values(['Album'])
    # Remove leading and trailing whitespace in columns: 'Track', 'Writer(s)' and 7 other columns
    df['Track'] = df['Track'].str.strip()
    df['Writer(s)'] = df['Writer(s)'].str.strip()
    df['Intro_Chords'] = df['Intro_Chords'].str.strip()
    df['Verse_Chords'] = df['Verse_Chords'].str.strip()
    df['Pre_Chorus_Chords'] = df['Pre_Chorus_Chords'].str.strip()
    df['Chorus_Chords'] = df['Chorus_Chords'].str.strip()
    df['Post_Chorus_Chords'] = df['Post_Chorus_Chords'].str.strip()
    df['Bridge_Chords'] = df['Bridge_Chords'].str.strip()
    df['Outro_Chords'] = df['Outro_Chords'].str.strip()
    # Remove leading and trailing whitespace in columns: 'Track', 'Writer(s)' and 7 other columns
    df['Track'] = df['Track'].str.strip()
    df['Writer(s)'] = df['Writer(s)'].str.strip()
    df['Verse_Lyrics'] = df['Verse_Lyrics'].str.strip()
    df['Pre-Chorus_Lyrics'] = df['Pre-Chorus_Lyrics'].str.strip()
    df['Chorus_Lyrics'] = df['Chorus_Lyrics'].str.strip()
    df['Post_Chorus_Lyrics'] = df['Post_Chorus_Lyrics'].str.strip()
    df['Bridge_Lyrics'] = df['Bridge_Lyrics'].str.strip()
    df['Outro_Lyrics'] = df['Outro_Lyrics'].str.strip()
    df['Album'] = df['Album'].str.strip()
    return df

# Loaded variable 'df' from URI: /Users/eearhart/TSWIFT_PROJECT/ALL_ALBUMS_CHORDS.csv
df = pd.read_csv(r'/Users/eearhart/TSWIFT_PROJECT/ALL_ALBUMS_CHORDS.csv')

df_clean = clean_data(df.copy())
df_clean.head()