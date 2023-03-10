# ELE130 2023
# Per Jotun
# Versjon 1
# 26. januar 2023
#
# Hente ut grupper og namn frå LaTeX-fil
# Skrive ut til ei CSV-fil

# For å kunna lesa filnamnet som parameter
import sys
# Må bruke biblioteket pathlib
import pathlib as pl
# For å få datoen i dag
from datetime import date
dato = date.today()
idag = dato.strftime("%Y.%m.%d")
#filInn = "ele130_20230131.tex"
# https://askubuntu.com/questions/1059579/input-the-filename-in-the-commandline-as-an-argument-in-python
filInn = sys.argv[1]
mappe = pl.Path.cwd()
# Berre ein test
#print(mappe)
#print(mappe.resolve())
# https://www.delftstack.com/howto/python/python-get-path/ og
# https://realpython.com/python-pathlib/
p = pl.Path(__file__).parent.absolute() / filInn
#print(p)
gr_nr = 0
stud_nr = 0
gruppe_snr = 2300
csv_streng = ""
csv_tittel = "ELE130 2023 Grupper i LEGO-prosjektet"
csv_topp = "Gruppe,Gr.str.,Studnr.,Førenamn,Etternamn,Studie,Status"
print(csv_tittel)
print(idag)
print(csv_topp)
# Eit standard oppsett med try - except blir da slik:
try:
    with p.open(mode="r") as fi:
        # Les gjennom fila line for line
        for line in fi:
            # Kode som gjer noko med innhaldet i fila
            # Her skriv berre ut at fila line for line
            #print(line)
            gruppe = line.find("Gruppe")
            tal = line.find("Tal:")
            student = line.find("student")
            #print(gruppe)
            #print(student)
            if gruppe == 4:
                gr_nr += 1
                #print(f"Gruppenummeret er: {gr_nr}")
            if tal == 6:
                line = line.replace("\n", "")
                gr_str = line[tal+4:]
            if student == 5:
                stud_nr += 1
                #print(f"Studentnummeret er: {stud_nr}")
                csv_streng = str(gruppe_snr+gr_nr) + "," + gr_str + ","
                #print(csv_streng)
                csv_streng = csv_streng + str(stud_nr)+","
                #print(csv_streng)
                namn_slutt = line.find("hline")
                #print(namn_slutt)
                #print(line[student+10:namn_slutt-4])
                namn_studie = line[student+10:namn_slutt-4]
                namn_studie = namn_studie.replace(", ", ",")
                #print(namn_studie)
                namn_studie = namn_studie.split(",")
                # Finn mellomrommet før etternamnet
                siste_mrom = namn_studie[0].rindex(" ")
                # Namnet
                #print(namn_studie[0])
                #print(siste_mrom)
                # Studie
                #print(f"Studie: {namn_studie[1]}")
                #if len(namn_studie) == 3:
                #    print(f"Status: {namn_studie[2]}")
                # Erstattar mellomrommet med komma
                # https://favtutor.com/blogs/replace-character-string-python
                # str = str[:index] + new_character + str[index+1:]
                namn = namn_studie[0][:siste_mrom] + "," + namn_studie[0][siste_mrom+1:]
                #print(namn)
                namn = namn.split(",")
                # Førenamn
                #print(namn[0])
                # Etternamn
                #print(namn[1])
                # Skriv ut all informasjon som CSV-fil, line for line
                csv_streng = csv_streng + namn[0] + "," + namn[1] + "," + namn_studie[1] + ","
                if len(namn_studie) == 3:
                    csv_streng = csv_streng + namn_studie[2]
                else:
                    csv_streng = csv_streng + ","
                print(csv_streng)

    fi.close()
except IOError as e:
    print("Feil med lesing/skriving av fil" +str(e))
