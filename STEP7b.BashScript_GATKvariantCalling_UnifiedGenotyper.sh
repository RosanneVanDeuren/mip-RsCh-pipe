#!/bin/bash
## STEP7b.Bashscript_GATKvariantCalling_UnifiedGenotyper.sh runs variant calling by GATK UnifiedGenotyper on read-filtered bamFiles that pass the coverage and gender check.

## PREPARATION - Please first specify all between <>.
# Date.
DATE=$"<DATE>"
# Cohort.
COHORT=$"<COHORT>"
# SamplesFile.
SAMPLES=$"<SAMPLES_INCLUDED_FILE>"
# Directories.
DIRECTORYbam=$"</PATH/TO/BAMFILE/DIRECTORY/>"
DIRECTORYvcf=$"</PATH/TO/VCFFILE/DIRECTORY/>"
DIRECTORYref=$"</PATH/TO/REFERENCEFILES/DIRECTORY/>"
# RefFiles.etc.
GATKJAR=$"</PATH/TO/>GenomeAnalysisTK-3.8-1-0-gf15c1c3ef/GenomeAnalysisTK.jar"
TARGET=$"targetCallingFile_il1mips.bed"
HG19FASTA=$"ref_hg19.fasta"
DB137SNP=$"dbsnp_137.hg19.vcf"
## END.

## Start running.
printf "Running STEP7b.Bashscript_GATKvariantCalling_UnifiedGenotyper.sh for cohort: $COHORT, on date: $DATE.\n"
printf "(...)\n\n"
printf "Running STEP7b.Bashscript_GATKvariantCalling_UnifiedGenotyper.sh for cohort: $COHORT, on date: $DATE.\n" >> logSTEP7b.Bashscript_GATKvariantCalling_UnifiedGenotyper_$COHORT-$DATE.txt
printf "(...)\n\n" >> logSTEP7b.Bashscript_GATKvariantCalling_UnifiedGenotyper_$COHORT-$DATE.txt

for sample in $( cat $SAMPLES )
do
	printf "$sample input for GATK variant calling using UnifiedGenotyper.\n" >> logSTEP7b.Bashscript_GATKvariantCalling_UnifiedGenotyper_$COHORT-$DATE.txt
	printf "(...)\n" >> logSTEP7b.Bashscript_GATKvariantCalling_UnifiedGenotyper_$COHORT-$DATE.txt
	java -jar $GATKJAR -T UnifiedGenotyper -R $DIRECTORYref$HG19FASTA -I $DIRECTORYbam$sample.readFiltered.sorted.hfix.bam -o $DIRECTORYvcf$sample.variantsGATKunifiedgenotyper.vcf -L $DIRECTORYref$TARGET -dcov 5000 -dt BY_SAMPLE --dbsnp $DIRECTORYref$DB137SNP -rf BadCigar -glm BOTH -stand_call_conf 30.0 &>> logSTEP7b.Bashscript_GATKvariantCalling_UnifiedGenotyper_$COHORT-$DATE.txt
	printf "done.\n\n" >> logSTEP7b.Bashscript_GATKvariantCalling_UnifiedGenotyper_$COHORT-$DATE.txt

done

printf "All done.\n"
printf "All done.\n" >> logSTEP7b.Bashscript_GATKvariantCalling_UnifiedGenotyper_$COHORT-$DATE.txt
