## STEP13.PythonScript_vcfFilter_onMpileup.py filters the QUAL-filtered vcfFiles on mpileup output.

## PREPARATION - Specify <parameters>.
# Date.
DATE = "<DATE>"
# Cohort.
COHORT = "<COHORT>"
# SamplesFile.
SAMPLES = "<SAMPLES_INCLUDED_FILE>"
# Directories.
DIRECTORYmpileup = "</PATH/TO/MPILEUPFILE/DIRECTORY/>"
DIRECTORYvcf = "</PATH/TO/VCFFILE/DIRECTORY/>"
## END.

## Start running.
print("Running STEP13.PythonScript_vcfFilter_onMpileup.py for cohort: " + COHORT + ", on date: " + DATE + ".")
print("(...)\n")

# Define function that extracts information from readEndMpileupFile.
def getInfoReadEndPos(line):
    cols = line.strip('\n').split('\t')
    CHR  = cols[0]
    BP   = cols[1]
    REF  = cols[2]
    return(CHR, BP, REF)
# Define function that extracts information from vcf.
def getInfoVcf(variant):
    columns = variant.split('\t')
    chrom  = columns[0]
    bppos  = columns[1]
    ref    = columns[3]
    alt    = columns[4]
    formGT = columns[9]
    return(chrom, bppos, ref, alt, formGT)

# Import necessary modules.
import pandas as pd
import numpy as np

# Logfile.
logfile = open("logSTEP13.PythonScript_vcfFilter_onMpileup_" + COHORT + "-" + DATE + ".txt", "w")
logfile.write(DATE + " - " + COHORT + " - STEP13.PythonScript_vcfFilter_onMpileup.py\n")

# Open samplesFile.
logfile.write("\n")
logfile.write("Open samples file.\n")
samples_open = open(SAMPLES, "r")

