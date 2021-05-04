## STEP9.PythonScript_vcfQUALfilter_posForSamtools_rvOnly.py filters rare variant sites on QUAL >=1000 and extracts those positions for mpileup.

## PREPARATION - Specify <parameters>.
# Date.
DATE = "<DATE>"
# Cohort.
COHORT = "<COHORT>"
# SamplesFile.
SAMPLES = "<SAMPLES_INCLUDED_FILE>"
# Directories.
DIRECTORYvcf = "</PATH/TO/VCFFILE/DIRECTORY/>"
DIRECTORYmpileup = "</PATH/TO/MPILEUPFILE/DIRECTORY/>"
DIRECTORYref = "</PATH/TO/REFERENCEFILES/DIRECTORY/>"
## END.

## Start running.
print("Running STEP9.PythonScript_vcfQUALfilter_posForSamtools_rvOnly.py for cohort: " + COHORT + ", on date: " + DATE + ".")
print("(...)\n")

# Define function that extracts information from vcfFile.
def getInfoVcf(line):
    cols = line.split()
    chromosome = cols[0]
    bpposition = cols[1]
    ref        = cols[3]
    alt        = cols[4]
    quality    = float(cols[5])
    return(chromosome, bpposition, ref, alt, quality)
# Define function that extracts information from dbSnp150 refFile.
def getInfoDBsnp150(variant):
    cols = variant.split()
    CHR = cols[0]
    BP  = cols[1]
    REF = cols[3]
    ALT = cols[4]
    return(CHR, BP, REF, ALT)

# Logfile.
logfile = open("logSTEP9.PythonScript_vcfQUALfilter_posForSamtools_rvOnly_" + COHORT + "-" + DATE + ".txt", "w")
logfile.write(DATE + " - " + COHORT + " - STEP9.PythonScript_vcfQUALfilter_posForSamtools_rvOnly.py\n")

# Open dbSnp common variants file.
logfile.write("\n")
logfile.write("Open dbSnp common variants file and process variants.\n")
logfile.write("(...)\n")
dbsnp150_open = open(DIRECTORYref + "dbSnp150common_il1mipTargetRegion_COMMONadjRC_CHR.txt", "r")
# Create list to store common variants in.
commonVarList = []
# Loop over variants and append to list.
for variant in dbsnp150_open:
    if not variant.startswith("#CHROM"):
        CHR, BP, REF, ALT = getInfoDBsnp150(variant)
        dbSnpKey = '{0}{1}{2}{3}{4}{5}{6}'.format(CHR, ":", BP, ":", REF, ":", ALT)
        commonVarList.append(dbSnpKey)
dbsnp150_open.close()
logfile.write("Common variants from dbSnp150 processed and stored into commonVarList.\n")

# Open samplesFile.
logfile.write("\n")
logfile.write("Open samples file.\n")
samples_open = open(SAMPLES, "r")

# Open vcfFiles one sample at a time.
for sample in samples_open:
    sample = sample.strip('\n')
    if sample:
        # Open vcf file.
        logfile.write("\n")
        logfile.write(sample + " input vcf for filtering.\n")
        logfile.write("(...)\n")
        vcf_open = open(DIRECTORYvcf + sample + ".variantsGATKunifiedgenotyper.splitted.vcf", "r")
        # Create filteredvcfFile to write QUAL-filtered variants.
        vcfFiltered = open(DIRECTORYvcf + sample + ".variantsGATKunifiedgenotyper.splitted.QUALfiltered.vcf", 'w')
        # Create rarevariantlocsFile to write rare variant locations for mpileup.
        posForSamtools = open(DIRECTORYmpileup + sample + ".rarevariantlocs.txt", "w")
        # Loop over variants in vcf.
        for line in vcf_open:
            if line.startswith('#'):
                vcfFiltered.write(line)
            else:
                chromosome, bpposition, ref, alt, quality = getInfoVcf(line)
                vcfKey = '{0}{1}{2}{3}{4}{5}{6}'.format(chromosome, ":", bpposition, ":", ref, ":", alt)
                if vcfKey in commonVarList:
                    vcfFiltered.write(line)
                else:
                    if quality >= 1000:
                        vcfFiltered.write(line)
                        samtoolsKey = '{0}{1}{2}{3}{4}\n'.format(chromosome, ":", bpposition, "-", bpposition)
                        posForSamtools.write(samtoolsKey)

        # Vcf processed, close files, write log, and continue.
        vcf_open.close()
        vcfFiltered.close()
        posForSamtools.close()
        logfile.write("done.\n")

# All done, write log, close samplesFile, and finally close logFile.
print("All done.")
logfile.write("\n")
logfile.write("All done.\n")
samples_open.close()
logfile.close()
