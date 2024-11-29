import abjad

# Define the notes for "Silent Night"
notes = [
    'g\'4', 'g\'4', 'd\'4', 'e\'4', 'g\'4', 'g\'4', 'g\'4', 'd\'4',
    'g\'4', 'g\'4', 'g\'4', 'g\'4', 'e\'4', 'g\'4', 'g\'4', 'g\'4',
    'g\'4', 'e\'4', 'g\'4', 'g\'4', 'g\'4', 'd\'4', 'g\'4', 'g\'4',
    'd\'4', 'e\'4', 'g\'4', 'g\'4', 'g\'4', 'd\'4', 'g\'4', 'g\'4'
]

# Create notes as Abjad Note objects
abjad_notes = [abjad.Note(n) for n in notes]

# Create a container for the notes
container = abjad.Container(abjad_notes)

# Create a time signature
time_signature = abjad.TimeSignature((4, 4))

# Create a measure and attach the time signature
measure = abjad.Measure(time_signature, container)

# Create a staff for the voice, which contains the measure
staff = abjad.Staff([measure])

# Create a score (for one voice)
score = abjad.Score([staff])

# Persist the score as a LilyPond file
abjad.persist.as_lilypond(score, 'silent_night.ly')

# Output to confirm the file was saved
print("LilyPond file saved as 'silent_night.ly'.")
