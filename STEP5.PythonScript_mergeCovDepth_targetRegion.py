## STEP5.PythonScript_mergeCovDepth_targetRegion.py merges the parsed, sorted coverage depth from all samples into a combined file.

## PREPARATION - Please first specify all between <>.
# Date.
DATE = "<DATE>"
# Cohort.
COHORT = "<COHORT>"
# SamplesFile.
SAMPLES = "<SAMPLES_FILE>"
# Directories.
DIRECTORYcov = "</PATH/TO/COVFILE/DIRECTORY/>"
DIRECTORYref = "</PATH/TO/REFERENCEFILES/DIRECTORY/>"
## END.

## Start running.
print("Running STEP5.PythonScript_mergeCovDepth_targetRegion.py for cohort: " + COHORT + ", on date: " + DATE + ".")
print("(...)\n")

# Import relevant modules.
import pandas as pd

# Logfile.
logfile = open("logSTEP5.PythonScript_mergeCovDepth_targetRegion_" + COHORT + "-" + DATE + ".txt", "w")
logfile.write(DATE + " - " + COHORT + " - STEP5.PythonScript_mergeCovDepth_targetRegion.py\n")

# Open baseCoverageFile.
logfile.write("\n")
logfile.write("Open base coverage file.\n")
BASECOV = "baseCovDepthDF_il1mipTargetRegion.txt"
baseDF = pd.read_table(DIRECTORYref + BASECOV, sep = '\t', header = 0, index_col=None)

# Open samplesFile.
logfile.write("\n")
logfile.write("Open samples file.\n")
samples_open = open(SAMPLES, 'r')
# Open sorted coverage one sample at a time.
for sample in samples_open:
    sample = sample.strip('\n')
    if sample:
        # Open sortedCoverageFile.
        logfile.write("\n")
        logfile.write(sample + " input sorted coverage for merging.\n")
        logfile.write("(...)\n")
        cov_df = pd.read_table(DIRECTORYcov + sample + '.coverage.parsed.sorted.txt', sep = '\t', header = 0, usecols=['MIPcovDepth'], index_col=None)
        baseDF[sample] = cov_df['MIPcovDepth']
        # Coverage merged, write log, and continue.
        logfile.write("done.\n")

# All samples processed, write log and close samples file.
logfile.write("\n")
logfile.write("All sample coverages merged.\n")
samples_open.close()

# All done, write log, write mergedCoverageFile, close samplesFile, and finally close logFile.
OUTFILEcov = COHORT + "_mergedCoverages_" + DATE + ".txt"
baseDF.to_csv(DIRECTORYcov + OUTFILEcov, sep = '\t', header = True, index = False)
logfile.write("\n")
logfile.write("Merged coverage file written.\n")
print("All done.")
logfile.write("\n")
logfile.write("All done.\n")
logfile.close()
