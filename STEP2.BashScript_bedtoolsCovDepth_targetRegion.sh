#!/bin/bash
## STEP2.BashScript_bedtoolsCovDepth_targetRegion.sh runs bedtools coverage depth for the specified region in the targetcallingFile on all samples.

## PREPARATION - Specify <parameters>.
# Date.
DATE=$"<DATE>"
# Cohort.
COHORT=$"<COHORT>"
# SamplesFile.
SAMPLES=$"<SAMPLES_FILE>"
# Directories.
DIRECTORYbam=$"</PATH/TO/BAMFILE/DIRECTORY/>"
DIRECTORYcov=$"</PATH/TO/COVFILE/DIRECTORY/>"
DIRECTORYref=$"</PATH/TO/REFERENCEFILES/DIRECTORY/>"
# RefFiles.etc.
TARGET=$"targetCallingFile_il1mips.bed"
## END.

## Start running.
printf "Running STEP2.BashScript_bedtoolsCovDepth_targetRegion.sh for cohort: $COHORT, on date: $DATE.\n"
printf "(...)\n\n"
printf "Running STEP2.BashScript_bedtoolsCovDepth_targetRegion.sh for cohort: $COHORT, on date: $DATE.\n" >> logSTEP2.BashScript_bedtoolsCovDepth_targetRegion_$COHORT-$DATE.txt
printf "(...)\n\n" >> logSTEP2.BashScript_bedtoolsCovDepth_targetRegion_$COHORT-$DATE.txt

for sample in $( cat $SAMPLES )
do
	printf "$sample input for bedtools coverage.\n" >> logSTEP2.BashScript_bedtoolsCovDepth_targetRegion_$COHORT-$DATE.txt
	printf "(...)\n" >> logSTEP2.BashScript_bedtoolsCovDepth_targetRegion_$COHORT-$DATE.txt
	bedtools coverage -abam $DIRECTORYbam$sample.readFiltered.sorted.hfix.bam -b $DIRECTORYref$TARGET -d > $DIRECTORYcov$sample.coverage.txt
	printf "done.\n\n" >> logSTEP2.BashScript_bedtoolsCovDepth_targetRegion_$COHORT-$DATE.txt

done

printf "All done.\n"
printf "All done.\n" >> logSTEP2.BashScript_bedtoolsCovDepth_targetRegion_$COHORT-$DATE.txt
