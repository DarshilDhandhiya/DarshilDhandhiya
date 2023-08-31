import os
from datetime import datetime, timedelta

total_commits_to_add = 11

# Get the current date
current_date = datetime.now()

for i in range(total_commits_to_add):
    # Create a commit date
    commit_date = current_date - timedelta(days=i)
    d = commit_date.strftime("%Y-%m-%d %H:%M:%S")
    
    # Write commit date to file and make a commit
    with open('file.txt', 'a') as file:
        file.write(d + '\n')
    os.system('git add .')
    os.system(f'git commit --date="{d}" -m "commit on {d}"')

# Push the commits to the repository
os.system('git push -u origin main')
