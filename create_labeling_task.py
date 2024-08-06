import sys
from github import Github
from git import Repo
import os

def main(video_name, batch_number):
    # Set up the GitHub API
    token = os.getenv('GH_TOKEN')
    g = Github(token)
    repo = g.get_repo("UCSD-E4E/baboon-hand-labeling")

    # Create the issue
    issue_title = f"Labeling Task: {video_name} Batch {batch_number}"
    issue_body = f"Please label the images in {video_name}/batch_{batch_number}/frames"
    label_name = "labeling"

    # Create or update the label
    try:
        label = repo.get_label(label_name)
        print(f"Label '{label_name}' already exists.")
    except:
        label = repo.create_label(name=label_name, color="0E8A16", description="Tasks for labeling images")
        print(f"Created label '{label_name}'.")

    # Create the issue
    issue = repo.create_issue(title=issue_title, body=issue_body, labels=[label])
    print(f"Created issue #{issue.number}")

    # Clone the repo locally (or use an existing clone)
    local_repo_path = "/home/runner/work/baboon-hand-labeling/baboon-hand-labeling"
    if not os.path.exists(local_repo_path):
        Repo.clone_from(repo.clone_url, local_repo_path)

    local_repo = Repo(local_repo_path)
    branch_name = f"labeling-task-{video_name.replace(' ', '-')}-batch-{batch_number}"

    # Create a new branch
    main_branch = local_repo.heads.main
    new_branch = local_repo.create_head(branch_name, main_branch.commit)
    new_branch.checkout()

    # Create a new file for the task
    file_path = os.path.join(local_repo_path, "labeling_task.md")
    with open(file_path, "w") as f:
        f.write(f"Labeling task for {video_name} Batch {batch_number}\n")

    # Stage and commit the new file
    local_repo.index.add([file_path])
    local_repo.index.commit(f"Initialize labeling task for {video_name} Batch {batch_number}")

    # Push the new branch to GitHub
    local_repo.remote(name='origin').push(refspec=f"{branch_name}:{branch_name}")

    # Create a pull request
    pr = repo.create_pull(title=f"Labeling Task: {video_name} Batch {batch_number}",
                          body=f"This PR is for the labeling task: {video_name} Batch {batch_number}.",
                          base="main", head=branch_name)
    print(f"Created pull request: {pr.html_url}")

    # Comment on the issue with the PR link
    issue.create_comment(f"A new branch and pull request have been created for this labeling task. You can find the pull request here: {pr.html_url}")

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: create_labeling_task.py <video_name> <batch_number>")
        sys.exit(1)

    video_name = sys.argv[1]
    batch_number = sys.argv[2]
    main(video_name, batch_number)
