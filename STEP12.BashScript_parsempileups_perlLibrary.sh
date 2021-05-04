#!/bin/bash
## STEP12.BashScript_parsempileups_perlLibrary.sh uses a publicly available perl library for parsing mpileups.

## PREPARATION - Specify <parameters>.
# Date.
DATE=$"<DATE>"
# Cohort.
COHORT=$"<COHORT>"
# SamplesFile.
SAMPLES=$"<SAMPLES_INCLUDED_FILE>"
# Directories.
DIRECTORYmpileup=$"</PATH/TO/MPILEUPFILE/DIRECTORY/>"
# RefFiles.etc.
PERLPARSETOOL=$"</PATH/TO/>pileup2base/pileup2baseindel_no_strand.pl"
## END.

## Start running.
printf "Running STEP12.BashScript_parsempileups_perlLibrary.sh for cohort: $COHORT, on date: $DATE.\n"
printf "(...)\n\n"
printf "Running STEP12.BashScript_parsempileups_perlLibrary.sh for cohort: $COHORT, on date: $DATE.\n" >> logSTEP12.BashScript_parsempileups_perlLibrary_$COHORT-$DATE.txt
printf "(...)\n\n" >> logSTEP12.BashScript_parsempileups_perlLibrary_$COHORT-$DATE.txt

for sample in $( cat $SAMPLES )

do
	printf "$sample prepped mpileups input for perl library parsing.\n" >> logSTEP12.BashScript_parsempileups_perlLibrary_$COHORT-$DATE.txt
	printf "(...)\n" >> logSTEP12.BashScript_parsempileups_perlLibrary_$COHORT-$DATE.txt
	perl $PERLPARSETOOL $DIRECTORYmpileup$sample.mpileups.prepped.txt 1 $DIRECTORYmpileup$sample.mpileups.prepped.parsed.txt >> logSTEP12.BashScript_parsempileups_perlLibrary_$COHORT-$DATE.txt
	printf "done.\n\n" >> logSTEP12.BashScript_parsempileups_perlLibrary_$COHORT-$DATE.txt
done

printf "All done.\n"
printf "All done.\n" >> logSTEP12.BashScript_parsempileups_perlLibrary_$COHORT-$DATE.txt
