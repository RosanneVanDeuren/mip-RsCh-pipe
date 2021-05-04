## STEP15.PythonScript_combine_mergedVcf_annotation.py combines the output from in-house annotation service with merged vcf into a txtVariantFile that is easily imported into Excel.

## PREPARATION - Specify <parameters>.
# Date.
DATE = "<DATE>"
# Cohort.
COHORT = "<COHORT>"
# SamplesFile.
SAMPLES = "<SAMPLES_INCLUDED_FILE>"
# Directories.
DIRECTORYvcf = "</PATH/TO/VCFFILE/DIRECTORY/>"
DIRECTORYout = "</PATH/TO/OUT/DIRECTORY/>"
# Infiles.
vcfINFILE = "<MERGEDSPLITTEDVCF_OUTPUT_STEP14a>"
txtINFILE = "<TXT_HOMHETUNCERTAIN_OUTPUT_STEP14c>"
annotINFILE = "<ANNOTATED_MERGEDVCFPOS_OUTPUT_INHOUSESERVICE>"
#END.

## Start running.
print("Running STEP15.PythonScript_combine_mergedVcf_annotation.py for cohort: " + COHORT + ", on date: " + DATE + ".")
print("(...)\n")

# Define function that extracts information from vcf.
def getinfoVcfDF(row):
    chrom = row[0]
    bppos = row[1]
    ref   = row[3]
    alt   = row[4]
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
# Define function that extracts information from annotatedFile.
def getinfoAnnotDF(row):
    chrom = row[0]
    bppos = row[1]
    ref   = row[3]
    alt   = row[4]
    return(chrom, bppos, ref, alt)
# Define function that assembles correct information for deletions in annotatedFile.
def delinfoAnnotDF(chrom, bppos, ref, alt):
    chromosome = chrom
    bpstart    = bppos
    refall     = ref
    altall     = 'DEL'
    return(chromosome, bpstart, refall, altall)
# Define function that assembles correct information for insertions in annotatedFile.
def insinfoAnnotDF(chrom, bppos, ref, alt):
    chromosome = chrom
    bpstart    = bppos
    refall     = 'INS'
    altall     = alt
    return(chromosome, bpstart, refall, altall)
# Define function that assembles correct information for substitutions in annotatedFile.
def substinfoAnnotDF(chrom, bppos, ref, alt):
    chromosome = chrom
    bpstart    = bppos
    refall     = ref
    altall     = alt
    return(chromosome, bpstart, refall, altall)

# Import necessary modules.
import pandas as pd
import numpy as np

# Logfile.
logfile = open("logSTEP15.PythonScript_combine_mergedVcf_annotation_" + COHORT + "-" + DATE + ".txt", "w")
logfile.write(DATE + " - " + COHORT + " - STEP15.PythonScript_combine_mergedVcf_annotation.py\n")

# Open vcfFile and count header lines.
logfile.write("\n")
logfile.write("Open vcf to count header lines.\n")
vcf_open = open(DIRECTORYvcf + vcfINFILE, "r")
countHeader = 0
for line in vcf_open:
    if line.startswith("##"):
        countHeader +=1
vcf_open.close()
logfile.write("Header lines counted.\n")

# Open vcfFile in dataframe without header lines.
logfile.write("\n")
logfile.write("Open vcf in dataframe without header lines.\n")
vcf_df = pd.read_table(DIRECTORYvcf + vcfINFILE, skiprows=countHeader, sep = "\t", header = 0)

# Loop over all variants in vcf and store information in vcfVariantIndex_dict.
logfile.write("\n")
logfile.write("Extract variant-position information and store in vcfVariantIndex_dict.\n")
logfile.write("(...)\n")
vcfVariantIndex_dict = {}
for index, row in vcf_df.iterrows():
    chrom, bppos, ref, alt = getinfoVcfDF(row)
    if len(ref) > 1:
        chromosome, bpstart, refall, altall = delinfoVcfDF(chrom, bppos, ref, alt)
    elif len(alt) > 1:
        chromosome, bpstart, refall, altall = insinfoVcfDF(chrom, bppos, ref, alt)
    else:
        chromosome, bpstart, refall, altall = substinfoVcfDF(chrom, bppos, ref, alt)
    # Add to dictionary.
    varKey = '{0}{1}{2}{3}{4}{5}{6}'.format(chromosome, ':', bpstart, ':', refall, ':', altall)
    vcfVariantIndex_dict[index] = varKey
logfile.write("done.\n")

