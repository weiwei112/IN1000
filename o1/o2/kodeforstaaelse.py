#1 Vil dette programmet kjøre? Begrunn svaret.
#2 Hvilke problemer vil vi kunne møte på når vi kjører denne koden?

#answer: no,  print ( heltall + "Hei!" ) will have syntax fail.
# because The left and right sides of the plus sign must be of the same variable type
# and in this case, heltall is a int variable, Hei is a str variable


heltallSomTekst = input( "Tast inn et heltall! " )
heltall = int( heltallSomTekst )
if heltall < 10:
    print ( heltall + "Hei!" )
