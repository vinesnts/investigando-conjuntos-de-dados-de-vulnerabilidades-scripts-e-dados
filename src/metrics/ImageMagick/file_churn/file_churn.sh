echo 'File Churn script starded'

while read hash;
do

  echo "cd ../ImageMagick"
  cd ../ImageMagick

  echo "git checkout -f ${hash}"
  git checkout -f "${hash}"

  total_files=$(<../deps/modified-files/${hash}.out)

  total_files=($total_files)

  total_files=${#total_files[@]}
  echo "Total of changed files: ${total_files}"

  echo "${hash}: $total_files" >> "../file_churn/file_churn.out"
done < ../hashes.txt

echo 'File Churn script ended'