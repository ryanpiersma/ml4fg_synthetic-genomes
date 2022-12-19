import h5py
import numpy as np
import random
import pandas as pd

snps = h5py.File('imputed_snps_binary.hdf5', 'r')

maf5_snps = []
sampled_snps = []
sample_indices = []

snps_processed = 0
progress_indicator = 1000000
samples = 10000

#Filter for MAF >5% SNPs
for snp in snps['snps']:
    snps_processed += 1
    if snps_processed % progress_indicator == 0:
        print(snps_processed)
    if ((np.count_nonzero(snp) / len(snp)) >= 0.05) and ((np.count_nonzero(snp) / len(snp)) <= 0.95):
        maf5_snps.append(snp)

print(len(maf5_snps))
print(str(len(maf5_snps)/len(snps['snps']) * 100) + " % are MAF >5% SNPs")

#Sample from MAF >% SNPs
for i in range(samples):
    curr_len = len(maf5_snps)
    sample_index = random.randint(0, curr_len-1)
    #Avoid sampling same snp
    while sample_index in sample_indices:
        sample_index = random.randint(0, curr_len-1)
    sample_indices.append(sample_index)
    sampled_snps.append(maf5_snps[sample_index])

snp_frame = pd.DataFrame(sampled_snps)
#Transpose for haplotype format
snp_frame = snp_frame.T

extra_col = []
for i in len(snp_frame[0]):
    extra_col.append("Real")

snp_frame.to_csv('arabidopsis_10k_sampled.hapt',header=None)
