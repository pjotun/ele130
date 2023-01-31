# ELE130

Dette git-prosjektet er for å ha versjonskontroll av Python-skript for å trekkje ut innformasjonen i LaTeX-fila (*.tex*) med oversikt over gruppene og gruppemedlemmene i LEGO-prosjektet i andre semesteret (vårsemesteret) på IDE i faget ELE130 *Anvendt matematikk og fysikk i robotprogrammering*. Faget er ein del av studieplanen for data, elektro S-veg, elektro Y-veg og medtek.

Python-skriptet trekkjer ut informasjonen og lagar ei CSV-fil som kan hentast inn i Excel eller andre rekneark. Informasjonen i LaTeX-fila er formatert på følgjande måte:

```latex
\begin{table}[H]
  \centering
  \begin{tabular}{|p{2.5cm}|p{7cm}|}\hline
    Gruppe \gruppe & Navn \\\hline\hline
    \student & Kari Jensen, S‐vei1, full jobb \\\hline
    \student & Kari Helene Jensen, enkeltemne \\\hline
  \end{tabular}
\end{table}
```

I fyrste omgang byggjer eg opp eller samlar Python-kode for å gjera føgjande:

1. Lest inn LaTeX-fila (*.tex*)
2. Listar ut fila line for line
3. Går vidare med å søkje opp ```Gruppe```
   1. Teljar for kor mange
4. Søkjer opp ```student```
   1. Teljar for kor mange
   2. Finn ```hline``` etter ```student``` for å finne indeksane for start og slutt på namn og studie mm.
   3. Ertstattar ```, ``` med ```,``` og splittar mellom namn og studie.
5. Ynskjer å dele namnet i førenamn og etternamn
   1. Kan bruke ```rindex``` for å finne siste *mellomrommet* i namnet
   2. Erstatte *mellomrommet* med *komma* for splitte namnet i førenamn og etternamn
6. La til kode for å hente ut *status* (element nr. 3 etter studie)
   1. brukte ```if``` og ```len``` som vil vera 3 om status er med
   
Har nå kode som får tak i alle dei elemnta eg treng for CSV-fila, i tillegg teljar for gruppenummer og fortløpande studentnummer frå ***1*** som i den kompilerte Latex-fila.

Prøvde ut litt å sy saman ein CSV-streng, men må sjå på rekkjefølgja i koda og nummerering av gruppene, for å få ei line for kvar student og rett gruppenummer.

## 31. januar 2023

Har nå eit python-skript som fungerar, har lagt til slik at eg kan bruke LaTeX-fila som argument når eg kjører skriptet slik:

```bash
python3 ele130prosjektgrupper_v1.py ele130_20230131.tex
```
Skriptet er ikkje særleg robust enda og det krev strukturert formatering av LaTeX-fila. La bl.a. til ein kommentar i LaTeX-fila for kor mange det er i kvar gruppe, som blir henta inn som ei kolonne i CSV-fila. Målet vil er å la python-skriptet finne ut dette sjølv, men så langt er det enkalste måten å gjera det på slik.


*Per Jotun*  
*27. januar 2023*  
*31. januar 2023*
