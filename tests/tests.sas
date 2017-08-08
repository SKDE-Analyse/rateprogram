/*
En samling tester av rateprogrammet
*/


%macro test1(branch = master);

/*
Arnfinn aug. 2017

Test av rateprogrammet i sin helhet. Kj�rer rateprogrammet fra A til �.

Variabel-valg finnes i tests\definerVariabler.sas

*/

%local filbane;
%let filbane=\\tos-sas-skde-01\SKDE_SAS\;

%include "&filbane.rateprogram\&branch\tests\makroer.sas";

%testAnno(slettDatasett = 0);

%testUtvalgX(alene = 0, branch = &branch, slettDatasett = 0, definerVariabler = 1);

%testOmraadeNorge(alene = 0, branch = &branch, slettDatasett = 0, definerVariabler = 0);

%testRateberegninger(alene = 0, branch = &branch, slettDatasett = 1, definerVariabler = 0);

%mend;

%macro test2(branch = master);

/*
Arnfinn aug. 2017

Test av deler av rateprogrammet hver for seg.

*/

%local filbane;
%let filbane=\\tos-sas-skde-01\SKDE_SAS\;

%include "&filbane.rateprogram\&branch\tests\makroer.sas";

%include "&filbane.rateprogram\&branch\tests\definerVariabler.sas";
%definerVariabler;

%testRateberegninger(alene = 1, branch = &branch);

%testOmraadeNorge(alene = 1, branch = &branch);

%testUtvalgX(alene = 1, branch = &branch);


%mend;
