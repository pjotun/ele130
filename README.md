# ELE130

Dette git-prosjektet er for å ha versjonskontroll av Python-skript for å trekkje ut innformasjonen i LaTeX-fila (*.tex*) med oversikt over gruppene og gruppemedlemmene i LEGO-prosjektet i andre semesteret (vårsemesteret) på IDE i faget ELE130 *Anvendt matematikk og fysikk i robotprogrammering*. Faget er ein del av studieplanen for data, elektro S-veg, elektro Y-veg og medtek.

Python-skriptet trekkjer ut informasjonen og lagar ei CSV-fil som kan hentast inn i Excel eller andre rekneark. Informasjonen i LaTeX-fila er formatert på følgjande måte:

```latex
\begin{table}[H]
  \centering
  \begin{tabular}{|p{2.5cm}|p{7cm}|}\hline
    Gruppe \gruppe & Navn \\\hline\hline
    \student & Per Olsen, Y‐vei1 \\\hline
    \student & Ole Olsen, Y‐vei1 \\\hline
    \student & Anne Persen, Y‐vei1 \\\hline
    \student & Kari Jensen, Y‐vei1 \\\hline
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

*Per Jotun*  
*27. januar 2023*
