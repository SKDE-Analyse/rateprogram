[Ta meg tilbake.](./)

# Oversikt over makroene i `rateberegninger.sas`


# Innholdsfortegnelse
{: .no_toc}

* auto-gen TOC:
{:toc}

# Makro utvalgx;

#### Form�l

- Lager datasettet `utvalgX`
   - Aggreregerer opp pasienter ut fra inkluderingskriteriene (hvilke �r, alder, etc.)
   - Henter inn antall innbyggere
   - Definerer opp boomr�der

#### "Steg for steg"-beskrivelse

1. Definerer Periode, �r1 etc.
2. Lager datasettet utvalgX av &Ratefil
   - RV = &RV_variabelnavn
   - keep RV ermann aar alder komnr bydel
   - alder mellom 106-115 defineres til 105
   - kj�rer aldjust (ermann = 1, hvis ikke tom)
3. Hvis vis_ekskludering = 1 -> lage tabeller over ekskluderte data i datasett
   - Dette burde flyttes ut i egen makro
4. Aggregerer RV (i `utvalgX`)
   - grupperer p� `aar, KomNr, bydel, Alder, ErMann`. 
   - ekskluderer data hvis aar utenfor &periode, alder utenfor &aldersspenn, komnr > 2030, og ermann ikke i &kjonn
5. Lese inn innbyggerfil
   - aggregering av innbyggere, gruppert som over 
   - samme ekskludering som over
   - legger s� innbyggere til `utvalgX`
