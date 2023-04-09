echo 'NEA script starded'

while read hash;
do
  echo "cd ../ImageMagick"
  cd ../ImageMagick

  echo "git checkout -f ${hash}"
  git checkout -f "${hash}"

  echo "git log -1 --pretty=format:'%ae'"
  author=($(git log -1 --pretty=format:'%ae'))

  echo 'git log -n2 | grep -o -E -e "[0-9a-f]{40}$"'
  commits=($(git log -n2 | grep -o -E -e "[0-9a-f]{40}$"))

  echo "git checkout -f ${commits[1]}"
  git checkout -f ${commits[1]}

  echo "Running git blame on commit files"
  modified_lines=()
  while read file;
  do
    echo "git blame -e "${file}" | grep -o -E -e ${author}"
    blame=$(git blame -e "${file}" | grep -o -E -e "${author}")
    if [ -n "$blame" ];
    then
      modified_lines+=1;
    fi

  done < ../deps/modified-files/${hash}.out

  echo "Setting NEA status"
  if [ -n "$modified_lines" ];
  then
    echo "${hash}: Não" >> "../NEA/is-nea.out" 
  else
    echo "${hash}: Sim" >> "../NEA/is-nea.out" 
  fi
done < ../hashes.txt

echo 'NEA script ended'