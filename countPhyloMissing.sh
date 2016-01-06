while read line; do echo "$line" | tr -cd  "N" | wc -c; done <sb323390.nex> sb32390_counts
