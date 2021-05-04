## STEP1.PythonScript_bamFile_readFilter.py filters input bamFiles on mappingQuality >= 60 && nsc && pprsF && pNMlt5.

## PREPARATION - Specify <parameters>.
# Date.
DATE = "<DATE>"
# Cohort.
COHORT = "<COHORT>"
# SamplesFile.
SAMPLES = "<SAMPLES_FILE>"
# Directories.
DIRECTORYbam = "</PATH/TO/BAMFILEDIRECTORY/>"
## END.

## Start running.
print("Running STEP1.PythonScript_bamFile_readFilter.py for cohort: " + COHORT + ", on date: " + DATE + ".")
print("(...)")

# Import relevant modules.
import pysam

# Logfile.
logfile = open("logSTEP1.PythonScript_bamFile_readFilter_" + COHORT + "-" + DATE + ".txt", "w")
logfile.write(DATE + " - " + COHORT + " - STEP1.PythonScript_bamFile_readFilter.py\n")

# Open samplesFile.
logfile.write("\n")
logfile.write("Open samples file.\n")
samples_open = open(SAMPLES, 'r')

# Filter bamFiles on sample at a time.
logfile.write("\n")
logfile.write("Open bamFiles.\n")
for sample in samples_open:
    sample = sample.strip('\n')
    if sample:
        logfile.write("\n")
        logfile.write(sample + " input for pysam processing and filtering reads.\n")
        logfile.write("(...)\n")
        # Open pysam infile and outfile.
        infile = pysam.AlignmentFile(DIRECTORYbam + sample + ".sorted.hfix.bam", "rb")
        outfile = pysam.AlignmentFile(DIRECTORYbam + sample + ".readFiltered.sorted.hfix.bam", "wb", template=infile)
        # Process the reads.
        for read in infile.fetch(until_eof=True, multiple_iterators=True):
            # Filter on mappingQuality >= 60.
            if read.mapping_quality >= 60:
               # Filter on softClipping.
               if not "S" in read.cigarstring:
                   # Filter on properlyPairedFlag.
                   if read.flag & 2:
                       # Filter on NMlt5 or/else INDEL>4.
                       if read.get_tag('NM') < 5:
                           outfile.write(read)
                       else:
                           CIGARtuple = read.cigartuples
                           for tupl in range(0, len(CIGARtuple)):
                               if (CIGARtuple[tupl][0] == 1) or (CIGARtuple[tupl][0] == 2):
                                   if (CIGARtuple[tupl][1] > 4):
                                       outfile.write(read)
        # Close pysam infile and outfile.
        infile.close()
        outfile.close()
        # Index filtered bamFile.
        pysam.index(DIRECTORYbam + sample + ".readFiltered.sorted.hfix.bam", DIRECTORYbam + sample + ".readFiltered.sorted.hfix.bam.bai")
        # Write log, and next sample.
        logfile.write("done.\n")

# All done, write log, close samplesFile, and finally close logFile.
print("All done.")
logfile.write("\n")
logfile.write("All done.\n")
samples_open.close()
logfile.close()
