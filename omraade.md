[Ta meg tilbake.](./)

# Oversikt over innholdet i filen *./sas/omraade.sas*


## omraade;

#### Formål

Selve rateberegningene. Ratene beregnes basert på &bo 

#### "Steg for steg"-beskrivelse

Kommer senere...

#### Avhengig av følgende datasett

- RV
- andel
- NORGE_AGG_RATE
   - Lages ved å kjøre makro med bo=Norge først. Burde den heller lages i [omraadeNorge](#omraadenorge)-makroen?

#### Lager følgende datasett

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

#### Avhengig av følgende variabler

- SluttÅr
- StartÅr
- Bo
- aar
- forbruksmal

#### Definerer følgende variabler

- Antall_aar

#### Kalles opp av følgende makroer

- [rateberegninger](#rateberegninger)

#### Bruker følgende makroer

Ingen

#### Annet