# Define sampleIDs based on columns in vcf.
sampleIDs = vcf_df.columns.values[9:]
# Extract genotypes from vcf for all sampleIDs and store in vcfGThet_dict and vcfGThom_dict.
logfile.write("\n")
logfile.write("Extract genotypes from vcf for all sampleIDs and store in vcfGThet_dict and vcfGThom_dict.\n")
logfile.write("(...)\n")
vcfGThet_dict = {}
vcfGThom_dict = {}
for index, variant in vcfVariantIndex_dict.items():
    vcfGTkey = variant
    for sample in sampleIDs:
        vcfFormatInfo = vcf_df.loc[index, sample]
        vcfGT = vcfFormatInfo.split(':')[0]
        if vcfGT == '0/1' or vcfGT == '1/0':
            vcfGThet_dict.setdefault(vcfGTkey, []).append(sample)
        elif vcfGT == '1/1':
            vcfGThom_dict.setdefault(vcfGTkey, []).append(sample)
        else:
            continue
logfile.write("done.\n")

# Import txtHomHetUncertain and store in txtHomHetUncertain_dict.
logfile.write("\n")
logfile.write("Open txtHomHetUncertainVariants and store in txtHomHetUncertain_dict.\n")
logfile.write("(...)\n")
txtHomHetUncertainDF = pd.read_table(DIRECTORYvcf + txtINFILE, sep = "\t", header = 0)
txtHomHetUncertainDF.columns = ["varKey", "samples"]
txtHomHetUncertain_dict = {}
for index, row in txtHomHetUncertainDF.iterrows():
    varkey = row[0]
    samples = row[1]
    txtHomHetUncertain_dict[varkey] = samples
logfile.write("done.\n")

# Open annotated variants file and store variant-position information in annotVariantIndex_dict.
logfile.write("\n")
logfile.write("Open annotated variants file and store variant-position information in annotVariantIndex_dict.\n")
logfile.write("(...)\n")
annot_df = pd.read_table(DIRECTORYvcf + annotINFILE, sep = '\t', header = 0)
annotVariantIndex_dict = {}
for index, row in annot_df.iterrows():
    chrom, bppos, ref, alt = getinfoAnnotDF(row)
    if pd.isnull(alt):
        chromosome, bpstart, refall, altall = delinfoAnnotDF(chrom, bppos, ref, alt)
    elif pd.isnull(ref):
        chromosome, bpstart, refall, altall = insinfoAnnotDF(chrom, bppos, ref, alt)
    else:
        chromosome, bpstart, refall, altall = substinfoAnnotDF(chrom, bppos, ref, alt)
    varHcDiffKey = '{0}{1}{2}{3}{4}{5}{6}'.format(chromosome, ':', bpstart, ':', refall, ':', altall)
    annotVariantIndex_dict[varHcDiffKey] = index
logfile.write("done.\n")

# Add genotypes to a copy of the annotated variants file.
logfile.write("\n")
logfile.write("Combine genotypes and annotation information.\n")
logfile.write("(...)\n")
annotGT_df = annot_df.assign(HeterozygousSamples="", HeterozygousCount=0, HomozygousSamples="", HomozygousCount=0, TotalCount=0, UncertainGenotype="")
for variantHET, samplesHET in vcfGThet_dict.items():
    rowToFillHET = annotVariantIndex_dict[variantHET]
    countHET  = len(samplesHET)
    annotGT_df.loc[rowToFillHET, 'HeterozygousCount'] = countHET
    annotGT_df.loc[rowToFillHET, 'HeterozygousSamples'] = '; '.join(samplesHET)
    if variantHET in txtHomHetUncertain_dict.keys():
        annotGT_df.loc[rowToFillHET, 'UncertainGenotype'] = txtHomHetUncertain_dict[variantHET]
for variantHOM, samplesHOM in vcfGThom_dict.items():
    rowToFillHOM = annotVariantIndex_dict[variantHOM]
    countHOM = len(samplesHOM)
    annotGT_df.loc[rowToFillHOM, 'HomozygousCount'] = countHOM
    annotGT_df.loc[rowToFillHOM, 'HomozygousSamples'] = '; '.join(samplesHOM)
    if variantHOM in txtHomHetUncertain_dict.keys():
        annotGT_df.loc[rowToFillHOM, 'UncertainGenotype'] = txtHomHetUncertain_dict[variantHOM]
# Compute total count.
annotGT_df['TotalCount'] = annotGT_df['HeterozygousCount'] + annotGT_df['HomozygousCount']
logfile.write("done.\n")

# Write out combined file.
logfile.write("\n")
logfile.write("Write out combined file.\n")
logfile.write("(...)\n")
combinedOUTFILE = "mergedAnnotatedVariants_" + COHORT + "-" + DATE + ".txt"
annotGT_df.to_csv(DIRECTORYout + combinedOUTFILE, sep = '\t', index = False)
logfile.write("done.\n")

# All done, write log, and finally close logFile.
print("All done.")
logfile.write("\n")
logfile.write("All done.\n")
logfile.close()
