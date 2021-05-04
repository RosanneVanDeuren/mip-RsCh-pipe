##STEP14c.PythonScript_parseHomHetUncertainVariants.py combines HomHetUncertain information from all samples into one combined file.

## PREPARATION - Specify <parameters>.
# Date.
DATE = "<DATE>"
# Cohort.
COHORT = "<COHORT>"
# SamplesFile.
SAMPLES = "<SAMPLES_INCLUDED_FILE>"
# Directories.
DIRECTORYvcf = "</PATH/TO/VCFFILE/DIRECTORY/>"
## END.

## Start running.
print("Running STEP14c.PythonScript_parseHomHetUncertainVariants.py for cohort: " + COHORT + ", on date: " + DATE + ".")
print("(...)\n")

# Define function that extracts information from vcf.
def getinfoVcfDF(row):
    cols = row.split('\t')
    chrom = cols[0]
    bppos = int(cols[1])
    ref   = cols[3]
    alt   = cols[4]
    return(chrom, bppos, ref, alt)
# Define function that assembles correct information for deletions in vcf.
def delinfoVcfDF(chrom, bppos, ref, alt):
    chromosome = chrom
    bpstart    = (bppos + 1)
    refall     = ref[1:]
    altall     = 'DEL'
    return(chromosome, bpstart, refall, altall)
# Define function that assembles correct information for insertions in vcf.
def insinfoVcfDF(chrom, bppos, ref, alt):
    chromosome = chrom
    bpstart    = bppos
    refall     = 'INS'
    altall     = alt[1:]
    return(chromosome, bpstart, refall, altall)
# Define function that assembles correct information for substitutions in vcf.
def substinfoVcfDF(chrom, bppos, ref, alt):
    chromosome = chrom
    bpstart    = bppos
    refall     = ref
    altall     = alt
    return(chromosome, bpstart, refall, altall)

# Import required modules.
import pandas as pd

# Logfile.
logfile = open("logSTEP14c.PythonScript_parseHomHetUncertainVariants_" + COHORT + "-" + DATE + ".txt", "w")
logfile.write(DATE + " - " + COHORT + " - STEP14c.PythonScript_parseHomHetUncertainVariants.py\n")

# Open samplesFile.
logfile.write("\n")
logfile.write("Open samples file.\n")
samples_open = open(SAMPLES, "r")

# Open txtHomHetUncertainFiles one sample at a time and combine information in a dictionary.
HomHetUncertain_dict = {}
for sample in samples_open:
    sample = sample.strip('\n')
    if sample:
        # Open txtHomHetUncertainFile.
        logfile.write("\n")
        logfile.write(sample + " input txtHomHetUncertain to be combined.\n")
        logfile.write("(...)\n")
        HomHetUncertain_open = open(DIRECTORYvcf + sample + ".variantsGATKunifiedgenotyper.splitted.QUALfiltered.pileupHomHetUncertain.txt", "r")
        for row in HomHetUncertain_open:
            chrom, bppos, ref, alt = getinfoVcfDF(row)
            if len(ref) > 1:
                chromosome, bpstart, refall, altall = delinfoVcfDF(chrom, bppos, ref, alt)
            elif len(alt) > 1:
                chromosome, bpstart, refall, altall = insinfoVcfDF(chrom, bppos, ref, alt)
            else:
                chromosome, bpstart, refall, altall = substinfoVcfDF(chrom, bppos, ref, alt)
            varKey = '{0}{1}{2}{3}{4}{5}{6}'.format(chromosome, ':', bpstart, ':', refall, ':', altall)
            # Add to dictionary.
            HomHetUncertain_dict.setdefault(varKey, []).append(sample)
        # HomHetUncertain locations processed, write log, close file and continue.
        logfile.write("done.\n")
        HomHetUncertain_open.close()

# All samples processed, write log and close samplesFile.
logfile.write("\n")
logfile.write("All samples processed.\n")
samples_open.close()

# Store HomHetUncertainVariants in dataframe and then write out to file.
HomHetUncertainDF = pd.DataFrame(columns=['key', 'value'])
num = 0
for pair in HomHetUncertain_dict.items():
    num +=1
    HomHetUncertainDF.loc[num, 'key'] = pair[0]
    HomHetUncertainDF.loc[num, 'value'] = pair[1]
OUTFILE = "txtHomHetUncertainVariantInformation_" + COHORT + "-" + DATE + ".txt"
HomHetUncertainDF.to_csv(DIRECTORYvcf + OUTFILE, sep = "\t", index = False)
logfile.write("\n")
logfile.write("OutputFile with HomHetUncertainVariant information written.\n")

# All done, write log, and close logFile.
print("All done.")
logfile.write("\n")
logfile.write("All done.\n")
logfile.close()
