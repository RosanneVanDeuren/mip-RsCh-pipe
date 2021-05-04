## STEP11.PythonScript_mpileupPreFilter_forPerlParsing.py prefilters mpileups in preparation for parsing by perl and saves positions with read-end-markers.

## PREPARATION - Specify <parameters>.
# Date.
DATE = "<DATE>"
# Cohort.
COHORT = "<COHORT>"
# SamplesFile.
SAMPLES = "<SAMPLES_INCLUDED_FILE>"
# Directories.
DIRECTORYmpileup = "</PATH/TO/MPILEUPFILE/DIRECTORY/>"
## END.

## Start running.
print("Running STEP11.PythonScript_mpileupPreFilter_forPerlParsing.py for cohort: " + COHORT + ", on date: " + DATE + ".")
print("(...)\n")

# Define function that extracts info from mpileupFile.
def getinfompileup(line):
    colmns = line.strip('\n').split('\t')
    pileup_chr = colmns[0]
    pileup_bp = int(colmns[1])
    pileup_ref = colmns[2]
    pileup_rc = int(colmns[3])
    pileup_seq = (colmns[4]).upper().replace(',', '.')
    pileup_bq = colmns[5]
    return(pileup_chr, pileup_bp, pileup_ref, pileup_rc, pileup_seq, pileup_bq)

# Logfile.
logfile = open("logSTEP11.PythonScript_mpileupPreFilter_forPerlParsing_" + COHORT + "-" + DATE + ".txt", "w")
logfile.write(DATE + " - " + COHORT + " - STEP11.PythonScript_mpileupPreFilter_forPerlParsing.py\n")

# Open samplesFile.
logfile.write("\n")
logfile.write("Open samples file.\n")
samples_open = open(SAMPLES, "r")

# Open merged mpileups one sample at a time.
for sample in samples_open:
    sample = sample.strip('\n')
    if sample:
        # Open merged mpileups.
        logfile.write("\n")
        logfile.write(sample + " input merged mpileups for pre-filter.\n")
        logfile.write("(...)\n")
        pileup_open = open(DIRECTORYmpileup + sample + ".mpileups.txt", "r")
        # Create preppedMpileupFile to write adjusted mpileup sequences.
        preppedMpileup_open = open(DIRECTORYmpileup + sample + ".mpileups.prepped.txt", "w")
        # Create readEndMpileupFile to write locations with readEndMarkers.
        readEndMpileup = open(DIRECTORYmpileup + sample + ".mpileups.readEnd.txt", "w")
        # Loop over mpileups.
        for line in pileup_open:
            pileup_chr, pileup_bp, pileup_ref, pileup_rc, pileup_seq, pileup_bq = getinfompileup(line)
            if not '$' in pileup_seq:
                preppedMpileup_open.write('{0}\t{1}\t{2}\t{3}\t{4}\t{5}\n'.format(pileup_chr, pileup_bp, pileup_ref, pileup_rc, pileup_seq, pileup_bq))
            else:
                readEndMpileup.write('{0}\t{1}\t{2}\n'.format(pileup_chr, pileup_bp, pileup_ref))
        # Mpileups prepped, close mergedMpileupFile, preppedMpileupFile, readEndMpileupFile, write log, and continue.
        preppedMpileup_open.close()
        pileup_open.close()
        readEndMpileup.close()
        logfile.write("done.\n")

# All done, write log, close samplesFile, and finally close logFile.
print("All done.")
logfile.write("\n")
logfile.write("All done.\n")
samples_open.close()
logfile.close()
