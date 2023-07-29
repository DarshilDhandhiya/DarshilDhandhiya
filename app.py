import os

target_dates = ["2023-07-30", "2023-07-31", "2023-07-23", "2023-07-07"]

for target_date in target_dates:
    # Create a commit for the target date
    d = target_date + " 00:00:00"
    with open('file.txt', 'a') as file:
        file.write(d + '\n')
    os.system('git add .')
    os.system(f'git commit --date="{d}" -m "commit on {target_date}"')

# Push the commits to the repository
os.system('git push -u origin main')
