import abjad

def tupletize_notes(voice, tuplet_values):
    # Detach notes only if they have a parent
    notes = []
    for note in voice:
        if note.parent is not None:  # Check if the note has a parent
            abjad.detach(note)  # Detach the note
        notes.append(note)  # Add the note to the list
    
    # Now create a tuplet with the detached notes
    tuplet = abjad.Tuplet(tuplet_values, notes)
    
    # Attach the tuplet to the voice
    abjad.attach(tuplet, voice)

# Example usage
voice_2 = abjad.Voice("d''16 a'16 g'16 f'16 c''16 g'16 f'16 ef'16 bf'16 f'16 ef'16 d'16 a'16 ef'16 d'16 c'16 c'16 d'16 ef'16 a'16 d'16 ef'16 f'16 bf'16 ef'16 f'16 g'16 c''16 f'16 g'16 a'16 d''16")

# Apply tupletization
tupletize_notes(voice_2, [3, 2, 5])

# Correctly save the output to a LilyPond file
abjad.persist.as_lilypond(voice_2, "output.ly")

print("Output saved to 'output.ly'.")
