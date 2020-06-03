"""
Script to pull changed files in a Pull Request using a GET resquest to the
GitHub API.
"""
import requests
import argparse


def parse_args():
    """Construct the command line interface for the script"""
    DESCRIPTION = "Script to check for occurences of 'Lorem Ipsum' in Markdown files"
    parser = argparse.ArgumentParser(description=DESCRIPTION)

    parser.add_argument(
        "--pull-request",
        type=str,
        default=None,
        help="If the script is be run on files changed by a pull request, parse the PR number",
    )

    return parser.parse_args()


def get_files_from_pr(pr_num):
    """Return a list of changed files from a GitHub Pull Request

    Arguments:
        pr_num {str} -- Pull Request number to get modified files from

    Returns:
        {list} -- List of modified filenames
    """
    files = []
    pr_url = f"https://api.github.com/repos/alan-turing-institute/the-turing-way/pulls/{pr_num}/files"
    resp = requests.get(pr_url)

    for item in resp.json():
        files.append(item["filename"])

    return files


if __name__ == "__main__":
    args = parse_args()
    changed_files = get_files_from_pr(args.pull_request)
    print(changed_files)
