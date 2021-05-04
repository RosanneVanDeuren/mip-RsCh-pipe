## STEP3a.PythonScript_parseCovDepth1_perBaseCov.py parses raw bedtools coverage depth per base.

## PREPARATION - Specify <parameters>.
# Date.
DATE = "<DATE>"
# Cohort.
COHORT = "<COHORT>"
# SamplesFile.
SAMPLES = "<SAMPLES_FILE>"
# Directories.
DIRECTORYcov = "</PATH/TO/COVFILE/DIRECTORY/>"
## END.

## Start running.
print("Running STEP3a.PythonScript_parseCovDepth1_perBaseCov.py for cohort: " + COHORT + ", on date: " + DATE + ".")
print("(...)\n")

# Define function that extracts info from rawCoverageFile file.
def getCovDepthInfo(line):
    columns     = line.split('\t')
    MIPchr      = columns[0]
    MIPstart    = int(columns[1])
    MIPend      = int(columns[2])
    MIPname     = columns[3]
    MIPstrand   = columns[4]
    MIPindex    = int(columns[5])
    MIPcovDepth = int(columns[6])
    return(MIPchr, MIPstart, MIPend, MIPname, MIPstrand, MIPindex, MIPcovDepth)

# Logfile.
logfile = open("logSTEP3a.PythonScript_parseCovDepth1_perBaseCov_" + COHORT + "-" + DATE + ".txt", "w")
logfile.write(DATE + " - " + COHORT + " - STEP3a.PythonScript_parseCovDepth1_perBaseCov.py\n")

# Open samples file.
logfile.write("\n")
logfile.write("Open samples file.\n")
samples_open = open(SAMPLES, 'r')

# Open raw coverages one sample at a time.
logfile.write("\n")
logfile.write("Open raw coverageFiles.\n")
for sample in samples_open:
    sample = sample.strip('\n')
    if sample:
        # Open rawCoverageFile.
        logfile.write("\n")
        logfile.write(sample + " input raw coverage for parsing.\n")
        logfile.write("(...)\n")
        rawCoverage_open = open(DIRECTORYcov + sample + '.coverage.txt', 'r')
        # Loop over lines, extract relevant information and store in position_dict.
        position_dict = {}
        for line in rawCoverage_open:
            MIPchr, MIPstart, MIPend, MIPname, MIPstrand, MIPindex, MIPcovDepth = getCovDepthInfo(line)
            outCHROM = MIPchr
            outBP    = (MIPstart + (MIPindex - 1))
            posKey   = '{0}{1}{2}'.format(outCHROM, ':', outBP)
            MIPinfo  = '{0}{1}{2}{3}{4}{5}{6}{7}{8}{9}{10}'.format(MIPname, '|', '(', MIPstrand, ')', '|', '[', MIPstart, '-', MIPend, ']')
            posVal   = '{0}{1}{2}'.format(MIPcovDepth, ';', MIPinfo)
            position_dict.setdefault(posKey, []).append(posVal)
        # Close rawCoverageFile.
        rawCoverage_open.close()
        # Create parsedCoverageFile to write to and write header.
        parsedCoverage_open = open(DIRECTORYcov + sample + '.coverage.parsed.txt', 'w')
        parsedCoverage_open.write('{0}\t{1}\t{2}\t{3}\n'.format('Chrom', 'BPpos', 'MIPcovDepth', 'MIPinfo'))
        # Process position_dict and write to parsedCoverageFile.
        for key in position_dict:
            posCHR = key.split(':')[0]
            posBP  = key.split(':')[1]
            samePos = {}
            for item in position_dict[key]:
                posCov = item.split(';')[0]
                posMIPinfo = item.split(';')[1]
                samePos.setdefault(posCov, []).append(posMIPinfo)
            linetowrite = '{0}\t{1}\t{2}\t{3}\n'.format(posCHR, posBP, posCov, ', '.join(samePos[posCov]))
            parsedCoverage_open.write(linetowrite)

        # Raw coverage parsed, write log, close parsedCoverageFile and continue.
        logfile.write("done.\n")
        parsedCoverage_open.close()

# All done, write log, close samplesFile, and finally close logFile.
print("All done.")
logfile.write("\n")
logfile.write("All done.\n")
samples_open.close()
logfile.close()
