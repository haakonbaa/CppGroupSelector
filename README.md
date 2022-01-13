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

gruppe | poeng
   25  :  15  
   50  :  14  
   49  :  13  
   38  :  12  
   66  :  12  
   32  :  11  
   46  :  11  
    1  :  10  
   22  :  10  
   23  :  10  
   31  :  10  
   35  :  10  
   48  :  10  
   53  :  10  
   30  :  9   
   ...
```