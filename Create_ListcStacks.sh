find ./ustacks_output/ >files
uniq no_names > uniques
sed -i '2,121s/^/-s /g' cstacks_with_files
sed -i 's/$/ \/g' cstacks_with_files
chmod +x cstacks_with_files
