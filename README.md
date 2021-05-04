# **mip-RsCh-pipeline**

Process research Molecular Inversion Probe (MIP) sequencing data to ensure reliable common and rare genetic variant calls for the purpose of cohort based analyses.

## **Instructions**

## **Dependencies**

This pipeline uses is built up from a combination of Bash and Python scripts. Python version 2.7 is used, with the following modules installed:
- pysam
- numpy
- pandas

In addition, please make sure that you have the following tools available on your system:
- bedtools v2.29.1 (https://bedtools.readthedocs.io/en/latest/content/installation.html)
- The Genome Analysis Toolkit (GATK) v3.8-1 ()
- bcftools 1.6 (http://www.htslib.org/download/)
- samtools 1.6 (http://www.htslib.org/download/)
- pileup2base (https://github.com/riverlee/pileup2base.git)

And finally, please download the following files into your "refFiles"-folder (see STEP0.Manual_mip-RsCh-pipe_preparations.txt):
- dbsnp_137.hg19.vcf (https://ftp.ncbi.nih.gov/snp/organisms/human_9606/VCF/00-All.vcf.gz)
- ref_hg19.fasta with accompanying ref_hg19.fasta.fai, ref_hg19.dict, and ref_hg19.dict.fai (http://hgdownload.cse.ucsc.edu/goldenPath/hg19/chromosomes/)

## **Meta**

An automated version of this pipeline is in progress. The link will appear here.
