for file in *.fq; 
do 
grep '+' $file | ^C -l >> readCounts; 
done
ls *.fq > names
paste -d, names readCounts > counts
