import os

target_dates = ["2023-08-14", "2023-08-15", "2023-08-17", "2023-08-18", "2023-08-01"]

for target_date in target_dates:
    # Create a commit for the target date
    d = target_date + " 00:00:00"
    with open('file.txt', 'a') as file:
        file.write(d + '\n')
    os.system('git add .')
    os.system(f'git commit --date="{d}" -m "commit on {target_date}"')

# Push the commits to the repository
os.system('git push -u origin main')
