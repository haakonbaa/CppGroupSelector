# CppGroupSelector
### Velg den beste gruppen
Et lite script for å finne den beste LA-gruppen for akkurat deg i TDT4102 Vår 2022.

kjør koden med
```bash
python3 main.py
```
eller *ctrl* + *c* , *ctrl* + *v* rett inn in [Jupyter](https://jupyter.org/install), [vscode](https://code.visualstudio.com/) eller en hvilken som helst annen kul [IDE](https://www.vim.org/) ;)
### eksempel på kjøring:
```
klokka   man   tir    ons   tor   fre  
08-09     0     1      1     0     1   
09-10     0     1      1     0     1   
10-11     3     1      0     0     0   
11-12     3     1      0     0     0   
12-13     3     2      0     0     3   
13-14     2     3      0     0     3   
14-15     2     0      0     0     2   
15-16     3     0      0     0     2   
16-17     3     3      0     0     1   
17-18     0     3      0     0     0   
18-19     0     2      2     2
19-20     1     1      2     2 
skriv hvor godt den gitte datoen passer
på en skala fra 0-3. skriv "p","n" for 
hennholdsvis forrige og neste.
torsdag 19-20 : 2

Resultat:

gruppe | poeng | tider
   25  :  15   : Mandag 12:00 - 14:00  Fredag 12:00 - 16:00
   50  :  14   : Tirsdag 16:00 - 18:00  Onsdag 18:00 - 20:00  Torsdag 18:00 - 20:00
   49  :  13   : Tirsdag 16:00 - 20:00  Torsdag 18:00 - 20:00
   38  :  12   : Mandag 14:00 - 16:00  Tirsdag 12:00 - 14:00  Fredag 08:00 - 10:00
   66  :  12   : Tirsdag 16:00 - 18:00  Torsdag 08:00 - 10:00  Fredag 12:00 - 14:00
   32  :  11   : Mandag 10:00 - 12:00  Tirsdag 18:00 - 20:00  Onsdag 08:00 - 10:00
   46  :  11   : Tirsdag 12:00 - 14:00  Onsdag 10:00 - 12:00  Fredag 12:00 - 14:00
    1  :  10   : Torsdag 12:00 - 14:00  Fredag 12:00 - 16:00
   22  :  10   : Onsdag 12:00 - 14:00  Onsdag 18:00 - 20:00  Fredag 12:00 - 14:00
   23  :  10   : Tirsdag 08:00 - 12:00  Fredag 12:00 - 14:00
   31  :  10   : Mandag 12:00 - 14:00  Tirsdag 12:00 - 16:00
   35  :  10   : Onsdag 10:00 - 12:00  Fredag 12:00 - 16:00
   48  :  10   : Mandag 12:00 - 16:00  Onsdag 10:00 - 12:00
   53  :  10   : Mandag 12:00 - 16:00  Torsdag 08:00 - 10:00
   30  :  9    : Mandag 16:00 - 18:00  Tirsdag 08:00 - 10:00  Torsdag 18:00 - 20:00
   36  :  9    : Mandag 14:00 - 16:00  Onsdag 10:00 - 12:00  Fredag 14:00 - 16:00
   ...
```