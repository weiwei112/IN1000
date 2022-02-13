#Skriv et program som ber brukeren om å svare “ja” eller “nei” på om de kunne tenke seg en brus. Lagre svaret i en variabel.
import sys
#input from users
brus = input("Vil du har en brus?")

#if input is ja, print "Her har du en brus!"
if brus == "ja":
    print("Her har du en brus!")
#if input is nei, print Den er grei.
elif brus == "nei":
    print("Den er grei.")
#if not ja and nei , print "Det forstod jeg ikke helt."
else:
    print("Det forstod jeg ikke helt.")




