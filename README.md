# ml4fg_synthetic-genomes
Code+data used for Machine Learning for Functional Genomics class project

**`snp_distribution.py`**
- EDA script used to visualize the distribution of SNPs over accessions of Arabidopsis thaliana

**`snp_sampler.py`**
- Script used to process raw hdf5 file from 1001 Genomes, filter for MAF >5% SNPs, then sample 10K of them in order to be able to input into GAN models

**`gan_script.py`**
- Script used to train GANs to produce synthetic Arabidopsis thaliana genomes. Largely adopted from https://gitlab.inria.fr/ml_genetics/public/artificial_genomes/-/tree/master/

**`arabidopsis_10k_sampled.hapt`**
- The data resulting from running `snp_sampler.py` that was input into the GANs
