#!/bin/bash
## STEP10.BashScript_samtoolsMpileup.sh generates mpileups for all rare variant positions for all samples.

## PREPARATION - Specify <parameters>.
# Date.
DATE=$"<DATE>"
# Cohort.
COHORT=$"<COHORT>"
# SamplesFile.
SAMPLES=$"<SAMPLES_INCLUDED_FILE>"
# Directories.
DIRECTORYbam=$"</PATH/TO/BAMFILE/DIRECTORY/>"
DIRECTORYmpileup=$"</PATH/TO/MPILEUPFILE/DIRECTORY/>"
DIRECTORYref=$"</PATH/TO/REFERENCEFILES/DIRECTORY/>"
# RefFiles.etc.
SAMTOOLSTOOL=$"</PATH/TO/SAMTOOLS/>samtools"
HG19FASTA=$"ref_hg19.fasta"
## END.

## Start running.
printf "Running STEP10.BashScript_samtoolsMpileup.sh for cohort: $COHORT, on date: $DATE.\n"
printf "(...)\n\n"
printf "Running STEP10.BashScript_samtoolsMpileup.sh for cohort: $COHORT, on date: $DATE.\n" >> logSTEP10.BashScript_samtoolsMpileup_$COHORT-$DATE.txt
printf "(...)\n\n" >> logSTEP10.BashScript_samtoolsMpileup_$COHORT-$DATE.txt

for sample in $( cat $SAMPLES )
do
	printf "$sample rare variant locations input for samtools mpileup.\n" >> logSTEP10.BashScript_samtoolsMpileup_$COHORT-$DATE.txt
	printf "(...)\n" >> logSTEP10.BashScript_samtoolsMpileup_$COHORT-$DATE.txt
	for pos in $( cat $DIRECTORYmpileup$sample.rarevariantlocs.txt )
	do
		snp=$pos
		$SAMTOOLSTOOL mpileup -r $snp -d 10000 -q 30 -Q 20 -B -f $DIRECTORYref$HG19FASTA $DIRECTORYbam$sample.readFiltered.sorted.hfix.bam > $DIRECTORYmpileup$snp.$sample.mpileup.txt
	done

cat $DIRECTORYmpileup*.$sample.mpileup.txt > $DIRECTORYmpileup$sample.mpileups.txt

rm $DIRECTORYmpileup*.$sample.mpileup.txt

printf "done.\n\n" >> logSTEP10.BashScript_samtoolsMpileup_$COHORT-$DATE.txt

done

printf "All done.\n"
printf "All done.\n" >> logSTEP10.BashScript_samtoolsMpileup_$COHORT-$DATE.txt
