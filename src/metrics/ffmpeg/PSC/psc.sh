echo 'PSC script starded'

while read hash;
do
  echo "cd ../FFmpeg"
  cd ../FFmpeg

  echo "git checkout -f ${hash}"
  git checkout -f "${hash}"

  echo "git log -1 --pretty=format:'%ae'"
  author=($(git log -1 --pretty=format:'%ae'))

  total_authors=$(<../deps/authors/${hash}.out)
  other_authors=${total_authors//$author/}

  total_authors=($total_authors)
  total_authors=${#total_authors[@]}
  echo "Total authors: ${total_authors}"

  other_authors=($other_authors)
  other_authors=${#other_authors[@]}
  echo "Other authors: ${other_authors}"

  psc=$(bc <<< "scale=2; 100 - ($other_authors * 100) / $total_authors")
  echo "${hash}: $psc" >> "../PSC/psc.out"
done < ../hashes.txt

echo 'PSC script ended'