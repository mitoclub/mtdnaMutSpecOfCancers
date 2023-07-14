# mtdnaMutSpecOfCancers

This repo contains all data and analyses for cancer part of mtDNA MutSpec project.

## Download human mtDNA refseqs

```bash
esearch -db nucleotide -query "ddbj_embl_genbank[filter] AND txid9606[orgn:noexp] AND complete-genome[title] AND mitochondrion[filter]" | efetch -format gb > human_mt.gb
```

## References

1. Yuan, Y., Ju, Y.S., Kim, Y. et al. Comprehensive molecular characterization of mitochondrial genomes in human cancers. Nat Genet 52, 342–352 (2020). https://doi.org/10.1038/s41588-019-0557-x
2. [Used Data](https://ibl.mdanderson.org/tcma/download.html)
