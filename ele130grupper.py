# ELE130 2024
# Per Jotun
# 10. februar 2024
# Program for å lage gruppeliste frå tex-fil
# Utgangspunkt i øving 10 - fil: oeving10v5.py
# og øving 7 - fil: oeving07_2v6.py

# Andre kjelder: https://discuss.python.org/t/how-to-count-the-number-of-times-specific-words-appear-in-a-text-file/19779/2

import pathlib as pl
# For å lage ordsky
# https://predictivehacks.com/?all-tips=how-to-create-word-clouds-from-dictionaries
import matplotlib.pyplot as plt
from wordcloud import WordCloud

from collections import defaultdict, OrderedDict
import re

# https://www.geeksforgeeks.org/python-ways-to-find-nth-occurrence-of-substring-in-a-string/
def finn_indeksnr(streng, teikn, plass):
    telje = streng.count(teikn)
    if telje < plass:
        return -1
    else:
        indeks = -1
        for i in range(plass):
            indeks = streng.find(teikn, indeks+1)
        return indeks

def finn_etternamn(streng, indeks):
    # Hentar ut heile namnet
    namn = streng[slice(0, indeks)]
    print(namn)
    # Finn alle mellomrom
    # https://www.delftstack.com/howto/python/python-find-all-occurrences-in-string/
    resultat = [_.start() for _ in re.finditer(" ", namn)]
    print(resultat)

tabelltopp = "\t\begin{table}[H]\n\t\t\centering\n\t\t\begin{tabular}{|p{2.5cm}|p{9cm}|p{2.1cm}|p{2.1cm}|}\hline\n\t\tGruppe \gruppe & Navn & LEGO ut & LEGO inn \\ \hline\hline\n"
tabellstorl = "\t\t% Tal:"
student = "\t\t\student & Berner Rotevatn Gilje, data & & \\ \hline % br.gilje@stud.uis.no"
tabellbotn = "\t\t\end{tabular}\n\t\end{table}\n\n"

md_topp = "---\ntitle: \"ELE130 2024\"\nformat:\n  pdf:\n    documentclass: article\n    classoption: [portrait]\n    lof: true\n    lot: true\n    geometry:\n      - top=20mm\n      - left=10mm\n      - heightrounded\n    fontfamily: libertinus\n    colorlinks: true\n---\n"

filliste = ["DAT120_2023_studieprogram_20240125.csv",
            "ele130_20240126_studentliste-studie.csv",
            "dat120_20230911_studentliste_ocr.txt-rensa.csv",
            "ele130grupper_liste.tex"]

filnummer = 3

if filnummer == 0:
    kolonne = 2 # Kolonne for studiekode DAT120
    studie = "DAT120 2023 25.01.2024"
elif filnummer == 1:
    kolonne = 1 # Kolonne for studiekode ELE130
    studie = "ELE130 2024 26.01.2024"
elif filnummer == 2:
    kolonne = 9 # Kolonne for studiekode ELE130
    studie = "DAT120 2023 11.9.2023"

filnamn_inn = filliste[filnummer]
filnamn_ut = filnamn_inn + "-grupper.csv"
filnamn_utmd = filnamn_inn + "-grupper.md"


# https://www.delftstack.com/howto/python/python-get-path/ og
# https://realpython.com/python-pathlib/
f_inn = pl.Path(__file__).parent.absolute() / filnamn_inn
f_ut =  pl.Path(__file__).parent.absolute() / filnamn_ut
f_umd =  pl.Path(__file__).parent.absolute() / filnamn_utmd

studenttal = defaultdict(int)
gruppenr = 2400
stud_tal = 0
try:
    with f_inn.open(mode="r", encoding="utf-8") as fi:
        with f_ut.open(mode="w") as fu:
            with f_umd.open(mode="w") as fumd:
                # Les gjennom fila line for line
                fu.write("\nELE130 2024 Gruppeinndeling\n\n")
                fumd.write(md_topp)
                fumd.write("# ELE130 2024 Gruppeinndeling\n")
                fu.write("Stud.tal,Gr.str.,Gruppenr.,Namn,Etternamn,Studie,Anna,E-post\n")
                # https://tabletomarkdown.com/convert-spreadsheet-to-markdown/
                fumd.write("| Gruppenr. | Namn                       | Etternamn       | Studie                                      | Anna      | E-post                        | LEGO ut  | LEGO inn |\n")
                fumd.write("| --------- | -------------------------- | --------------- | ------------------------------------------- | --------- | ----------------------------- |----------|----------|\n")
                for line in fi:
                    line = line.strip()
                    #print(line)
                    tal = line.startswith("% Tal:")
                    if tal == True:
                        gruppestr = int(line[6])
                        #print(gruppestr)
                        gruppenr = gruppenr + 1
                        #print(gruppenr)
                        #fu.write(str(gruppenr) + "\n")
                        #fu.write(str(gruppestr) + "\n")
                    stud = line.startswith("\student")
                    if stud == True:
                        stud_tal += 1
                        line = line.strip("\student & ")
                        # https://datagy.io/python-split-string-multiple-delimiters/
                        line = line.replace(", ", ",").replace("% ", ",").replace(" \\\\ \\hline ", "").replace(" \\\\\\hline ", "").replace(" \\\\ \\hli", "").replace(" \\\\\\hli", "")
                        #line = line.split(",")
                        #print(line)
                        komma = line.count(",")
                        #print(f"Komma: {komma}")
                        if komma == 1:
                            line = line + ",,"
                        elif komma == 2:
                            # https://datagy.io/python-find-index-substring/
                            plass = line.rindex(",")
                            #print(f"Plass: {plass}")
                            # https://www.geeksforgeeks.org/python-add-substring-at-specific-index/
                            line = line[:plass] + "," + line[plass:]
                        #print(line)
                        kommaind = finn_indeksnr(line, ",", 1)
                        #print(kommaind)
                        # Hentar ut heile namnet
                        namn = line[slice(0, kommaind)]
                        # Finn alle mellomrom
                        # https://www.delftstack.com/howto/python/python-find-all-occurrences-in-string/
                        # Finn siste mellomrommet i namnet
                        resultat = [_.start() for _ in re.finditer(" ", namn)]
                        # https://pythonexamples.org/python-string-replace-character-at-specific-position/
                        # Legg erstattar siste mellomrommet i namnet med komma (,)
                        line = line[:resultat[-1]] + "," + line[resultat[-1]+1:]
                        # Skriv ut resultatet til ei CSV-fil line for line
                        fu.write(str(stud_tal) + "," + str(gruppestr) + "," + str(gruppenr) + "," + line + "\n")
                        # Skriv ut som MARKdown-tabell
                        line = line.replace(",", "|")
                        fumd.write("|" + str(gruppenr) + "|" + line + "|\n")
except IOError as e:
    print("Feil med lesing/skriving av fil" +str(e))

print("Ferdig! ================================================================================")
#print(studenttal)

# if __name__ == "__main__":
#    filliste = [0, 1, 2]
#    for runde in filliste:
