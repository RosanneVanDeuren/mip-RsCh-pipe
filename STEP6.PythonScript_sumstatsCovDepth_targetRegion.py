## STEP6.PythonScript_sumstatsCovDepth_targetRegion.py calculates coverage summary statistics for all samples in the combined file.

## PREPARATION - Please first specify all between <>.
# Date.
DATE = "<DATE>"
# Cohort.
COHORT = "<COHORT>"
# Directories.
DIRECTORYcov = "</PATH/TO/COVFILE/DIRECTORY/>"
# InputFile.
MERGED_COVDEPTH = "<STEP5_OUTPUT_FILE>"
## END.

## Start running.
print("Running STEP6.PythonScript_sumstatsCovDepth_targetRegion.py for cohort: " + COHORT + ", on date: " + DATE + ".")
print("(...)\n")

# Import relevant modules.
import pandas as pd
import numpy as np

# Logfile.
logfile = open("logSTEP6.PythonScript_sumstatsCovDepth_targetRegion_" + COHORT + "-" + DATE + ".txt", "w")
logfile.write(DATE + " - " + COHORT + " - STEP6.PythonScript_sumstatsCovDepth_targetRegion.py\n")

# Open mergedCoverageFile and create geneMIPindex_dict.
logfile.write("\n")
logfile.write("Open merged coverage file and create geneMIPindex_dict.\n")
logfile.write("(...)\n")
covDepth_df = pd.read_table(DIRECTORYcov + MERGED_COVDEPTH, header = 0)
geneMIPindex_dict = {}
for index, col in covDepth_df.iterrows():
    MIPinfo = col[2]
    if 'AIM2' in MIPinfo:
        geneMIPindex_dict.setdefault('AIM2', []).append(index)
    elif 'ATG16L1' in MIPinfo:
        geneMIPindex_dict.setdefault('ATG16L1', []).append(index)
    elif 'ATG5' in MIPinfo:
        geneMIPindex_dict.setdefault('ATG5', []).append(index)
    elif 'ATG7' in MIPinfo:
        geneMIPindex_dict.setdefault('ATG7', []).append(index)
    elif 'BECN1' in MIPinfo:
        geneMIPindex_dict.setdefault('BECN1', []).append(index)
    elif 'CASP1' in MIPinfo:
        geneMIPindex_dict.setdefault('CASP1', []).append(index)
    elif 'CYBA' in MIPinfo:
        geneMIPindex_dict.setdefault('CYBA', []).append(index)
    elif 'CYBB' in MIPinfo:
        geneMIPindex_dict.setdefault('CYBB', []).append(index)
    elif '_IL18_' in MIPinfo:
        geneMIPindex_dict.setdefault('IL18', []).append(index)
    elif 'IL18BP' in MIPinfo:
        geneMIPindex_dict.setdefault('IL18BP', []).append(index)
    elif 'IL18R1' in MIPinfo:
        geneMIPindex_dict.setdefault('IL18R1', []).append(index)
    elif 'IL18RAP' in MIPinfo:
        geneMIPindex_dict.setdefault('IL18RAP', []).append(index)
    elif 'IL1A' in MIPinfo:
        geneMIPindex_dict.setdefault('IL1A', []).append(index)
    elif 'IL1B' in MIPinfo:
        geneMIPindex_dict.setdefault('IL1B', []).append(index)
    elif 'IL1F10' in MIPinfo:
        geneMIPindex_dict.setdefault('IL1F10', []).append(index)
    elif 'IL1R1' in MIPinfo:
        geneMIPindex_dict.setdefault('IL1R1', []).append(index)
    elif 'IL1R2' in MIPinfo:
        geneMIPindex_dict.setdefault('IL1R2', []).append(index)
    elif '_IL1RAP_' in MIPinfo:
        geneMIPindex_dict.setdefault('IL1RAP', []).append(index)
    elif 'IL1RAPL1' in MIPinfo:
        geneMIPindex_dict.setdefault('IL1RAPL1', []).append(index)
    elif 'IL1RAPL2' in MIPinfo:
        geneMIPindex_dict.setdefault('IL1RAPL2', []).append(index)
    elif 'IL1RL1' in MIPinfo:
        geneMIPindex_dict.setdefault('IL1RL1', []).append(index)
    elif 'IL1RL2' in MIPinfo:
        geneMIPindex_dict.setdefault('IL1RL2', []).append(index)
    elif 'IL1RN' in MIPinfo:
        geneMIPindex_dict.setdefault('IL1RN', []).append(index)
    elif 'IL33' in MIPinfo:
        geneMIPindex_dict.setdefault('IL33', []).append(index)
    elif 'IL36A' in MIPinfo:
        geneMIPindex_dict.setdefault('IL36A', []).append(index)
    elif 'IL36B' in MIPinfo:
        geneMIPindex_dict.setdefault('IL36B', []).append(index)
    elif 'IL36G' in MIPinfo:
        geneMIPindex_dict.setdefault('IL36G', []).append(index)
    elif 'IL36RN' in MIPinfo:
        geneMIPindex_dict.setdefault('IL36RN', []).append(index)
    elif 'IL37' in MIPinfo:
        geneMIPindex_dict.setdefault('IL37', []).append(index)
    elif 'IRAK4' in MIPinfo:
        geneMIPindex_dict.setdefault('IRAK4', []).append(index)
    elif 'KIAA0226' in MIPinfo:
        geneMIPindex_dict.setdefault('KIAA0226', []).append(index)
    elif 'MAP1LC3A' in MIPinfo:
        geneMIPindex_dict.setdefault('MAP1LC3A', []).append(index)
    elif 'MYD88' in MIPinfo:
        geneMIPindex_dict.setdefault('MYD88', []).append(index)
    elif 'NCF1' in MIPinfo:
        geneMIPindex_dict.setdefault('NCF1', []).append(index)
    elif 'NCF2' in MIPinfo:
        geneMIPindex_dict.setdefault('NCF2', []).append(index)
    elif 'NCF4' in MIPinfo:
        geneMIPindex_dict.setdefault('NCF4', []).append(index)
    elif 'NLRP1' in MIPinfo:
        geneMIPindex_dict.setdefault('NLRP1', []).append(index)
    elif 'NLRP3' in MIPinfo:
        geneMIPindex_dict.setdefault('NLRP3', []).append(index)
    elif 'NOX4' in MIPinfo:
        geneMIPindex_dict.setdefault('NOX4', []).append(index)
    elif 'PIK3C3' in MIPinfo:
        geneMIPindex_dict.setdefault('PIK3C3', []).append(index)
    elif 'PYCARD' in MIPinfo:
        geneMIPindex_dict.setdefault('PYCARD', []).append(index)
    elif 'RAC1' in MIPinfo:
        geneMIPindex_dict.setdefault('RAC1', []).append(index)
    elif 'RAC2' in MIPinfo:
        geneMIPindex_dict.setdefault('RAC2', []).append(index)
    elif 'RAP1A' in MIPinfo:
        geneMIPindex_dict.setdefault('RAP1A', []).append(index)
    elif 'SIGIRR' in MIPinfo:
        geneMIPindex_dict.setdefault('SIGIRR', []).append(index)
    elif 'TIMD4' in MIPinfo:
        geneMIPindex_dict.setdefault('TIMD4', []).append(index)
    elif 'TRAF6' in MIPinfo:
        geneMIPindex_dict.setdefault('TRAF6', []).append(index)
    elif 'UVRAG' in MIPinfo:
        geneMIPindex_dict.setdefault('UVRAG', []).append(index)
