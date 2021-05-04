## STEP3b.PythonScript_parseCovDepth2_sortPerBaseCov.py sorts the per base parsed coverage.

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
print("Running STEP3b.PythonScript_parseCovDepth2_sortPerBaseCov.py for cohort: " + COHORT + ", on date: " + DATE + ".")
print("(...)\n")

# Define function that extracts info and puts into correct variables.
def getInfoCovParsed(line):
    lineOnly = line.strip()
    cols = lineOnly.split('\t')
    covCHR  = cols[0]
    covBP   = cols[1]
    covDP   = cols[2]
    covINFO = cols[3]
    return(covCHR, covBP, covDP, covINFO)
# Define function that reorganizes the information from dictionaries.
def organizeDictInfo(item):
    colmns  = item.split(';')
    covChr  = colmns[1]
    covBp   = colmns[0]
    covDp   = colmns[2]
    covInfo = colmns[3]
    return(covChr, covBp, covDp, covInfo)

# Logfile.
logfile = open("logSTEP3b.PythonScript_parseCovDepth2_sortPerBaseCov_" + COHORT + "-" + DATE + ".txt", "w")
logfile.write(DATE + " - " + COHORT + " - STEP3b.PythonScript_parseCovDepth2_sortPerBaseCov.py\n")

# Open samples file.
logfile.write("\n")
logfile.write("Open samples file.\n")
samples_open = open(SAMPLES, "r")

