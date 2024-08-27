from enum import Enum


GENE_SNP_URL = ("https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=snp&term="
                "{GENE_NAME}[Gene Name]&retmode=json")

UNIPROT_ID_URL = ("https://rest.uniprot.org/uniprotkb/search?query={GENE_NAME}+AND+reviewed:true+AND+organism_id:9606"
                  "&format=json&size=1&fields=id")


class OPTIONS(Enum):
    SYNCHRONOUS = 'sync'
    THREADS = 'threads'
    PROCESSES = 'processes'
