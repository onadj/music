\version "2.24.2" % version of LilyPond
\header {
  title = "Silent Night"
  composer = "Traditional"
}

\score {
  \new Staff {
    \clef treble
    \time 4/4

    \relative c' {
      \key g \major

      g4  g  d'4  e'  g  g  g  g
      d'4  g  g  g  g  e'4  g  g
      g  g  g  g  e'4  g  g  g
      d'4  g  g  g  g  e'4  g  g
    }
  }
}