# Open parsed coverages one sample at a time.
for sample in samples_open:
    sample = sample.strip('\n')
    if sample:
        # Open parsedCoverageFile.
        logfile.write("\n")
        logfile.write(sample + " input parsed coverage for sorting.\n")
        logfile.write("(...)\n")
        parsed_open = open(DIRECTORYcov + sample + ".coverage.parsed.txt", "r")
        # Store information from parsedCoverageFile in lists per chromosome.
        chr1List  = []
        chr2List  = []
        chr3List  = []
        chr5List  = []
        chr6List  = []
        chr7List  = []
        chr9List  = []
        chr11List = []
        chr12List = []
        chr16List = []
        chr17List = []
        chr18List = []
        chr20List = []
        chr22List = []
        chrXList  = []
        for line in parsed_open:
            covCHR, covBP, covDP, covINFO = getInfoCovParsed(line)
            sortkey = '{0}{1}{2}{3}{4}{5}{6}'.format(covBP, ';', covCHR, ';', covDP, ';', covINFO)
            if covCHR == 'chr1':
                chr1List.append(sortkey)
            elif covCHR == 'chr2':
                chr2List.append(sortkey)
            elif covCHR == 'chr3':
                chr3List.append(sortkey)
            elif covCHR == 'chr5':
                chr5List.append(sortkey)
            elif covCHR == 'chr6':
                chr6List.append(sortkey)
            elif covCHR == 'chr7':
                chr7List.append(sortkey)
            elif covCHR == 'chr9':
                chr9List.append(sortkey)
            elif covCHR == 'chr11':
                chr11List.append(sortkey)
            elif covCHR == 'chr12':
                chr12List.append(sortkey)
            elif covCHR == 'chr16':
                chr16List.append(sortkey)
            elif covCHR == 'chr17':
                chr17List.append(sortkey)
            elif covCHR == 'chr18':
                chr18List.append(sortkey)
            elif covCHR == 'chr20':
                chr20List.append(sortkey)
            elif covCHR == 'chr22':
                chr22List.append(sortkey)
            elif covCHR == 'chrX':
                chrXList.append(sortkey)
        # Close parsedCoverageFile.
        parsed_open.close()
        # Sort basepair positions in lists per chromosome.
        chr1List.sort()
        chr2List.sort()
        chr3List.sort()
        chr5List.sort()
        chr6List.sort()
        chr7List.sort()
        chr9List.sort()
        chr11List.sort()
        chr12List.sort()
        chr16List.sort()
        chr17List.sort()
        chr18List.sort()
        chr20List.sort()
        chr22List.sort()
        chrXList.sort()
        # Open sortedCoverageFile to write to and write header.
        sortParsed_open = open(DIRECTORYcov + sample + ".coverage.parsed.sorted.txt", "w")
        sortParsed_open.write('{0}\t{1}\t{2}\t{3}\n'.format('Chrom', 'BPpos', 'MIPcovDepth', 'MIPinfo'))
        # Write sorted lists to sortedCoverageFile.
        for item in chr1List:
            covChr, covBp, covDp, covInfo = organizeDictInfo(item)
            lineToWrite = '{0}\t{1}\t{2}\t{3}\n'.format(covChr, covBp, covDp, covInfo)
            sortParsed_open.write(lineToWrite)
        for item in chr2List:
            covChr, covBp, covDp, covInfo = organizeDictInfo(item)
            lineToWrite = '{0}\t{1}\t{2}\t{3}\n'.format(covChr, covBp, covDp, covInfo)
            sortParsed_open.write(lineToWrite)
        for item in chr3List:
            covChr, covBp, covDp, covInfo = organizeDictInfo(item)
            lineToWrite = '{0}\t{1}\t{2}\t{3}\n'.format(covChr, covBp, covDp, covInfo)
            sortParsed_open.write(lineToWrite)
        for item in chr5List:
            covChr, covBp, covDp, covInfo = organizeDictInfo(item)
            lineToWrite = '{0}\t{1}\t{2}\t{3}\n'.format(covChr, covBp, covDp, covInfo)
            sortParsed_open.write(lineToWrite)
        for item in chr6List:
            covChr, covBp, covDp, covInfo = organizeDictInfo(item)
            lineToWrite = '{0}\t{1}\t{2}\t{3}\n'.format(covChr, covBp, covDp, covInfo)
            sortParsed_open.write(lineToWrite)
        for item in chr7List:
            covChr, covBp, covDp, covInfo = organizeDictInfo(item)
            lineToWrite = '{0}\t{1}\t{2}\t{3}\n'.format(covChr, covBp, covDp, covInfo)
            sortParsed_open.write(lineToWrite)
        for item in chr9List:
            covChr, covBp, covDp, covInfo = organizeDictInfo(item)
            lineToWrite = '{0}\t{1}\t{2}\t{3}\n'.format(covChr, covBp, covDp, covInfo)
            sortParsed_open.write(lineToWrite)
        for item in chr11List:
            covChr, covBp, covDp, covInfo = organizeDictInfo(item)
            lineToWrite = '{0}\t{1}\t{2}\t{3}\n'.format(covChr, covBp, covDp, covInfo)
            sortParsed_open.write(lineToWrite)
        for item in chr12List:
            covChr, covBp, covDp, covInfo = organizeDictInfo(item)
            lineToWrite = '{0}\t{1}\t{2}\t{3}\n'.format(covChr, covBp, covDp, covInfo)
            sortParsed_open.write(lineToWrite)
        for item in chr16List:
            covChr, covBp, covDp, covInfo = organizeDictInfo(item)
            lineToWrite = '{0}\t{1}\t{2}\t{3}\n'.format(covChr, covBp, covDp, covInfo)
            sortParsed_open.write(lineToWrite)
        for item in chr17List:
            covChr, covBp, covDp, covInfo = organizeDictInfo(item)
            lineToWrite = '{0}\t{1}\t{2}\t{3}\n'.format(covChr, covBp, covDp, covInfo)
            sortParsed_open.write(lineToWrite)
        for item in chr18List:
            covChr, covBp, covDp, covInfo = organizeDictInfo(item)
            lineToWrite = '{0}\t{1}\t{2}\t{3}\n'.format(covChr, covBp, covDp, covInfo)
            sortParsed_open.write(lineToWrite)
        for item in chr20List:
            covChr, covBp, covDp, covInfo = organizeDictInfo(item)
            lineToWrite = '{0}\t{1}\t{2}\t{3}\n'.format(covChr, covBp, covDp, covInfo)
            sortParsed_open.write(lineToWrite)
        for item in chr22List:
            covChr, covBp, covDp, covInfo = organizeDictInfo(item)
            lineToWrite = '{0}\t{1}\t{2}\t{3}\n'.format(covChr, covBp, covDp, covInfo)
            sortParsed_open.write(lineToWrite)
        for item in chrXList:
            covChr, covBp, covDp, covInfo = organizeDictInfo(item)
            lineToWrite = '{0}\t{1}\t{2}\t{3}\n'.format(covChr, covBp, covDp, covInfo)
            sortParsed_open.write(lineToWrite)
        # Close sortedCoverageFile and continue.
        logfile.write("done.\n")
        sortParsed_open.close()

# All done, write log, close samplesFile, and finally close logFile.
print("All Done")
logfile.write("\n")
logfile.write("All done.\n")
samples_open.close()
logfile.close()
