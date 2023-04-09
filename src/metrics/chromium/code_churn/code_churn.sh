echo 'Code Churn script starded'

while read hash;
do

  echo "cd ../chromium"
  cd ../chromium

  echo "git checkout -f ${hash}"
  git checkout -f "${hash}"

  added_lines=0
  while read file;
  do
    lines=($file)

    number_of_lines=${#lines[@]}

    added_lines=$(($added_lines+$number_of_lines-1))
  done < "../deps/added-lines/${hash}.out"

  removed_lines=0
  while read file;
  do
    lines=($file)

    number_of_lines=${#lines[@]}

    removed_lines=$(($removed_lines+$number_of_lines-1))
  done < "../deps/lines/${hash}.out"

  code_churn=$(($added_lines+$removed_lines))
  echo "Total of changed lines: ${code_churn}"

  echo "${hash}: $code_churn" >> "../code_churn/code_churn.out"
done < ../hashes.txt

echo 'Code Churn script ended'