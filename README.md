# Taylor Swift Song Structure Analysis
This repository is the home for an ongoing data analysis project I am working on studying the song structure, patterns, formulas, and techniques used by Taylor Swift to create those "raging bops" (official terminology.) 

The goal of this project is to figure out the magic behind Ms. Swift's tunes, of course, but mostly I'm using it to learn and practice core data analysis skills and programs like spreadsheets, SQL, and Tableau, as well as python, relational database management, machine learning, and community contribution sites like kaggle and (obviously) github.  

Final Note: this is the first coding I've done without guidance from any number of youtube video bootcamps.  

## What's What (table of contents) 
Code:
"scrape_all_albums.py" - The python script that I wrote to scrape the song data from ultimate-guitar.com. 
"clean_all_chords.py" - I used the VSCode extension Data Wrangler to clean up the CSV file, this is the resulting code.
"transpose_chords.py" - The python script that I wrote to transpose all of the chords based on the capo # indicated. 

CSV's:
"scraped_chords_all_albums.csv" 
    Columns:
        album
        song_title
        writers
        capo
        intro_chords
        verse_chords
        verse_lyrics*
        pre_chorus_chords
        pre_chorus_lyrics*
        chorus_chords
        chorus_lyrics*
        post_chorus_chords
        post_chorus_lyrics*
        bridge_lyrics*
        bridge_chorus
        outro_chords
        outro_lyrics*
        multi_bridge**
        multi_chorus***
        common_id****
*The "lyrics" are short fragments meant to be used for reference only, not entire songs.
**Multiple Verses indicates whether a song has 3 or more verses
***Multiple Bridges indicates whether it has 2 or more bridges
**** This is a key column. I used python to extract a core title and create a common ID for each song so that I could reference the data across multiple tables. This common_ID will match the more stripped down & simplified chords_transposed table.

"all_chords_transposed.csv" 
    Columns: same as above with the addition of: 
        core_title
        intro_chords(transposed)
        verse_chords(transposed)
        pre_chorus_chords(transposed)
        chorus_chords(transposed)
        post_chorus_chords(transposed)
        bridge_chords(transposed)
        outro_chords(transposed)
        
"all_progressions_transposed-Table 1.csv"
    Columns: *
        album
        song title
        intro_chords(transposed)
        verse_chords(transposed)
        pre_chorus_chords(transposed)
        chorus_chords(transposed)
        post_chorus_chords(transposed)
        bridge_chords(transposed)
        outro_chords(transposed)
        multi_verse
        multi_bridge
        core_title
        common_id
*this is a condensed version of the all_chords_transposed csv, including only the chords themselves without reference lyrics
  
  "simplified_progressions_transposed-Table 1.csv"
    Columns: *
        album
        song title
        intro_chords(transposed)
        verse_chords(transposed)
        pre_chorus_chords(transposed)
        chorus_chords(transposed)
        post_chorus_chords(transposed)
        bridge_chords(transposed)
        outro_chords(transposed)
        multi_verse
        multi_bridge
        core_title
        common_id
*similar to all_progressions_transposed.csv, however this version simplifies the chord progressions into their 4 most distinct chords. For example, "D-D-C-G-D-Em" would appear only as "D-C-G-Em" to make identifying patterns in keys and chord usage easier. 
