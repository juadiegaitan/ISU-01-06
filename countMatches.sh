for file in *matches.tsv; 
do 
wc -l $file >> matchLength; 
done
cut -d' ' -f1 matchLength > length
cut -d' ' -f2 matchLength > names
paste -d, length names > matchInfo
