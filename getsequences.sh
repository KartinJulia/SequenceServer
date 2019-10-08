awk "/^>/ {n++} n>10 {exit} {print}" inputfile.fa >outputfile.fa
