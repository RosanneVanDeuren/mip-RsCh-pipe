#!/bin/bash
## STEP4.BashScript_averageCoverage_targetRegion.sh calculates the average coverage for all samples over the target region.

## PREPARATION - Specify <parameters>.
# Date.
DATE=$"<DATE>"
# Cohort.
COHORT=$"<COHORT>"
# SamplesFile.
SAMPLES=$"<SAMPLES_FILE>"
# Directories.
DIRECTORYcov=$"</PATH/TO/COVFILE/DIRECTORY/>"
## END.

## Start running.
printf "Running STEP4.BashScript_averageCoverage_targetRegion.sh for cohort: $COHORT, on date: $DATE.\n"
printf "(...)\n\n"

OUTAVCOVFILE=$"outSTEP4_averageCoverage_targetRegion_"$COHORT"-"$DATE".txt"

for sample in $( cat $SAMPLES )
do
	printf "$sample\n" >> $DIRECTORYcov$OUTAVCOVFILE
	cat $DIRECTORYcov$sample.coverage.parsed.sorted.txt | awk '{ NR > 1 } { total += $3 } END { print total/(NR-1) }' >> $DIRECTORYcov$OUTAVCOVFILE
done

printf "All done.\n"
