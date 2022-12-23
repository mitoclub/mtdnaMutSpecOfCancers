# mtdnaMutSpecOfCancers

This repo contains all data and analyses for cancer part of mtDNA MutSpec project.

## Download human mtDNA refseqs

```bash
esearch -db nucleotide -query "ddbj_embl_genbank[filter] AND txid9606[orgn:noexp] AND complete-genome[title] AND mitochondrion[filter]" | efetch -format gb > human_mt.gb
```