# Dictionary geneMIPindex_dict created.
logfile.write("Dictionary geneMIPindex_dict created.\n")

# Collect start and stop information per gene.
logfile.write("\n")
logfile.write("Collect start and stop information per gene.\n")
logfile.write("(...)\n")
# AIM2.
startAIM2 = (geneMIPindex_dict['AIM2'][0])
stopAIM2  = (geneMIPindex_dict['AIM2'][(len(geneMIPindex_dict['AIM2']) - 1)])
# ATG16L1.
startATG16L1 = (geneMIPindex_dict['ATG16L1'][0])
stopATG16L1  = (geneMIPindex_dict['ATG16L1'][(len(geneMIPindex_dict['ATG16L1']) - 1)])
# ATG5.
startATG5 = (geneMIPindex_dict['ATG5'][0])
stopATG5  = (geneMIPindex_dict['ATG5'][(len(geneMIPindex_dict['ATG5']) - 1)])
# ATG7.
startATG7 = (geneMIPindex_dict['ATG7'][0])
stopATG7  = (geneMIPindex_dict['ATG7'][(len(geneMIPindex_dict['ATG7']) - 1)])
# BECN1.
startBECN1 = (geneMIPindex_dict['BECN1'][0])
stopBECN1  = (geneMIPindex_dict['BECN1'][(len(geneMIPindex_dict['BECN1']) - 1)])
# CASP1.
startCASP1 = (geneMIPindex_dict['CASP1'][0])
stopCASP1  = (geneMIPindex_dict['CASP1'][(len(geneMIPindex_dict['CASP1']) - 1)])
# CYBA.
startCYBA = (geneMIPindex_dict['CYBA'][0])
stopCYBA  = (geneMIPindex_dict['CYBA'][(len(geneMIPindex_dict['CYBA']) - 1)])
# CYBB.
startCYBB = (geneMIPindex_dict['CYBB'][0])
stopCYBB  = (geneMIPindex_dict['CYBB'][(len(geneMIPindex_dict['CYBB']) - 1)])
# IL18.
startIL18 = (geneMIPindex_dict['IL18'][0])
stopIL18  = (geneMIPindex_dict['IL18'][(len(geneMIPindex_dict['IL18']) - 1)])
# IL18BP.
startIL18BP = (geneMIPindex_dict['IL18BP'][0])
stopIL18BP  = (geneMIPindex_dict['IL18BP'][(len(geneMIPindex_dict['IL18BP']) - 1)])
# IL18R1.
startIL18R1 = (geneMIPindex_dict['IL18R1'][0])
stopIL18R1  = (geneMIPindex_dict['IL18R1'][(len(geneMIPindex_dict['IL18R1']) - 1)])
# IL18RAP.
startIL18RAP = (geneMIPindex_dict['IL18RAP'][0])
stopIL18RAP  = (geneMIPindex_dict['IL18RAP'][(len(geneMIPindex_dict['IL18RAP']) - 1)])
# IL1A.
startIL1A = (geneMIPindex_dict['IL1A'][0])
stopIL1A  = (geneMIPindex_dict['IL1A'][(len(geneMIPindex_dict['IL1A']) - 1)])
#IL1B.
startIL1B = (geneMIPindex_dict['IL1B'][0])
stopIL1B  = (geneMIPindex_dict['IL1B'][(len(geneMIPindex_dict['IL1B']) - 1)])
# IL1F10.
startIL1F10 = (geneMIPindex_dict['IL1F10'][0])
stopIL1F10  = (geneMIPindex_dict['IL1F10'][(len(geneMIPindex_dict['IL1F10']) - 1)])
# IL1R1.
startIL1R1 = (geneMIPindex_dict['IL1R1'][0])
stopIL1R1  = (geneMIPindex_dict['IL1R1'][(len(geneMIPindex_dict['IL1R1']) - 1)])
# IL1R2.
startIL1R2 = (geneMIPindex_dict['IL1R2'][0])
stopIL1R2  = (geneMIPindex_dict['IL1R2'][(len(geneMIPindex_dict['IL1R2']) - 1)])
# IL1RAP.
startIL1RAP = (geneMIPindex_dict['IL1RAP'][0])
stopIL1RAP  = (geneMIPindex_dict['IL1RAP'][(len(geneMIPindex_dict['IL1RAP']) - 1)])
# IL1RAPL1.
startIL1RAPL1 = (geneMIPindex_dict['IL1RAPL1'][0])
stopIL1RAPL1  = (geneMIPindex_dict['IL1RAPL1'][(len(geneMIPindex_dict['IL1RAPL1']) - 1)])
# IL1RAPL2.
startIL1RAPL2 = (geneMIPindex_dict['IL1RAPL2'][0])
stopIL1RAPL2  = (geneMIPindex_dict['IL1RAPL2'][(len(geneMIPindex_dict['IL1RAPL2']) - 1)])
#IL1RL1.
startIL1RL1 = (geneMIPindex_dict['IL1RL1'][0])
stopIL1RL1  = (geneMIPindex_dict['IL1RL1'][(len(geneMIPindex_dict['IL1RL1']) - 1)])
# IL1RL2.
startIL1RL2 = (geneMIPindex_dict['IL1RL2'][0])
stopIL1RL2  = (geneMIPindex_dict['IL1RL2'][(len(geneMIPindex_dict['IL1RL2']) - 1)])
# IL1RN.
startIL1RN = (geneMIPindex_dict['IL1RN'][0])
stopIL1RN  = (geneMIPindex_dict['IL1RN'][(len(geneMIPindex_dict['IL1RN']) - 1)])
# IL33.
startIL33 = (geneMIPindex_dict['IL33'][0])
stopIL33  = (geneMIPindex_dict['IL33'][(len(geneMIPindex_dict['IL33']) - 1)])
# IL36A.
startIL36A = (geneMIPindex_dict['IL36A'][0])
stopIL36A  = (geneMIPindex_dict['IL36A'][(len(geneMIPindex_dict['IL36A']) - 1)])
# IL36B.
startIL36B = (geneMIPindex_dict['IL36B'][0])
stopIL36B  = (geneMIPindex_dict['IL36B'][(len(geneMIPindex_dict['IL36B']) - 1)])
# IL36G.
startIL36G = (geneMIPindex_dict['IL36G'][0])
stopIL36G  = (geneMIPindex_dict['IL36G'][(len(geneMIPindex_dict['IL36G']) - 1)])
# IL36RN.
startIL36RN = (geneMIPindex_dict['IL36RN'][0])
stopIL36RN  = (geneMIPindex_dict['IL36RN'][(len(geneMIPindex_dict['IL36RN']) - 1)])
# IL37.
startIL37 = (geneMIPindex_dict['IL37'][0])
stopIL37  = (geneMIPindex_dict['IL37'][(len(geneMIPindex_dict['IL37']) - 1)])
# IRAK4.
startIRAK4 = (geneMIPindex_dict['IRAK4'][0])
stopIRAK4  = (geneMIPindex_dict['IRAK4'][(len(geneMIPindex_dict['IRAK4']) - 1)])
# KIAA0226.
startKIAA0226 = (geneMIPindex_dict['KIAA0226'][0])
stopKIAA0226  = (geneMIPindex_dict['KIAA0226'][(len(geneMIPindex_dict['KIAA0226']) - 1)])
# MAP1LC3A.
startMAP1LC3A = (geneMIPindex_dict['MAP1LC3A'][0])
stopMAP1LC3A  = (geneMIPindex_dict['MAP1LC3A'][(len(geneMIPindex_dict['MAP1LC3A']) - 1)])
# MYD88.
startMYD88 = (geneMIPindex_dict['MYD88'][0])
stopMYD88  = (geneMIPindex_dict['MYD88'][(len(geneMIPindex_dict['MYD88']) - 1)])
# NCF1.
startNCF1 = (geneMIPindex_dict['NCF1'][0])
stopNCF1  = (geneMIPindex_dict['NCF1'][(len(geneMIPindex_dict['NCF1'])-1)])
# NCF2.
startNCF2 = (geneMIPindex_dict['NCF2'][0])
stopNCF2  = (geneMIPindex_dict['NCF2'][(len(geneMIPindex_dict['NCF2']) - 1)])
# NCF4.
startNCF4 = (geneMIPindex_dict['NCF4'][0])
stopNCF4  = (geneMIPindex_dict['NCF4'][(len(geneMIPindex_dict['NCF4']) - 1)])
# NLRP1.
startNLRP1 = (geneMIPindex_dict['NLRP1'][0])
stopNLRP1  = (geneMIPindex_dict['NLRP1'][(len(geneMIPindex_dict['NLRP1']) - 1)])
# NLRP3.
startNLRP3 = (geneMIPindex_dict['NLRP3'][0])
stopNLRP3  = (geneMIPindex_dict['NLRP3'][(len(geneMIPindex_dict['NLRP3']) - 1)])
# NOX4.
startNOX4 = (geneMIPindex_dict['NOX4'][0])
stopNOX4  = (geneMIPindex_dict['NOX4'][(len(geneMIPindex_dict['NOX4']) - 1)])
# PIK3C3.
startPIK3C3 = (geneMIPindex_dict['PIK3C3'][0])
stopPIK3C3  = (geneMIPindex_dict['PIK3C3'][(len(geneMIPindex_dict['PIK3C3']) - 1)])
# PYCARD.
startPYCARD = (geneMIPindex_dict['PYCARD'][0])
stopPYCARD  = (geneMIPindex_dict['PYCARD'][(len(geneMIPindex_dict['PYCARD']) - 1)])
# RAC1.
startRAC1 = (geneMIPindex_dict['RAC1'][0])
stopRAC1  = (geneMIPindex_dict['RAC1'][(len(geneMIPindex_dict['RAC1']) - 1)])
# RAC2.
startRAC2 = (geneMIPindex_dict['RAC2'][0])
stopRAC2  = (geneMIPindex_dict['RAC2'][(len(geneMIPindex_dict['RAC2']) - 1)])
# RAP1A.
startRAP1A = (geneMIPindex_dict['RAP1A'][0])
stopRAP1A  = (geneMIPindex_dict['RAP1A'][(len(geneMIPindex_dict['RAP1A']) - 1)])
# SIGIRR.
startSIGIRR = (geneMIPindex_dict['SIGIRR'][0])
stopSIGIRR  = (geneMIPindex_dict['SIGIRR'][(len(geneMIPindex_dict['SIGIRR']) - 1)])
# TIMD4.
startTIMD4 = (geneMIPindex_dict['TIMD4'][0])
stopTIMD4  = (geneMIPindex_dict['TIMD4'][(len(geneMIPindex_dict['TIMD4']) - 1)])
# TRAF6.
startTRAF6 = (geneMIPindex_dict['TRAF6'][0])
stopTRAF6  = (geneMIPindex_dict['TRAF6'][(len(geneMIPindex_dict['TRAF6']) - 1)])
# UVRAG.
startUVRAG = (geneMIPindex_dict['UVRAG'][0])
stopUVRAG  = (geneMIPindex_dict['UVRAG'][(len(geneMIPindex_dict['UVRAG']) - 1)])
# Start and stop information per gene collected.
logfile.write("Start and stop information per gene collected.\n")

