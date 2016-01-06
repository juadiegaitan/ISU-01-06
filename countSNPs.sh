for file in *.snps.tsv ; 
do 
wc -l $file >> SNPS; 
done
cut -d' ' SNPS -f2 > files
cut -d' ' SNPS -f1 > sites
paste -d, sites files > putativeSNPs 
