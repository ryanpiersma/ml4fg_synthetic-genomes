import h5py
import numpy as np
import matplotlib.pyplot as plt

snps = h5py.File('imputed_snps_binary.hdf5', 'r')
print(list(snps.keys()))
print(snps['snps'].shape)

num_accessions = []
progress_step = 100000
progress = 0

for entry in snps['snps']:
    num_accessions.append(np.sum(entry))
    progress += 1
    if progress % progress_step == 0:
        print(progress)

plt.hist(num_accessions)
plt.grid()
plt.title("Distribution of SNPs")
plt.xlabel("Number of accessions with a given SNP")
plt.ylabel("SNPs")
plt.savefig("snps.png")