# Compute summary statistics.
logfile.write("\n")
logfile.write("Compute summary statistics.\n")
logfile.write("(...)\n")
averages_df = pd.DataFrame(index=(covDepth_df.columns.values[3:]),
                           columns=('AIM2.mean', 'AIM2.min', 'AIM2.max', 'AIM2.median',
                                    'ATG16L1.mean', 'ATG16L1.min', 'ATG16L1.max', 'ATG16L1.median',
                                    'ATG5.mean', 'ATG5.min', 'ATG5.max', 'ATG5.median',
                                    'ATG7.mean', 'ATG7.min', 'ATG7.max', 'ATG7.median',
                                    'BECN1.mean', 'BECN1.min', 'BECN1.max', 'BECN1.median',
                                    'CASP1.mean', 'CASP1.min', 'CASP1.max', 'CASP1.median',
                                    'CYBA.mean', 'CYBA.min', 'CYBA.max', 'CYBA.median',
                                    'CYBB.mean', 'CYBB.min', 'CYBB.max', 'CYBB.median',
                                    'IL18.mean', 'IL18.min', 'IL18.max', 'IL18.median',
                                    'IL18BP.mean', 'IL18BP.min', 'IL18BP.max', 'IL18BP.median',
                                    'IL18R1.mean', 'IL18R1.min', 'IL18R1.max', 'IL18R1.median',
                                    'IL18RAP.mean', 'IL18RAP.min', 'IL18RAP.max', 'IL18RAP.median',
                                    'IL1A.mean', 'IL1A.min', 'IL1A.max', 'IL1A.median',
                                    'IL1B.mean', 'IL1B.min', 'IL1B.max', 'IL1B.median',
                                    'IL1F10.mean', 'IL1F10.min', 'IL1F10.max', 'IL1F10.median',
                                    'IL1R1.mean', 'IL1R1.min', 'IL1R1.max', 'IL1R1.median',
                                    'IL1R2.mean', 'IL1R2.min', 'IL1R2.max', 'IL1R2.median',
                                    'IL1RAP.mean', 'IL1RAP.min', 'IL1RAP.max', 'IL1RAP.median',
                                    'IL1RAPL1.mean', 'IL1RAPL1.min', 'IL1RAPL1.max', 'IL1RAPL1.median',
                                    'IL1RAPL2.mean', 'IL1RAPL2.min', 'IL1RAPL2.max', 'IL1RAPL2.median',
                                    'IL1RL1.mean', 'IL1RL1.min', 'IL1RL1.max', 'IL1RL1.median',
                                    'IL1RL2.mean', 'IL1RL2.min', 'IL1RL2.max', 'IL1RL2.median',
                                    'IL1RN.mean', 'IL1RN.min', 'IL1RN.max', 'IL1RN.median',
                                    'IL33.mean', 'IL33.min', 'IL33.max', 'IL33.median',
                                    'IL36A.mean', 'IL36A.min', 'IL36A.max', 'IL36A.median',
                                    'IL36B.mean', 'IL36B.min', 'IL36B.max', 'IL36B.median',
                                    'IL36G.mean', 'IL36G.min', 'IL36G.max', 'IL36G.median',
                                    'IL36RN.mean', 'IL36RN.min', 'IL36RN.max', 'IL36RN.median',
                                    'IL37.mean', 'IL37.min', 'IL37.max', 'IL37.median',
                                    'IRAK4.mean', 'IRAK4.min', 'IRAK4.max', 'IRAK4.median',
                                    'KIAA0226.mean', 'KIAA0226.min', 'KIAA0226.max', 'KIAA0226.median',
                                    'MAP1LC3A.mean', 'MAP1LC3A.min', 'MAP1LC3A.max', 'MAP1LC3A.median',
                                    'MYD88.mean', 'MYD88.min', 'MYD88.max', 'MYD88.median',
                                    'NCF1.mean', 'NCF1.min', 'NCF1.max', 'NCF1.median',
                                    'NCF2.mean', 'NCF2.min', 'NCF2.max', 'NCF2.median',
                                    'NCF4.mean', 'NCF4.min', 'NCF4.max', 'NCF4.median',
                                    'NLRP1.mean', 'NLRP1.min', 'NLRP1.max', 'NLRP1.median',
                                    'NLRP3.mean', 'NLRP3.min', 'NLRP3.max', 'NLRP3.median',
                                    'NOX4.mean', 'NOX4.min', 'NOX4.max', 'NOX4.median',
                                    'PIK3C3.mean', 'PIK3C3.min', 'PIK3C3.max', 'PIK3C3.median',
                                    'PYCARD.mean', 'PYCARD.min', 'PYCARD.max', 'PYCARD.median',
                                    'RAC1.mean', 'RAC1.min', 'RAC1.max', 'RAC1.median',
                                    'RAC2.mean', 'RAC2.min', 'RAC2.max', 'RAC2.median',
                                    'RAP1A.mean', 'RAP1A.min', 'RAP1A.max', 'RAP1A.median',
                                    'SIGIRR.mean', 'SIGIRR.min', 'SIGIRR.max', 'SIGIRR.median',
                                    'TIMD4.mean', 'TIMD4.min', 'TIMD4.max', 'TIMD4.median',
                                    'TRAF6.mean', 'TRAF6.min', 'TRAF6.max', 'TRAF6.median',
                                    'UVRAG.mean', 'UVRAG.min', 'UVRAG.max', 'UVRAG.median'),
                           data=np.nan)
