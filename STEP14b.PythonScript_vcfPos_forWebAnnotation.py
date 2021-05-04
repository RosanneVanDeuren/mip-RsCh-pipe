## STEP14b.PythonScript_vcfPos_forWebAnnotation.py extracts positions from mergedVcf as input for in-house annotation service.

## PREPARATION - Specify <parameters>.
# Date.
DATE = "<DATE>"
# Cohort.
COHORT = "<COHORT>"
# Directories.
DIRECTORYvcf = "</PATH/TO/VCFFILE/DIRECTORY/>"
# InputFile.
INFILE = "<MERGEDSPLITTEDVCF_OUTPUT_STEP14a>"
## END.

## Start running.
print("Running STEP14b.PythonScript_vcfPos_forWebAnnotation.py for cohort: " + COHORT + ", on date: " + DATE + ".")
print("(...)\n")

# Define function that extracts information from vcfFile.
def getinfoVcfDF(row):
    chrom = row[0]
    bppos = int(row[1])
    ref   = row[3]
    alt   = row[4]
    return(chrom, bppos, ref, alt)
# Define function that assembles correct information deletions.
def delinfoVcfDF(chrom, bppos, ref, alt):
    chromosome = chrom
    bpstart    = (bppos + 1)
    bpend      = bppos + (len(ref) - 1)
    refall     = ref[1:]
    altall     = ''
    return(chromosome, bpstart, bpend, refall, altall)
# Define function that assembles correct information for insertions.
def insinfoVcfDF(chrom, bppos, ref, alt):
    chromosome = chrom
    bpstart    = bppos
    bpend      = bppos
    refall     = ''
    altall     = alt[1:]
    return(chromosome, bpstart, bpend, refall, altall)
# Define function that assembles correct information for substitutions.
def substinfoVcfDF(chrom, bppos, ref, alt):
    chromosome = chrom
    bpstart    = bppos
    bpend      = bppos
    refall     = ref
    altall     = alt
    return(chromosome, bpstart, bpend, refall, altall)

# Import necessary modules.
import pandas as pd
import numpy as np

# Logfile.
logfile = open("logSTEP14b.PythonScript_vcfPos_forWebAnnotation_" + COHORT + "-" + DATE + ".txt", "w")
logfile.write(DATE + " - " + COHORT + " - STEP14b.PythonScript_vcfPos_forWebAnnotation.py\n")

# Open vcfFile and count header lines.
logfile.write("\n")
logfile.write("Open vcf to count header lines.\n")
vcf_open = open(DIRECTORYvcf + INFILE, "r")
countHeader = 0
for line in vcf_open:
    if line.startswith("##"):
        countHeader +=1
vcf_open.close()

# Open vcfFile in dataframe without header lines.
logfile.write("\n")
logfile.write("Open vcf in dataframe without header lines.\n")
vcf_df = pd.read_table(DIRECTORYvcf + INFILE, skiprows=countHeader, sep = "\t", header = 0)

# Open locsForAnnotationFile to write to.
OUTFILE = "vcfsMergedSplitted_positions_forWebAnnotation_" + COHORT + "-" + DATE + ".txt"
locsForAnnotationFile = open(DIRECTORYvcf + OUTFILE, "w")
locsForAnnotationFile.write('{0}\t{1}\t{2}\t{3}\t{4}\n'.format('Chromosome', 'Start Position', 'End Position', 'Reference', 'Variant'))

# Loop over variants and extract positions for annotation.
logfile.write("\n")
logfile.write("Extract variant positions for in-house annotation.\n")
logfile.write("(...)\n")
for index, row in vcf_df.iterrows():
    chrom, bppos, ref, alt = getinfoVcfDF(row)
    if len(ref) > 1:
        chromosome, bpstart, bpend, refall, altall = delinfoVcfDF(chrom, bppos, ref, alt)
    elif len(alt) > 1:
        chromosome, bpstart, bpend, refall, altall = insinfoVcfDF(chrom, bppos, ref, alt)
    else:
        chromosome, bpstart, bpend, refall, altall = substinfoVcfDF(chrom, bppos, ref, alt)
    locsForAnnotationFile.write('{0}\t{1}\t{2}\t{3}\t{4}\n'.format(chromosome, bpstart, bpend, refall, altall))
logfile.write("done.\n")

# All done, close locsForAnnotationFile, write log, and finally close logFile.
print("All done.")
locsForAnnotationFile.close()
logfile.write("\n")
logfile.write("All done.\n")
logfile.close()
