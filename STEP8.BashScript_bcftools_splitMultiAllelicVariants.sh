#!/bin/bash
## STEP8.BashScript_bcftools_splitMultiAllelicVariants.sh splits multi-allelic variant sites for all vcfs.

## PREPARATION - Specify <parameters>.
# Date.
DATE=$"<DATE>"
# Cohort.
COHORT=$"<COHORT>"
# SamplesFile.
SAMPLES=$"<SAMPLES_INCLUDED_FILE>"
# Directories.
DIRECTORYvcf=$"</PATH/TO/VCFFILE/DIRECTORY/>"
DIRECTORYref=$"</PATH/TO/REFERENCEFILES/DIRECTORY/>"
# RefFiles.etc.
BCFTOOLSTOOL=$"</PATH/TO/BCFTOOLS/>bcftools"
HG19FASTA=$"ref_hg19.fasta"
## END.

## Start running.
printf "Running STEP8.BashScript_bcftools_splitMultiAllelicVariants.sh for cohort: $COHORT, on date: $DATE.\n"
printf "(...)\n\n"
printf "Running STEP8.BashScript_bcftools_splitMultiAllelicVariants.sh for cohort: $COHORT, on date: $DATE.\n" >> logSTEP8.BashScript_bcftools_splitMultiAllelicVariants_$COHORT-$DATE.txt
printf "(...)\n\n" >> logSTEP8.BashScript_bcftools_splitMultiAllelicVariants_$COHORT-$DATE.txt

for sample in $( cat $SAMPLES )
do
	printf "$sample input for bcftools split multi-allelic variant sites.\n" >> logSTEP8.BashScript_bcftools_splitMultiAllelicVariants_$COHORT-$DATE.txt
	printf "(...)\n" >> logSTEP8.BashScript_bcftools_splitMultiAllelicVariants_$COHORT-$DATE.txt
	$BCFTOOLSTOOL norm -m - -f $DIRECTORYref$HG19FASTA $DIRECTORYvcf$sample.variantsGATKunifiedgenotyper.vcf -o $DIRECTORYvcf$sample.variantsGATKunifiedgenotyper.splitted.vcf &>> logSTEP8.BashScript_bcftools_splitMultiAllelicVariants_$COHORT-$DATE.txt
	printf "done.\n\n" >> logSTEP8.BashScript_bcftools_splitMultiAllelicVariants_$COHORT-$DATE.txt

done

printf "All done.\n"
printf "All done.\n" >> logSTEP8.BashScript_bcftools_splitMultiAllelicVariants_$COHORT-$DATE.txt