# Define sampleIDs and compute summary statistics.
sampleIDs = covDepth_df.columns.values[3:]
for sample in sampleIDs:
    # AIM2.
    averages_df.loc[sample, 'AIM2.mean'] = covDepth_df.loc[startAIM2:stopAIM2, sample].mean()
    averages_df.loc[sample, 'AIM2.min'] = covDepth_df.loc[startAIM2:stopAIM2, sample].min()
    averages_df.loc[sample, 'AIM2.max'] = covDepth_df.loc[startAIM2:stopAIM2, sample].max()
    averages_df.loc[sample, 'AIM2.median'] = covDepth_df.loc[startAIM2:stopAIM2, sample].median()
    # ATG16L1.
    averages_df.loc[sample, 'ATG16L1.mean'] = covDepth_df.loc[startATG16L1:stopATG16L1, sample].mean()
    averages_df.loc[sample, 'ATG16L1.min'] = covDepth_df.loc[startATG16L1:stopATG16L1, sample].min()
    averages_df.loc[sample, 'ATG16L1.max'] = covDepth_df.loc[startATG16L1:stopATG16L1, sample].max()
    averages_df.loc[sample, 'ATG16L1.median'] = covDepth_df.loc[startATG16L1:stopATG16L1, sample].median()
    # ATG5.
    averages_df.loc[sample, 'ATG5.mean'] = covDepth_df.loc[startATG5:stopATG5, sample].mean()
    averages_df.loc[sample, 'ATG5.min'] = covDepth_df.loc[startATG5:stopATG5, sample].min()
    averages_df.loc[sample, 'ATG5.max'] = covDepth_df.loc[startATG5:stopATG5, sample].max()
    averages_df.loc[sample, 'ATG5.median'] = covDepth_df.loc[startATG5:stopATG5, sample].median()
    # ATG7.
    averages_df.loc[sample, 'ATG7.mean'] = covDepth_df.loc[startATG7:stopATG7, sample].mean()
    averages_df.loc[sample, 'ATG7.min'] = covDepth_df.loc[startATG7:stopATG7, sample].min()
    averages_df.loc[sample, 'ATG7.max'] = covDepth_df.loc[startATG7:stopATG7, sample].max()
    averages_df.loc[sample, 'ATG7.median'] = covDepth_df.loc[startATG7:stopATG7, sample].median()
    # BECN1.
    averages_df.loc[sample, 'BECN1.mean'] = covDepth_df.loc[startBECN1:stopBECN1, sample].mean()
    averages_df.loc[sample, 'BECN1.min'] = covDepth_df.loc[startBECN1:stopBECN1, sample].min()
    averages_df.loc[sample, 'BECN1.max'] = covDepth_df.loc[startBECN1:stopBECN1, sample].max()
    averages_df.loc[sample, 'BECN1.median'] = covDepth_df.loc[startBECN1:stopBECN1, sample].median()
    # CASP1.
    averages_df.loc[sample, 'CASP1.mean'] = covDepth_df.loc[startCASP1:stopCASP1, sample].mean()
    averages_df.loc[sample, 'CASP1.min'] = covDepth_df.loc[startCASP1:stopCASP1, sample].min()
    averages_df.loc[sample, 'CASP1.max'] = covDepth_df.loc[startCASP1:stopCASP1, sample].max()
    averages_df.loc[sample, 'CASP1.median'] = covDepth_df.loc[startCASP1:stopCASP1, sample].median()
    # CYBA.
    averages_df.loc[sample, 'CYBA.mean'] = covDepth_df.loc[startCYBA:stopCYBA, sample].mean()
    averages_df.loc[sample, 'CYBA.min'] = covDepth_df.loc[startCYBA:stopCYBA, sample].min()
    averages_df.loc[sample, 'CYBA.max'] = covDepth_df.loc[startCYBA:stopCYBA, sample].max()
    averages_df.loc[sample, 'CYBA.median'] = covDepth_df.loc[startCYBA:stopCYBA, sample].median()
    # CYBB.
    averages_df.loc[sample, 'CYBB.mean'] = covDepth_df.loc[startCYBB:stopCYBB, sample].mean()
    averages_df.loc[sample, 'CYBB.min'] = covDepth_df.loc[startCYBB:stopCYBB, sample].min()
    averages_df.loc[sample, 'CYBB.max'] = covDepth_df.loc[startCYBB:stopCYBB, sample].max()
    averages_df.loc[sample, 'CYBB.median'] = covDepth_df.loc[startCYBB:stopCYBB, sample].median()
    # IL18.
    averages_df.loc[sample, 'IL18.mean'] = covDepth_df.loc[startIL18:stopIL18, sample].mean()
    averages_df.loc[sample, 'IL18.min'] = covDepth_df.loc[startIL18:stopIL18, sample].min()
    averages_df.loc[sample, 'IL18.max'] = covDepth_df.loc[startIL18:stopIL18, sample].max()
    averages_df.loc[sample, 'IL18.median'] = covDepth_df.loc[startIL18:stopIL18, sample].median()
    # IL18BP.
    averages_df.loc[sample, 'IL18BP.mean'] = covDepth_df.loc[startIL18BP:stopIL18BP, sample].mean()
    averages_df.loc[sample, 'IL18BP.min'] = covDepth_df.loc[startIL18BP:stopIL18BP, sample].min()
    averages_df.loc[sample, 'IL18BP.max'] = covDepth_df.loc[startIL18BP:stopIL18BP, sample].max()
    averages_df.loc[sample, 'IL18BP.median'] = covDepth_df.loc[startIL18BP:stopIL18BP, sample].median()
    # IL18R1.
    averages_df.loc[sample, 'IL18R1.mean'] = covDepth_df.loc[startIL18R1:stopIL18R1, sample].mean()
    averages_df.loc[sample, 'IL18R1.min'] = covDepth_df.loc[startIL18R1:stopIL18R1, sample].min()
    averages_df.loc[sample, 'IL18R1.max'] = covDepth_df.loc[startIL18R1:stopIL18R1, sample].max()
    averages_df.loc[sample, 'IL18R1.median'] = covDepth_df.loc[startIL18R1:stopIL18R1, sample].median()
    # IL18RAP.
    averages_df.loc[sample, 'IL18RAP.mean'] = covDepth_df.loc[startIL18RAP:stopIL18RAP, sample].mean()
    averages_df.loc[sample, 'IL18RAP.min'] = covDepth_df.loc[startIL18RAP:stopIL18RAP, sample].min()
    averages_df.loc[sample, 'IL18RAP.max'] = covDepth_df.loc[startIL18RAP:stopIL18RAP, sample].max()
    averages_df.loc[sample, 'IL18RAP.median'] = covDepth_df.loc[startIL18RAP:stopIL18RAP, sample].median()
    # IL1A.
    averages_df.loc[sample, 'IL1A.mean'] = covDepth_df.loc[startIL1A:stopIL1A, sample].mean()
    averages_df.loc[sample, 'IL1A.min'] = covDepth_df.loc[startIL1A:stopIL1A, sample].min()
    averages_df.loc[sample, 'IL1A.max'] = covDepth_df.loc[startIL1A:stopIL1A, sample].max()
    averages_df.loc[sample, 'IL1A.median'] = covDepth_df.loc[startIL1A:stopIL1A, sample].median()
    # IL1B.
    averages_df.loc[sample, 'IL1B.mean'] = covDepth_df.loc[startIL1B:stopIL1B, sample].mean()
    averages_df.loc[sample, 'IL1B.min'] = covDepth_df.loc[startIL1B:stopIL1B, sample].min()
    averages_df.loc[sample, 'IL1B.max'] = covDepth_df.loc[startIL1B:stopIL1B, sample].max()
    averages_df.loc[sample, 'IL1B.median'] = covDepth_df.loc[startIL1B:stopIL1B, sample].median()
    # IL1F10.
    averages_df.loc[sample, 'IL1F10.mean'] = covDepth_df.loc[startIL1F10:stopIL1F10, sample].mean()
    averages_df.loc[sample, 'IL1F10.min'] = covDepth_df.loc[startIL1F10:stopIL1F10, sample].min()
    averages_df.loc[sample, 'IL1F10.max'] = covDepth_df.loc[startIL1F10:stopIL1F10, sample].max()
    averages_df.loc[sample, 'IL1F10.median'] = covDepth_df.loc[startIL1F10:stopIL1F10, sample].median()
    # IL1R1.
    averages_df.loc[sample, 'IL1R1.mean'] = covDepth_df.loc[startIL1R1:stopIL1R1, sample].mean()
    averages_df.loc[sample, 'IL1R1.min'] = covDepth_df.loc[startIL1R1:stopIL1R1, sample].min()
    averages_df.loc[sample, 'IL1R1.max'] = covDepth_df.loc[startIL1R1:stopIL1R1, sample].max()
    averages_df.loc[sample, 'IL1R1.median'] = covDepth_df.loc[startIL1R1:stopIL1R1, sample].median()
    # IL1R2.
    averages_df.loc[sample, 'IL1R2.mean'] = covDepth_df.loc[startIL1R2:stopIL1R2, sample].mean()
    averages_df.loc[sample, 'IL1R2.min'] = covDepth_df.loc[startIL1R2:stopIL1R2, sample].min()
    averages_df.loc[sample, 'IL1R2.max'] = covDepth_df.loc[startIL1R2:stopIL1R2, sample].max()
    averages_df.loc[sample, 'IL1R2.median'] = covDepth_df.loc[startIL1R2:stopIL1R2, sample].median()
    # IL1RAP.
    averages_df.loc[sample, 'IL1RAP.mean'] = covDepth_df.loc[startIL1RAP:stopIL1RAP, sample].mean()
    averages_df.loc[sample, 'IL1RAP.min'] = covDepth_df.loc[startIL1RAP:stopIL1RAP, sample].min()
    averages_df.loc[sample, 'IL1RAP.max'] = covDepth_df.loc[startIL1RAP:stopIL1RAP, sample].max()
    averages_df.loc[sample, 'IL1RAP.median'] = covDepth_df.loc[startIL1RAP:stopIL1RAP, sample].median()
    # IL1RAPL1.
    averages_df.loc[sample, 'IL1RAPL1.mean'] = covDepth_df.loc[startIL1RAPL1:stopIL1RAPL1, sample].mean()
    averages_df.loc[sample, 'IL1RAPL1.min'] = covDepth_df.loc[startIL1RAPL1:stopIL1RAPL1, sample].min()
    averages_df.loc[sample, 'IL1RAPL1.max'] = covDepth_df.loc[startIL1RAPL1:stopIL1RAPL1, sample].max()
    averages_df.loc[sample, 'IL1RAPL1.median'] = covDepth_df.loc[startIL1RAPL1:stopIL1RAPL1, sample].median()
    # IL1RAPL2.
    averages_df.loc[sample, 'IL1RAPL2.mean'] = covDepth_df.loc[startIL1RAPL2:stopIL1RAPL2, sample].mean()
    averages_df.loc[sample, 'IL1RAPL2.min'] = covDepth_df.loc[startIL1RAPL2:stopIL1RAPL2, sample].min()
    averages_df.loc[sample, 'IL1RAPL2.max'] = covDepth_df.loc[startIL1RAPL2:stopIL1RAPL2, sample].max()
    averages_df.loc[sample, 'IL1RAPL2.median'] = covDepth_df.loc[startIL1RAPL2:stopIL1RAPL2, sample].median()
    # IL1RL1.
    averages_df.loc[sample, 'IL1RL1.mean'] = covDepth_df.loc[startIL1RL1:stopIL1RL1, sample].mean()
    averages_df.loc[sample, 'IL1RL1.min'] = covDepth_df.loc[startIL1RL1:stopIL1RL1, sample].min()
    averages_df.loc[sample, 'IL1RL1.max'] = covDepth_df.loc[startIL1RL1:stopIL1RL1, sample].max()
    averages_df.loc[sample, 'IL1RL1.median'] = covDepth_df.loc[startIL1RL1:stopIL1RL1, sample].median()
    # IL1RL2.
    averages_df.loc[sample, 'IL1RL2.mean'] = covDepth_df.loc[startIL1RL2:stopIL1RL2, sample].mean()
    averages_df.loc[sample, 'IL1RL2.min'] = covDepth_df.loc[startIL1RL2:stopIL1RL2, sample].min()
    averages_df.loc[sample, 'IL1RL2.max'] = covDepth_df.loc[startIL1RL2:stopIL1RL2, sample].max()
    averages_df.loc[sample, 'IL1RL2.median'] = covDepth_df.loc[startIL1RL2:stopIL1RL2, sample].median()
    # IL1RN.
    averages_df.loc[sample, 'IL1RN.mean'] = covDepth_df.loc[startIL1RN:stopIL1RN, sample].mean()
    averages_df.loc[sample, 'IL1RN.min'] = covDepth_df.loc[startIL1RN:stopIL1RN, sample].min()
    averages_df.loc[sample, 'IL1RN.max'] = covDepth_df.loc[startIL1RN:stopIL1RN, sample].max()
    averages_df.loc[sample, 'IL1RN.median'] = covDepth_df.loc[startIL1RN:stopIL1RN, sample].median()
    # IL33.
    averages_df.loc[sample, 'IL33.mean'] = covDepth_df.loc[startIL33:stopIL33, sample].mean()
    averages_df.loc[sample, 'IL33.min'] = covDepth_df.loc[startIL33:stopIL33, sample].min()
    averages_df.loc[sample, 'IL33.max'] = covDepth_df.loc[startIL33:stopIL33, sample].max()
    averages_df.loc[sample, 'IL33.median'] = covDepth_df.loc[startIL33:stopIL33, sample].median()
    # IL36A.
    averages_df.loc[sample, 'IL36A.mean'] = covDepth_df.loc[startIL36A:stopIL36A, sample].mean()
    averages_df.loc[sample, 'IL36A.min'] = covDepth_df.loc[startIL36A:stopIL36A, sample].min()
    averages_df.loc[sample, 'IL36A.max'] = covDepth_df.loc[startIL36A:stopIL36A, sample].max()
    averages_df.loc[sample, 'IL36A.median'] = covDepth_df.loc[startIL36A:stopIL36A, sample].median()
    # IL36B.
    averages_df.loc[sample, 'IL36B.mean'] = covDepth_df.loc[startIL36B:stopIL36B, sample].mean()
    averages_df.loc[sample, 'IL36B.min'] = covDepth_df.loc[startIL36B:stopIL36B, sample].min()
    averages_df.loc[sample, 'IL36B.max'] = covDepth_df.loc[startIL36B:stopIL36B, sample].max()
    averages_df.loc[sample, 'IL36B.median'] = covDepth_df.loc[startIL36B:stopIL36B, sample].median()
    # IL36G.
    averages_df.loc[sample, 'IL36G.mean'] = covDepth_df.loc[startIL36G:stopIL36G, sample].mean()
    averages_df.loc[sample, 'IL36G.min'] = covDepth_df.loc[startIL36G:stopIL36G, sample].min()
    averages_df.loc[sample, 'IL36G.max'] = covDepth_df.loc[startIL36G:stopIL36G, sample].max()
    averages_df.loc[sample, 'IL36G.median'] = covDepth_df.loc[startIL36G:stopIL36G, sample].median()
    # IL36RN.
    averages_df.loc[sample, 'IL36RN.mean'] = covDepth_df.loc[startIL36RN:stopIL36RN, sample].mean()
    averages_df.loc[sample, 'IL36RN.min'] = covDepth_df.loc[startIL36RN:stopIL36RN, sample].min()
    averages_df.loc[sample, 'IL36RN.max'] = covDepth_df.loc[startIL36RN:stopIL36RN, sample].max()
    averages_df.loc[sample, 'IL36RN.median'] = covDepth_df.loc[startIL36RN:stopIL36RN, sample].median()
    # IL37.
    averages_df.loc[sample, 'IL37.mean'] = covDepth_df.loc[startIL37:stopIL37, sample].mean()
    averages_df.loc[sample, 'IL37.min'] = covDepth_df.loc[startIL37:stopIL37, sample].min()
    averages_df.loc[sample, 'IL37.max'] = covDepth_df.loc[startIL37:stopIL37, sample].max()
    averages_df.loc[sample, 'IL37.median'] = covDepth_df.loc[startIL37:stopIL37, sample].median()
    # IRAK4.
    averages_df.loc[sample, 'IRAK4.mean'] = covDepth_df.loc[startIRAK4:stopIRAK4, sample].mean()
    averages_df.loc[sample, 'IRAK4.min'] = covDepth_df.loc[startIRAK4:stopIRAK4, sample].min()
    averages_df.loc[sample, 'IRAK4.max'] = covDepth_df.loc[startIRAK4:stopIRAK4, sample].max()
    averages_df.loc[sample, 'IRAK4.median'] = covDepth_df.loc[startIRAK4:stopIRAK4, sample].median()
    # KIAA0226.
    averages_df.loc[sample, 'KIAA0226.mean'] = covDepth_df.loc[startKIAA0226:stopKIAA0226, sample].mean()
    averages_df.loc[sample, 'KIAA0226.min'] = covDepth_df.loc[startKIAA0226:stopKIAA0226, sample].min()
    averages_df.loc[sample, 'KIAA0226.max'] = covDepth_df.loc[startKIAA0226:stopKIAA0226, sample].max()
    averages_df.loc[sample, 'KIAA0226.median'] = covDepth_df.loc[startKIAA0226:stopKIAA0226, sample].median()
    # MAP1LC3A.
    averages_df.loc[sample, 'MAP1LC3A.mean'] = covDepth_df.loc[startMAP1LC3A:stopMAP1LC3A, sample].mean()
    averages_df.loc[sample, 'MAP1LC3A.min'] = covDepth_df.loc[startMAP1LC3A:stopMAP1LC3A, sample].min()
    averages_df.loc[sample, 'MAP1LC3A.max'] = covDepth_df.loc[startMAP1LC3A:stopMAP1LC3A, sample].max()
    averages_df.loc[sample, 'MAP1LC3A.median'] = covDepth_df.loc[startMAP1LC3A:stopMAP1LC3A, sample].median()
    # MYD88.
    averages_df.loc[sample, 'MYD88.mean'] = covDepth_df.loc[startMYD88:stopMYD88, sample].mean()
    averages_df.loc[sample, 'MYD88.min'] = covDepth_df.loc[startMYD88:stopMYD88, sample].min()
    averages_df.loc[sample, 'MYD88.max'] = covDepth_df.loc[startMYD88:stopMYD88, sample].max()
    averages_df.loc[sample, 'MYD88.median'] = covDepth_df.loc[startMYD88:stopMYD88, sample].median()
    # NCF1.
    averages_df.loc[sample, 'NCF1.mean'] = covDepth_df.loc[startNCF1:stopNCF1, sample].mean()
    averages_df.loc[sample, 'NCF1.min'] = covDepth_df.loc[startNCF1:stopNCF1, sample].min()
    averages_df.loc[sample, 'NCF1.max'] = covDepth_df.loc[startNCF1:stopNCF1, sample].max()
    averages_df.loc[sample, 'NCF1.median'] = covDepth_df.loc[startNCF1:stopNCF1, sample].median()
    # NCF2.
    averages_df.loc[sample, 'NCF2.mean'] = covDepth_df.loc[startNCF2:stopNCF2, sample].mean()
    averages_df.loc[sample, 'NCF2.min'] = covDepth_df.loc[startNCF2:stopNCF2, sample].min()
    averages_df.loc[sample, 'NCF2.max'] = covDepth_df.loc[startNCF2:stopNCF2, sample].max()
    averages_df.loc[sample, 'NCF2.median'] = covDepth_df.loc[startNCF2:stopNCF2, sample].median()
    # NCF4.
    averages_df.loc[sample, 'NCF4.mean'] = covDepth_df.loc[startNCF4:stopNCF4, sample].mean()
    averages_df.loc[sample, 'NCF4.min'] = covDepth_df.loc[startNCF4:stopNCF4, sample].min()
    averages_df.loc[sample, 'NCF4.max'] = covDepth_df.loc[startNCF4:stopNCF4, sample].max()
    averages_df.loc[sample, 'NCF4.median'] = covDepth_df.loc[startNCF4:stopNCF4, sample].median()
    # NLRP1.
    averages_df.loc[sample, 'NLRP1.mean'] = covDepth_df.loc[startNLRP1:stopNLRP1, sample].mean()
    averages_df.loc[sample, 'NLRP1.min'] = covDepth_df.loc[startNLRP1:stopNLRP1, sample].min()
    averages_df.loc[sample, 'NLRP1.max'] = covDepth_df.loc[startNLRP1:stopNLRP1, sample].max()
    averages_df.loc[sample, 'NLRP1.median'] = covDepth_df.loc[startNLRP1:stopNLRP1, sample].median()
    # NLRP3.
    averages_df.loc[sample, 'NLRP3.mean'] = covDepth_df.loc[startNLRP3:stopNLRP3, sample].mean()
    averages_df.loc[sample, 'NLRP3.min'] = covDepth_df.loc[startNLRP3:stopNLRP3, sample].min()
    averages_df.loc[sample, 'NLRP3.max'] = covDepth_df.loc[startNLRP3:stopNLRP3, sample].max()
    averages_df.loc[sample, 'NLRP3.median'] = covDepth_df.loc[startNLRP3:stopNLRP3, sample].median()
    # NOX4.
    averages_df.loc[sample, 'NOX4.mean'] = covDepth_df.loc[startNOX4:stopNOX4, sample].mean()
    averages_df.loc[sample, 'NOX4.min'] = covDepth_df.loc[startNOX4:stopNOX4, sample].min()
    averages_df.loc[sample, 'NOX4.max'] = covDepth_df.loc[startNOX4:stopNOX4, sample].max()
    averages_df.loc[sample, 'NOX4.median'] = covDepth_df.loc[startNOX4:stopNOX4, sample].median()
    # PIK3C3.
    averages_df.loc[sample, 'PIK3C3.mean'] = covDepth_df.loc[startPIK3C3:stopPIK3C3, sample].mean()
    averages_df.loc[sample, 'PIK3C3.min'] = covDepth_df.loc[startPIK3C3:stopPIK3C3, sample].min()
    averages_df.loc[sample, 'PIK3C3.max'] = covDepth_df.loc[startPIK3C3:stopPIK3C3, sample].max()
    averages_df.loc[sample, 'PIK3C3.median'] = covDepth_df.loc[startPIK3C3:stopPIK3C3, sample].median()
    # PYCARD.
    averages_df.loc[sample, 'PYCARD.mean'] = covDepth_df.loc[startPYCARD:stopPYCARD, sample].mean()
    averages_df.loc[sample, 'PYCARD.min'] = covDepth_df.loc[startPYCARD:stopPYCARD, sample].min()
    averages_df.loc[sample, 'PYCARD.max'] = covDepth_df.loc[startPYCARD:stopPYCARD, sample].max()
    averages_df.loc[sample, 'PYCARD.median'] = covDepth_df.loc[startPYCARD:stopPYCARD, sample].median()
    # RAC1.
    averages_df.loc[sample, 'RAC1.mean'] = covDepth_df.loc[startRAC1:stopRAC1, sample].mean()
    averages_df.loc[sample, 'RAC1.min'] = covDepth_df.loc[startRAC1:stopRAC1, sample].min()
    averages_df.loc[sample, 'RAC1.max'] = covDepth_df.loc[startRAC1:stopRAC1, sample].max()
    averages_df.loc[sample, 'RAC1.median'] = covDepth_df.loc[startRAC1:stopRAC1, sample].median()
    # RAC2.
    averages_df.loc[sample, 'RAC2.mean'] = covDepth_df.loc[startRAC2:stopRAC2, sample].mean()
    averages_df.loc[sample, 'RAC2.min'] = covDepth_df.loc[startRAC2:stopRAC2, sample].min()
    averages_df.loc[sample, 'RAC2.max'] = covDepth_df.loc[startRAC2:stopRAC2, sample].max()
    averages_df.loc[sample, 'RAC2.median'] = covDepth_df.loc[startRAC2:stopRAC2, sample].median()
    # RAP1A.
    averages_df.loc[sample, 'RAP1A.mean'] = covDepth_df.loc[startRAP1A:stopRAP1A, sample].mean()
    averages_df.loc[sample, 'RAP1A.min'] = covDepth_df.loc[startRAP1A:stopRAP1A, sample].min()
    averages_df.loc[sample, 'RAP1A.max'] = covDepth_df.loc[startRAP1A:stopRAP1A, sample].max()
    averages_df.loc[sample, 'RAP1A.median'] = covDepth_df.loc[startRAP1A:stopRAP1A, sample].median()
    # SIGIRR.
    averages_df.loc[sample, 'SIGIRR.mean'] = covDepth_df.loc[startSIGIRR:stopSIGIRR, sample].mean()
    averages_df.loc[sample, 'SIGIRR.min'] = covDepth_df.loc[startSIGIRR:stopSIGIRR, sample].min()
    averages_df.loc[sample, 'SIGIRR.max'] = covDepth_df.loc[startSIGIRR:stopSIGIRR, sample].max()
    averages_df.loc[sample, 'SIGIRR.median'] = covDepth_df.loc[startSIGIRR:stopSIGIRR, sample].median()
    # TIMD4.
    averages_df.loc[sample, 'TIMD4.mean'] = covDepth_df.loc[startTIMD4:stopTIMD4, sample].mean()
    averages_df.loc[sample, 'TIMD4.min'] = covDepth_df.loc[startTIMD4:stopTIMD4, sample].min()
    averages_df.loc[sample, 'TIMD4.max'] = covDepth_df.loc[startTIMD4:stopTIMD4, sample].max()
    averages_df.loc[sample, 'TIMD4.median'] = covDepth_df.loc[startTIMD4:stopTIMD4, sample].median()
    # TRAF6.
    averages_df.loc[sample, 'TRAF6.mean'] = covDepth_df.loc[startTRAF6:stopTRAF6, sample].mean()
    averages_df.loc[sample, 'TRAF6.min'] = covDepth_df.loc[startTRAF6:stopTRAF6, sample].min()
    averages_df.loc[sample, 'TRAF6.max'] = covDepth_df.loc[startTRAF6:stopTRAF6, sample].max()
    averages_df.loc[sample, 'TRAF6.median'] = covDepth_df.loc[startTRAF6:stopTRAF6, sample].median()
    # UVRAG.
    averages_df.loc[sample, 'UVRAG.mean'] = covDepth_df.loc[startUVRAG:stopUVRAG, sample].mean()
    averages_df.loc[sample, 'UVRAG.min'] = covDepth_df.loc[startUVRAG:stopUVRAG, sample].min()
    averages_df.loc[sample, 'UVRAG.max'] = covDepth_df.loc[startUVRAG:stopUVRAG, sample].max()
    averages_df.loc[sample, 'UVRAG.median'] = covDepth_df.loc[startUVRAG:stopUVRAG, sample].median()
# Summary statistics computed.
logfile.write("Summary statistics per gene computed.\n")

# Write out summary statistics.
SUMSTATS = COHORT + "_mergedCoverages_summaryStatistics_" + DATE + ".txt"
averages_df.to_csv(DIRECTORYcov + SUMSTATS, sep = '\t', index = True)
logfile.write("\n")
logfile.write("Summary statistics written to file.\n")

# All done, write log, and finally close logFile.
print("All done.")
logfile.write("\n")
logfile.write("All done.\n")
logfile.close()
