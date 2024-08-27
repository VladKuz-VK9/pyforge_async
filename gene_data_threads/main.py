import time

from constants import OPTIONS
from functions import Runner


genes_1 = ("BRAF", "KRAS", "PTEN", "NF1", "INS", "EGFR")
genes_2 = genes_1 + ("ALAS1", "APEH", "BTD", "CRBN", "DCLK3", "DLEC1", "EAF1", "FOXP1", "HACL1", "HEMK1")


if __name__ == "__main__":
    start = time.time()

    # use run_ncbi_request or run_uniprot_request method,
    # change the geneset (genes_1, genes_2),
    # change the option using OPTIONS (synchronous, threads, processes)
    Runner.run_uniprot_request(genes_2, OPTIONS.SYNCHRONOUS.value)

    end = time.time()
    print(f"{end - start:.2f} seconds")
