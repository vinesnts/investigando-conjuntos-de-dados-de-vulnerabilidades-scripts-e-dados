echo 'deps scripts starded'

while read hash;
do

  echo "cd ../linux"
  cd ../linux

  echo "git checkout -f ${hash}"
  git checkout -f "${hash}"

  echo "git diff --name-only HEAD~1"
  git diff --name-only HEAD~1 > "../deps/modified-files/${hash}.out"

  if [ ! -f "../deps/lines/${hash}.out" ];
  then

    while read file;
    do
      echo "git log -1 -p -U0 -- "${file}" | grep -o -E '^\@{2}\s\-[0-9]+\,*[0-9]*'"
      lines=$(git log -1 -p -U0 -- "${file}" | grep -o -E '^\@{2}\s\-[0-9]+\,*[0-9]*')

      echo "git log -1 -p -U0 -- ""${file}"" | grep -o -E '^\@{2}\s\-[0-9]+\,*[0-9]*\s\+[0-9]+\,*[0-9]*' | grep -o -E '\+[0-9]+\,*[0-9]*'"
      added_lines=$(git log -1 -p -U0 -- ""${file}"" | grep -o -E '^\@{2}\s\-[0-9]+\,*[0-9]*\s\+[0-9]+\,*[0-9]*' | grep -o -E '\+[0-9]+\,*[0-9]*')
      
      # Replace "@@ -" with nothing
      lines=${lines//@@ -/}
      added_lines=${added_lines//\+/}

      # Convert $lines to array
      lines=($lines)
      added_lines=($added_lines)

      each_line=($file)
      for line in "${lines[@]}";
      do
        value=${line#*:}
        value=${value//,/ }
        value=($value)

        loop=${value[1]}
        if [ "$loop" != 0 ];
        then
          each_line+=(${value[0]})
        fi

        if [ $loop ];
        then
          while [ $loop -ge 2 ];
          do
            value[0]=$((${value[0]}+1))
            each_line+=(${value[0]})
            loop=$(($loop-1))
          done
        fi
      done

      each_added_line=($file)
      for line in "${added_lines[@]}";
      do
        value=${line#*:}
        value=${value//,/ }
        value=($value)

        loop=${value[1]}
        if [ "$loop" != 0 ];
        then
          each_added_line+=(${value[0]})
        fi

        if [ $loop ];
        then
          while [ $loop -ge 2 ];
          do
            value[0]=$((${value[0]}+1))
            each_added_line+=(${value[0]})
            loop=$(($loop-1))
          done
        fi
      done
      
      echo ${each_line[@]} >> "../deps/lines/${hash}.out"
      echo ${each_added_line[@]} >> "../deps/added-lines/${hash}.out"
    done < ../deps/modified-files/${hash}.out
  fi

  echo 'git log -n2 | grep -o -E -e "[0-9a-f]{40}$"'
  commits=($(git log -n2 | grep -o -E -e "[0-9a-f]{40}$"))

  echo "git checkout -f ${commits[1]}"
  git checkout -f ${commits[1]}

  echo "Running git blame on commit files"
  while read file;
  do
    file=($file)

    command=()
    if [ ${file[1]} ];
    then
      command=("git blame -e "${file[0]}"")

      command+=(" | grep ")
      i=1
      len=$((${#file[@]}))
      while [ "$len" -ge "$i" ];
      do
        command+=(" -e \" ${file[$i]})\"")
        i=$(($i+1))
      done

      command+=(" | grep -o -E -e \"[a-zA-Z0-9._-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-]+\" -e \"initial.commit\"")
    fi
    echo ${command[@]}
    eval ${command[@]} >> "../deps/authors/${hash}.out"

  done < ../deps/lines/${hash}.out
done < ../hashes.txt

echo 'deps scripts ended'