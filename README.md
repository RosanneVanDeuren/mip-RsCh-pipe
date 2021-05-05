# **mip-RsCh-pipeline**

This pipeline processes Molecular Inversion Probe (MIP) sequencing data to ensure reliable common and rare genetic variant calls. 


## **Overview**

The script-names (STEP-number) specify the order in which the scripts need to be executed to complete the pipeline process.
In short, the following filters / checks are executed:
1. A read-filter is applied (STEP1)
2. A coverage-check is performed (STEP2, 3a, 3b, 4, 5, 6)
3. Variant calling by GATK UnifiedGenotyper (STEP7a, 7b, 8)
4. A rare variant filter on vcf QUAL >= 1000 (STEP9)
5. Mpileup-statistics-filter (STEP10, 11, 12, 13)
6. Variant annotation, using our inhouse annotation service (STEP14a, 14b, 14c, 15)

# **Input**
Sorted bamfiles for all samples in your cohort.

# **Output**
A merged variant file (tab-separated txt) from all samples in your cohort combined.


## **Requirements**

- Python2.7 (modules: pysam, numpy, pandas)
- bedtools v2.29.1 (https://bedtools.readthedocs.io/en/latest/content/installation.html)
- The Genome Analysis Toolkit (GATK) v3.8-1 (https://github.com/broadgsa/gatk/releases/tag/3.8-1)
- bcftools 1.6 (http://www.htslib.org/download/)
- samtools 1.6 (http://www.htslib.org/download/)
- pileup2base (https://github.com/riverlee/pileup2base.git)

Reference files:
- dbsnp_137.hg19.vcf (https://ftp.ncbi.nih.gov/snp/organisms/human_9606/VCF/00-All.vcf.gz)
- ref_hg19.fasta (including accompanying ref_hg19.fasta.fai, ref_hg19.dict, and ref_hg19.dict.fai) (http://hgdownload.cse.ucsc.edu/goldenPath/hg19/chromosomes/)
- targetCallingFile_il1mips.bed (see ./refFiles)
- baseCovDepthDF_il1mipTargetRegion.txt (see ./refFiles)
- dbSnp150common_il1mipTargetRegion_COMMONadjRC_CHR.txt (see ./refFiles)


## **Additional Information**

The current version of this pipeline has been applied to the MIP-sequencing data used in the following publications:
- Kluck V, ***van Deuren RC***, Cavalli G, Shaukat A, Arts P, Cleophas MC, et al. Rare genetic variants in interleukin-37 link this anti-inflammatory cytokine to the pathogenesis and treatment of gout. Ann Rheum Dis. 2020;79(4):536-44.
- ***van Deuren RC***, Arts P, Cavalli G, Jaeger M, Steehouwer M, et al. Impact of rare and common genetic variation in the Interleukin-1 pathway on human cytokine responses. bioRxiv. 2020:949602v3.
 
An automated version of this pipeline is in progress, the link will appear here.

**Author**  : Rosanne C. van Deuren
**Contact** : Rosanne.vanDeuren@radboudumc.nl