6. Definere alderskategorier
   - kj�r makro [valg_kategorier](#valg_kategorier)
   - kj�rer `proc means` 
7. Definerer boomr�der
8. Beregner andeler
   - Er denne n�dvendig? Kan ikke se at den "virker".
   - Lager datasett `Andel`

   
#### Avhengig av f�lgende variabler

- Ratefil (navnet p� det aggregerte datasettet)
- RV_variabelnavn (variablen det skal beregnes rater p�)
- vis_ekskludering (=1 hvis man vil ha ut antall pasienter som er ekskludert)
- innbyggerfil (navnet p� innbyggerfila)
- boomraadeN (?)
- boomraade (?)

#### Definerer f�lgende variabler

Sjekk hvilke som brukes av andre makroer og hvilke som kun er interne.

- aarsvarfigur=1
- Periode=(&Start�r:&Slutt�r)
- Antall_aar=%sysevalf(&Slutt�r-&Start�r+2)
- �r1 etc.


#### Kalles opp av f�lgende makroer

Ingen

#### Bruker f�lgende makroer

- [valg_kategorier](#valg_kategorier)
- Boomraader (fra makro-mappen)

#### Lager f�lgende datasett

- utvalgx (slettes)
- innb_aar (slettes)
- RV
- alderdef (slettes)
- Andel

#### Annet

F�rste makro som kj�res direkte i rateprogrammet


# Makro omraadeNorge;

#### Form�l
{: .no_toc}

#### "Steg for steg"-beskrivelse
{: .no_toc}

1. 

#### Avhengig av f�lgende datasett
{: .no_toc}

-

#### Lager f�lgende datasett
{: .no_toc}

- NORGE_AGG
- NORGE_AGG_SNITT

#### Avhengig av f�lgende variabler
{: .no_toc}

-

#### Definerer f�lgende variabler
{: .no_toc}


#### Kalles opp av f�lgende makroer
{: .no_toc}

-

#### Bruker f�lgende makroer
{: .no_toc}

-

#### Annet
{: .no_toc}
Andre makro som kj�res direkte i rateprogrammet

# Makro omraade;

#### Form�l

Selve rateberegningene. Ratene beregnes basert p� &bo 

#### "Steg for steg"-beskrivelse

Kommer senere...

#### Avhengig av f�lgende datasett

- RV
- andel
- NORGE_AGG_RATE
   - Lages ved � kj�re makro med bo=Norge f�rst. Burde den heller lages i [omraadeNorge](#omraadenorge)-makroen?

#### Lager f�lgende datasett

- RV&Bo
- &Bo._Agg
- &Bo._Agg_Snitt
- alder
- &Bo._Agg_rate
- &Bo._AGG_CV
- NORGE_AGG_RATE2
- NORGE_AGG_RATE3
- NORGE_AGG_RATE4
- NORGE_AGG_RATE5

#### Avhengig av f�lgende variabler

- Slutt�r
- Start�r
- Bo
- aar
- forbruksmal

#### Definerer f�lgende variabler

- Antall_aar

#### Kalles opp av f�lgende makroer

- [rateberegninger](#rateberegninger)

#### Bruker f�lgende makroer

Ingen

#### Annet


# Makro lag_kart;

#### Form�l
{: .no_toc}

#### "Steg for steg"-beskrivelse
{: .no_toc}
1. 

#### Avhengig av f�lgende datasett
{: .no_toc}
-

#### Lager f�lgende datasett
{: .no_toc}

-

#### Avhengig av f�lgende variabler
{: .no_toc}

-

#### Definerer f�lgende variabler
{: .no_toc}


#### Kalles opp av f�lgende makroer
{: .no_toc}

-

#### Bruker f�lgende makroer
{: .no_toc}

-

#### Annet
{: .no_toc}


# Makro omraadeHN;

#### Form�l
{: .no_toc}

#### "Steg for steg"-beskrivelse
{: .no_toc}

1. 

#### Avhengig av f�lgende datasett
{: .no_toc}

-

#### Lager f�lgende datasett
{: .no_toc}

-

#### Avhengig av f�lgende variabler
{: .no_toc}

-

#### Definerer f�lgende variabler
{: .no_toc}


#### Kalles opp av f�lgende makroer
{: .no_toc}

-

#### Bruker f�lgende makroer
{: .no_toc}

-

#### Annet
{: .no_toc}


# Makro valg_kategorier;

## **valg_kategorier**

#### Form�l
{: .no_toc}

Dele alder inn i kategorier, basert p� verdi av `Alderskategorier`

#### "Steg for steg"-beskrivelse
{: .no_toc}

1. Kj�rer en av alderinndeling-makroene, basert p� verdien av Alderskategorier
   - Der defineres `Startgr1`, `SluttGr1` etc.
2. Definerer `alder_ny` til 1, 2 etc. ut fra `Startgr1`, `SluttGr1` etc.

#### Avhengig av f�lgende datasett
{: .no_toc}

- utvalgx

#### Lager f�lgende datasett
{: .no_toc}

Ingen (legger til variablen `alder_ny` til datasettet utvalgx)


#### Avhengig av f�lgende variabler
{: .no_toc}

- `Alderskategorier`

#### Definerer f�lgende variabler
{: .no_toc}

Ingen

#### Kalles opp av f�lgende makroer
{: .no_toc}

- [utvalgX](#utvalgx)

#### Bruker f�lgende makroer
{: .no_toc}

- [Todeltalder](#todeltalder-tredeltalder-firedeltalder-femdeltalder)
- [Tredeltalder](#todeltalder-tredeltalder-firedeltalder-femdeltalder)
- [Firedeltalder](#todeltalder-tredeltalder-firedeltalder-femdeltalder)
- [Femdeltalder](#todeltalder-tredeltalder-firedeltalder-femdeltalder)
- `Alderkat` (hvis Alderskategorier = 99; makroen defineres i selve rateprogrammet)

#### Annet
{: .no_toc}


# Makro tabell_1;

#### Form�l
{: .no_toc}

#### "Steg for steg"-beskrivelse
{: .no_toc}

1. 

#### Avhengig av f�lgende datasett
{: .no_toc}

-

#### Lager f�lgende datasett
{: .no_toc}

-

#### Avhengig av f�lgende variabler
{: .no_toc}

-

#### Definerer f�lgende variabler
{: .no_toc}


#### Kalles opp av f�lgende makroer
{: .no_toc}

-

#### Bruker f�lgende makroer
{: .no_toc}

-

#### Annet
{: .no_toc}


# Makro tabell_1e;

#### Form�l
{: .no_toc}

#### "Steg for steg"-beskrivelse
{: .no_toc}

1. 

#### Avhengig av f�lgende datasett
{: .no_toc}

-

#### Lager f�lgende datasett
{: .no_toc}

-

#### Avhengig av f�lgende variabler
{: .no_toc}

-

#### Definerer f�lgende variabler
{: .no_toc}


#### Kalles opp av f�lgende makroer
{: .no_toc}

-

#### Bruker f�lgende makroer
{: .no_toc}

-

#### Annet
{: .no_toc}


# Makro Tabell_CV;

#### Form�l
{: .no_toc}

#### "Steg for steg"-beskrivelse
{: .no_toc}

1. 

#### Avhengig av f�lgende datasett
{: .no_toc}

-

#### Lager f�lgende datasett
{: .no_toc}

-

#### Avhengig av f�lgende variabler
{: .no_toc}

-

#### Definerer f�lgende variabler
{: .no_toc}


#### Kalles opp av f�lgende makroer
{: .no_toc}

-

#### Bruker f�lgende makroer
{: .no_toc}

-

#### Annet
{: .no_toc}


# Makro Tabell_CVe;

#### Form�l
{: .no_toc}

#### "Steg for steg"-beskrivelse
{: .no_toc}

1. 

#### Avhengig av f�lgende datasett
{: .no_toc}

-

#### Lager f�lgende datasett
{: .no_toc}

-

#### Avhengig av f�lgende variabler
{: .no_toc}

-

#### Definerer f�lgende variabler
{: .no_toc}


#### Kalles opp av f�lgende makroer
{: .no_toc}

-

#### Bruker f�lgende makroer
{: .no_toc}

-

#### Annet
{: .no_toc}


# Makro tabell_3N;

#### Form�l
{: .no_toc}

#### "Steg for steg"-beskrivelse
{: .no_toc}

1. 

#### Avhengig av f�lgende datasett
{: .no_toc}

-

#### Lager f�lgende datasett
{: .no_toc}

-

#### Avhengig av f�lgende variabler
{: .no_toc}

-

#### Definerer f�lgende variabler
{: .no_toc}


#### Kalles opp av f�lgende makroer
{: .no_toc}

-

#### Bruker f�lgende makroer
{: .no_toc}

-

#### Annet
{: .no_toc}


# Makro tabell_3Ne;

#### Form�l
{: .no_toc}

#### "Steg for steg"-beskrivelse
{: .no_toc}

1. 

#### Avhengig av f�lgende datasett
{: .no_toc}

-

#### Lager f�lgende datasett
{: .no_toc}

-

#### Avhengig av f�lgende variabler
{: .no_toc}

-

#### Definerer f�lgende variabler
{: .no_toc}


#### Kalles opp av f�lgende makroer
{: .no_toc}

-

#### Bruker f�lgende makroer
{: .no_toc}

-

#### Annet
{: .no_toc}


# Makro Tabell_3;

#### Form�l
{: .no_toc}

#### "Steg for steg"-beskrivelse
{: .no_toc}

1. 

#### Avhengig av f�lgende datasett
{: .no_toc}

-

#### Lager f�lgende datasett
{: .no_toc}

-

#### Avhengig av f�lgende variabler
{: .no_toc}

-

#### Definerer f�lgende variabler
{: .no_toc}


#### Kalles opp av f�lgende makroer
{: .no_toc}

-

#### Bruker f�lgende makroer
{: .no_toc}

-

#### Annet
{: .no_toc}


# Makro Tabell_3e;

#### Form�l
{: .no_toc}

#### "Steg for steg"-beskrivelse
{: .no_toc}

1. 

#### Avhengig av f�lgende datasett
{: .no_toc}

-

#### Lager f�lgende datasett
{: .no_toc}

-

#### Avhengig av f�lgende variabler
{: .no_toc}

-

#### Definerer f�lgende variabler
{: .no_toc}


#### Kalles opp av f�lgende makroer
{: .no_toc}

-

#### Bruker f�lgende makroer
{: .no_toc}

-

#### Annet
{: .no_toc}


# Makro lag_aarsvarbilde;

#### Form�l
{: .no_toc}

#### "Steg for steg"-beskrivelse
{: .no_toc}

1. 

#### Avhengig av f�lgende datasett
{: .no_toc}

-

#### Lager f�lgende datasett
{: .no_toc}

-

#### Avhengig av f�lgende variabler
{: .no_toc}

-

#### Definerer f�lgende variabler
{: .no_toc}


#### Kalles opp av f�lgende makroer
{: .no_toc}

-

#### Bruker f�lgende makroer
{: .no_toc}

-

#### Annet
{: .no_toc}


# Makro lag_aarsvarfigur;

#### Form�l
{: .no_toc}

#### "Steg for steg"-beskrivelse
{: .no_toc}

1. 

#### Avhengig av f�lgende datasett
{: .no_toc}

-

#### Lager f�lgende datasett
{: .no_toc}

-

#### Avhengig av f�lgende variabler
{: .no_toc}

-

#### Definerer f�lgende variabler
{: .no_toc}


#### Kalles opp av f�lgende makroer
{: .no_toc}

-

#### Bruker f�lgende makroer
{: .no_toc}

-

#### Annet
{: .no_toc}

#### Form�l
{: .no_toc}

#### "Steg for steg"-beskrivelse
{: .no_toc}

1. 

#### Avhengig av f�lgende datasett
{: .no_toc}

-

#### Lager f�lgende datasett
{: .no_toc}

-

#### Avhengig av f�lgende variabler
{: .no_toc}

-

#### Definerer f�lgende variabler
{: .no_toc}


#### Kalles opp av f�lgende makroer
{: .no_toc}

-

#### Bruker f�lgende makroer
{: .no_toc}

-

#### Annet
{: .no_toc}


# Makro KI_bilde;


# Makro lagre_dataNorge;

Beskrivelse

# Makro lagre_dataN;

Beskrivelse

# Makro lagre_dataHN;

Beskrivelse

# Makro aarsvar;

#### Form�l
{: .no_toc}

#### "Steg for steg"-beskrivelse
{: .no_toc}

1. 

#### Avhengig av f�lgende datasett
{: .no_toc}

-

#### Lager f�lgende datasett
{: .no_toc}

-

#### Avhengig av f�lgende variabler
{: .no_toc}

-

#### Definerer f�lgende variabler
{: .no_toc}


#### Kalles opp av f�lgende makroer
{: .no_toc}

-

#### Bruker f�lgende makroer
{: .no_toc}

-

#### Annet
{: .no_toc}

# Makro rateberegninger;

#### Form�l

Makro som beregner rater og spytter ut tabeller og figurer.

#### "Steg for steg"-beskrivelse

1. Lager datasettet `Norgeaarsspenn` fra `RV` og henter ut variablene min_aar og max_aar
2. Legger variablen alder til `norge_agg_snitt`
   - `alder=(substr(alder_ny,1,((find(alder_ny,'-','i'))-1)))-0;`
3. Lager tabell over aldersstruktur, basert p� datasett `norge_agg_snitt`
4. Definere variablene Periode, Antall_aar, �r1 etc. (dette gj�res ogs� i utvalgX-makroen)
5. Kaller opp [omraade](#omraade)-makroen, som beregner ratene etc. ut fra `Bo`. `Bo` kan v�re

|`Bo`        |variabel = 1        |makro       |
| ---------- | -----------        | ---------- |
| Norge      |                    | [omraade](#omraade)    |
| BoRHF      | &RHF=1             | [omraade](#omraade)    |
| BoHF       | &HF=1              | [omraade](#omraade)    | 
| BoShHN     | &sykehus_HN=1      | [omraadeHN](#omraadehn)|
| komnr      | &kommune=1         | [omraade](#omraade)    | 
| komnr      | &kommune_HN=1      | [omraadeHN](#omraadehn)|
| fylke      | &fylke=1           | [omraade](#omraade)    |
| VK         | &Verstkommune_HN=1 | [omraadeHN](#omraadehn)|
| bydel      | &oslo=1            | [omraade](#omraade)    |
   
6. Kaller opp tabell-rutiner, figur-rutiner etc. basert p� valg gjort i rateprogrammet (se variabelliste under)

#### Avhengig av f�lgende datasett

- `RV`
- `norge_agg_snitt`

#### Lager f�lgende datasett

- Norgeaarsspenn (kun for � finne min_aar og max_aar?)

#### Avhengig av f�lgende variabler

- tallformat
- ratevariabel
- forbruksmal
- boomraadeN
- boomraade
- Vis_tabeller
- RHF
- kart
- aarsvarfigur
- Fig_AA_RHF
- KIfigur
- Fig_KI_RHF
- HF
- Fig_AA_HF
- Fig_KI_HF
- sykehus_HN
- Fig_AA_ShHN
- Fig_KI_ShHN
- kommune
- Fig_AA_kom
- Fig_KI_kom
- kommune_HN
- Fig_AA_komHN
- Fig_KI_komHN
- fylke
- Fig_AA_fylke
- Fig_KI_fylke
- Verstkommune_HN
- oslo
- Fig_AA_Oslo
- Fig_KI_Oslo


#### Definerer f�lgende variabler

Sjekk hvilke som brukes av andre makroer og hvilke som kun er interne.

- aarsvarfigur (defineres ogs� i [utvalgX](#utvalgx))
- Periode (defineres ogs� i [utvalgX](#utvalgx))
- Antall_aar (defineres ogs� i [utvalgX](#utvalgx))
- �r1 etc. (defineres ogs� i [utvalgX](#utvalgx))
- Bo (brukes i tabell-rutiner og figur-rutiner som kalles opp)


#### Kalles opp av f�lgende makroer

Ingen

#### Bruker f�lgende makroer

- [omraade](#omraade) (selve rateberegningene)
- [tabell_1](#tabell_1) (hvis Vis_tabeller=1,2,3 og tallformat=NLnum) Kj�res for Bo=Norge, Bo=BoRHF, , 
- [tabell_1e](#tabell_1e) (hvis Vis_tabeller=1,2,3 og tallformat=Excel)
- [tabell_3N](#tabell_3n) (hvis Vis_tabeller=3 og tallformat=NLnum)
- [tabell_3Ne](#tabell_3ne) (hvis Vis_tabeller=3 og tallformat=Excel)
- [lagre_dataNorge](#lagre_datanorge)
- [tabell_CV](#tabell_cv)
- [tabell_CVe](#tabell_cve)
- [tabell_3](#tabell_3)
- [tabell_3e](#tabell_3e)
- [lag_kart](#lag_kart)
- [lag_aarsvarbilde](#lag_aarsvarbilde)
- [lag_aarsvarfigur](#lag_aarsvarfigur)
- [KI_bilde](#ki_bilde)
- [KI_figur](#ki_figur)
- [lagre_dataN](#lagre_datan)
- [omraadeHN](#omraadehn)

#### Annet

Kj�res som tredje makro av rateprogrammet (etter [utvalgX](#utvalgX) og [omraadeNorge](#omraadeNorge))

