import requests
from multiprocessing import Process
from threading import Thread

from constants import GENE_SNP_URL, UNIPROT_ID_URL


class Runner:

    @staticmethod
    def _fetch_data(url):
        try:
            result = requests.get(url)
            result.raise_for_status()
            return result.json()
        except requests.RequestException as e:
            print(f"Request failed: {e}")
            return None

    @staticmethod
    def _get_snps(gene):
        url = GENE_SNP_URL.replace("{GENE_NAME}", gene)

        result = Runner._fetch_data(url)
        if result:
            print(f"{gene}\n{result.get("esearchresult").get("idlist")}\n")
        else:
            print(f"Failed to retrieve SNPs for {gene}")

    @staticmethod
    def _get_uniprot(gene):
        url = UNIPROT_ID_URL.replace("{GENE_NAME}", gene)
        result = Runner._fetch_data(url)
        if result:
            try:
                print(f"{gene}\n{result.get("results")[0].get("primaryAccession")}\n")
            except IndexError as e:
                print(e)
        else:
            print(f"Failed to retrieve UniProt ID for {gene}")

    @staticmethod
    def _run_request(function, gene_list, mode):
        if mode == "sync":
            for gene in gene_list:
                function(gene)

        if mode == "threads":
            threads = [Thread(target=function, args=(gene,)) for gene in gene_list]
            for thread in threads:
                thread.start()

            for thread in threads:
                thread.join()

        if mode == "processes":
            processes = [Process(target=function, args=(gene,)) for gene in gene_list]
            for process in processes:
                process.start()

            for process in processes:
                process.join()

    @staticmethod
    def run_nsbi_request(gene_list, mode):
        Runner._run_request(Runner._get_snps, gene_list, mode)

    @staticmethod
    def run_uniprot_request(gene_list, mode):
        Runner._run_request(Runner._get_uniprot, gene_list, mode)