# Open vcfFiles and readEndMpileupFiles one sample at a time.
for sample in samples_open:
    sample = sample.strip('\n')
    if sample:
        # Open readEndPositionsFile and store information in list.
        logfile.write("\n")
        logfile.write(sample + " input vcf, parsed mpileups and read-end positions for filtering.\n")
        logfile.write("(...)\n")
        readEndPosFile = open(DIRECTORYmpileup + sample + ".mpileups.readEnd.txt", "r")
        readEndPosList = []
        for readEndPos in readEndPosFile:
            CHR, BP, REF = getInfoReadEndPos(readEndPos)
            readEndKey = '{0}{1}{2}{3}{4}'.format(CHR, ':', BP, ':', REF)
            readEndPosList.append(readEndKey)
        readEndPosFile.close()
        # Open parsedMpileupFile in dataframe, calculate readCount and create variantIndexDictionary.
        pileupParsedDF = pd.read_table(DIRECTORYmpileup + sample + ".mpileups.prepped.parsed.txt", header=0)
        pileupParsedDF['readCount'] = pileupParsedDF['A'] + pileupParsedDF['T'] + pileupParsedDF['C'] + pileupParsedDF['G']
        pileupVarIndexDict = {}
        for index, row in pileupParsedDF.iterrows():
            pileupKey = '{0}{1}{2}'.format(row[0], ':', row[1])
            pileupVarIndexDict[pileupKey] = index
        # Open vcfFile and create vcfMpileupFilteredFile, vcfMpileupLowQualFile, vcfMpileupFalsePositiveFile and txtHomHetUncertainFile to write to.
        vcf_open           = open(DIRECTORYvcf + sample + ".variantsGATKunifiedgenotyper.splitted.QUALfiltered.vcf", "r")
        vcfFiltered        = open(DIRECTORYvcf + sample + ".variantsGATKunifiedgenotyper.splitted.QUALfiltered.pileupFiltered.vcf", "w")
        vcfLowQual         = open(DIRECTORYvcf + sample + ".variantsGATKunifiedgenotyper.splitted.QUALfiltered.pileupLowQual.vcf", "w")
        vcfFalsePositive   = open(DIRECTORYvcf + sample + ".variantsGATKunifiedgenotyper.splitted.QUALfiltered.pileupFalsePositive.vcf", "w")
        txtHomHetUncertain = open(DIRECTORYvcf + sample + ".variantsGATKunifiedgenotyper.splitted.QUALfiltered.pileupHomHetUncertain.txt", "w")
        # Create dictionaries to store variants from vcf.
        substALT_dict = {}
        substGT_dict = {}
        indelALT_dict = {}
        indelGT_dict = {}
        # Loop over variants in vcf.
        for variant in vcf_open:
            if variant.startswith('#'):
                # Write header.
                vcfFiltered.write(variant)
                vcfLowQual.write(variant)
                vcfFalsePositive.write(variant)
            else:
                chrom, bppos, ref, alt, formGT = getInfoVcf(variant)
                vcfKey = '{0}{1}{2}{3}{4}'.format(chrom, ':', bppos, ':', ref)
                if vcfKey in readEndPosList:
                    # Read-end marker in mpileup; write to vcfMpileupLowQualFile.
                    vcfLowQual.write(variant)
                else:
                    vcfGT = formGT.split(':')[0]
                    # Substitutions.
                    if len(ref) == 1 and len(alt) == 1:
                        substALT_dict[vcfKey] = alt
                        substGT_dict[vcfKey] = vcfGT
                        pileupToCheck = '{0}{1}{2}'.format(vcfKey.split(':')[0], ':', vcfKey.split(':')[1])
                        if pileupToCheck in pileupVarIndexDict.keys():
                            pileupRow = pileupVarIndexDict[pileupToCheck]
                            READcount = pileupParsedDF.loc[pileupRow, 'readCount']
                            if READcount <= 20:
                                # Low read count; write to vcfMpileupLowQualFile.
                                vcfLowQual.write(variant)
                            else:
                                ALTcount = pileupParsedDF.loc[pileupRow, alt]
                                ALTperc  = round((float(ALTcount) / READcount) * 100, 2)
                                if ALTperc < 25:
                                    # Alternative percentage too low; write to vcfMpileupFalsePositiveFile.
                                    vcfFalsePositive.write(variant)
                                elif (25 <= ALTperc < 90):
                                    pGT1 = '0/1'
                                    pGT2 = '1/0'
                                    if substGT_dict[vcfKey] == pGT1 or substGT_dict[vcfKey] == pGT2:
                                        # Alternative percentage for heterozygous variant OK; write to vcfMpileupFilteredFile.
                                        vcfFiltered.write(variant)
                                    else:
                                        # Uncertain zygosity; write to vcfMpileupFilteredFile and txtHomHetUncertainFile.
                                        txtHomHetUncertain.write(variant)
                                        vcfFiltered.write(variant)
                                elif 90 <= ALTperc:
                                    pGT = '1/1'
                                    if substGT_dict[vcfKey] == pGT:
                                        # Alternative percentage for homozygous variant OK; write to vcfMpileupFilteredFile.
                                        vcfFiltered.write(variant)
                                    else:
                                        # Uncertain zygosity; write to vcfMpileupFilteredFile and txtHomHetUncertainFile.
                                        txtHomHetUncertain.write(variant)
                                        vcfFiltered.write(variant)
                        else:
                            # No mpileup performed (common variant); write to vcfMpileupFilteredFile.
                            vcfFiltered.write(variant)
                    # Indels.
                    else:
                        indelALT_dict[vcfKey] = alt
                        indelGT_dict[vcfKey] = vcfGT
                        pileupToCheck = '{0}{1}{2}'.format(vcfKey.split(':')[0], ':', vcfKey.split(':')[1])
                        if pileupToCheck in pileupVarIndexDict.keys():
                            pileupRow = pileupVarIndexDict[pileupToCheck]
                            READcount = pileupParsedDF.loc[pileupRow, 'readCount']
                            if READcount <= 20:
                                # Low read count; write to vcfMpileupLowQualFile.
                                vcfLowQual.write(variant)
                            else:
                                # Deletions.
                                if len(ref) > 1:
                                    DELtoCheck = ref[1:]
                                    if pd.isnull(pileupParsedDF.loc[pileupRow, 'Deletion']):
                                        # Deletion not present at all; write to vcfMpileupFalsePositiveFile.
                                        vcfFalsePositive.write(variant)
                                    else:
                                        DELoptions = (pileupParsedDF.loc[pileupRow, 'Deletion']).split('|')
                                        for DELopt in DELoptions:
                                            DELallele = DELopt.split(':')
                                            if DELtoCheck == DELallele[1]:
                                                DELperc = round((float(DELallele[0]) / READcount) * 100, 2)
                                                if DELperc < 25:
                                                    # Alternative percentage too low; write to vcfMpileupFalsePositiveFile.
                                                    vcfFalsePositive.write(variant)
                                                elif (25 <= DELperc < 90):
                                                    pGT1 = '0/1'
                                                    pGT2 = '1/0'
                                                    if indelGT_dict[vcfKey] == pGT1 or indelGT_dict[vcfKey] == pGT2:
                                                        # Alternative percentage for heterozygous variant OK; write to vcfMpileupFilteredFile.
                                                        vcfFiltered.write(variant)
                                                    else:
                                                        # Uncertain zygosity; write to vcfMpileupFilteredFile and txtHomHetUncertainFile.
                                                        txtHomHetUncertain.write(variant)
                                                        vcfFiltered.write(variant)
                                                elif (90 <= DELperc):
                                                    pGT = '1/1'
                                                    if indelGT_dict[vcfKey] == pGT:
                                                        # Alternative percentage for homozygous variant OK; write to vcfMpileupFilteredFile.
                                                        vcfFiltered.write(variant)
                                                    else:
                                                        # Uncertain zygosity; write to vcfMpileupFilteredFile and txtHomHetUncertainFile.
                                                        txtHomHetUncertain.write(variant)
                                                        vcfFiltered.write(variant)
                                else:
                                    # Insertions.
                                    INStoCheck = alt[1:]
                                    if pd.isnull(pileupParsedDF.loc[pileupRow, 'Insertion']):
                                        # Insertion not present at all; write to vcfMpileupFalsePositiveFile.
                                        vcfFalsePositive.write(variant)
                                    else:
                                        INSoptions = (pileupParsedDF.loc[pileupRow, 'Insertion']).split('|')
                                        for INSopt in INSoptions:
                                            INSallele = INSopt.split(':')
                                            if INStoCheck == INSallele[1]:
                                                INSperc = round((float(INSallele[0]) / READcount) * 100, 2)
                                                if INSperc < 25:
                                                    # Alternative percentage too low; write to vcfMpileupFalsePositiveFile.
                                                    vcfFalsePositive.write(variant)
                                                elif (25 <= INSperc < 90):
                                                    pGT1 = '0/1'
                                                    pGT2 = '1/0'
                                                    if indelGT_dict[vcfKey] == pGT1 or indelGT_dict[vcfKey] == pGT2:
                                                        # Alternative percentage for heterozygous variant OK; write to vcfMpileupFilteredFile.
                                                        vcfFiltered.write(variant)
                                                    else:
                                                        # Uncertain zygosity; write to vcfMpileupFilteredFile and txtHomHetUncertainFile.
                                                        txtHomHetUncertain.write(variant)
                                                        vcfFiltered.write(variant)
                                                elif 90 <= INSperc:
                                                    pGT = '1/1'
                                                    if indelGT_dict[vcfKey] == pGT:
                                                        # Alternative percentage for homozygous variant OK; write to vcfMpileupFilteredFile.
                                                        vcfFiltered.write(variant)
                                                    else:
                                                        # Uncertain zygosity; write to vcfMpileupFilteredFile and txtHomHetUncertainFile.
                                                        txtHomHetUncertain.write(variant)
                                                        vcfFiltered.write(variant)
                        else:
                            # No mpileup performed (common variant); write to vcfMpileupFilteredFile.
                            vcfFiltered.write(variant)
        # Vcf filtered on mpileups, close vcfFile, vcfMpileupFilteredFile, vcfMpileupLowQualFile, vcfMpileupFalsePositiveFile, txtHomHetUncertainFile, write log, and continue.
        vcf_open.close()
        vcfFiltered.close()
        vcfLowQual.close()
        vcfFalsePositive.close()
        txtHomHetUncertain.close()
        logfile.write("done.\n")

# All done, write log, close samplesFile, and finally close logFile.
print("All done.")
logfile.write("\n")
logfile.write("All done.\n")
samples_open.close()
logfile.close()
