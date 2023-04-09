require_relative 'commit_verifier'
require_relative '../files/file_aux'

path = 'input/*.input'

all_commits = []
for filename in Dir.glob(path)
  puts filename

  commit_verifier = CommitVerifier.new(filename)

  commits_by_author = commit_verifier.inform_commits_by_author
  write_list_to_csv(commits_by_author, true, ';', filename.split('/')[1].split('.')[0], 'commits_by_author')
  puts "END of #{filename}"
end