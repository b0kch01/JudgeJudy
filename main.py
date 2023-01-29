import os
import subprocess
import pyperclip
import profanity_check
from termcolor import colored, cprint
import json
from alive_progress import alive_bar


TITLE = """
 ▄▄▄· ▄• ▄▌▄▄▄▄▄       ▐▄▄▄▄• ▄▌·▄▄▄▄   ▄▄ • ▄▄▄ .
▐█ ▀█ █▪██▌•██  ▪       ·███▪██▌██▪ ██ ▐█ ▀ ▪▀▄.▀·
▄█▀▀█ █▌▐█▌ ▐█.▪ ▄█▀▄ ▪▄ ███▌▐█▌▐█· ▐█▌▄█ ▀█▄▐▀▀▪▄
▐█ ▪▐▌▐█▄█▌ ▐█▌·▐█▌.▐▌▐▌▐█▌▐█▄█▌██. ██ ▐█▄▪▐█▐█▄▄▌
 ▀  ▀  ▀▀▀  ▀▀▀  ▀█▄▀▪ ▀▀▀• ▀▀▀ ▀▀▀▀▀• ·▀▀▀▀  ▀▀▀ 
"""


# Only accepts GitHub Repo urls so far...
def verify_url(url: str):
    rules = [
        # Add rules here
        url.startswith("https://github.com/"),
        " " not in url,
        "\t" not in url,
        "\n" not in url,
        "\r" not in url
    ]

    return all(rules)


# Creates empty temp folder
def create_temp_dir():
    if os.path.exists("temp/"):
        subprocess.run(["rm", "-rf", "temp/"])
    os.mkdir("temp")


# Prints the title
def title():
    subprocess.run(["clear"])
    cprint(TITLE)

    print(
        f"Made with {colored('*magic*', attrs=['bold'])} by Nathan the intern.\n")


# UNUSED, but asks for single url
def ask_url():
    if verify_url(github_url := pyperclip.paste()):
        print(colored("Found GitHub Repo from pasteboard:",
              "yellow", attrs=["bold"]), github_url)
    else:
        github_url = input(colored("Enter repo url: ", "blue", attrs=["bold"]))

    return github_url


# Clones a git repository to temp
def clone_repo(url):
    if not verify_url(url):
        cprint("Link is not valid!", "red")
        return

    create_temp_dir()
    subprocess.run([f"git clone {url} temp/"], capture_output=True, shell=True)


# Get the number of commits in temp
def get_commit_n():
    try:
        count = int(subprocess.run(
            ["cd temp; git rev-list --all --count"],
            capture_output=True,
            shell=True).stdout)
    except ValueError:
        count = 0

    return count


def get_file_stats(file):
    suspicious = []
    line_number = 0

    try:
        for line in file:
            line_number += 1
            if (p := profanity_check.predict_prob([line])[0]) > 0.7:
                suspicious.append(
                    f"{line_number} - {p} - {line.strip()}")
    except (UnicodeDecodeError, OSError):
        pass

    return (suspicious, line_number)


# Walks through temp folder and returns statistics
# If nothing is suspicious, dictionary is empty
def walk_temp():
    profanity_log = dict()
    total_lines = 0

    for dir in os.walk("temp"):
        if any(bad in dir[0] for bad in
               [".git", "package.json",
                "package-lock.json", "yarn.lock"
                ".png", ".jpg", ".svg",
                "node_modules"]
               ):
            continue

        # Check for suspicious lines
        for file in dir[2]:
            with open(dir[0] + '/' + file) as live_file:
                suspicious, line_number = get_file_stats(live_file)
                total_lines += line_number
                if len(suspicious) > 0:
                    profanity_log[dir[0] + '/' + file] = suspicious

    commit_n = get_commit_n()
    if commit_n < 10 or len(profanity_log) > 0:
        profanity_log['commit_number'] = commit_n
        profanity_log['lines_checked'] = total_lines

    return profanity_log


def create_csv(urls):
    results = dict()

    cprint("✔ Cloning repositories...", "green")

    with alive_bar(len(urls), spinner="waves2", ctrl_c=False) as progress:
        for url in urls:
            repo_name = url.split('/')[4][:-5]
            repo_name_padded = "• " + (repo_name + " "*12)[:12]
            progress.title(colored(repo_name_padded, "yellow"))
            clone_repo(url.strip())

            if len(faults := walk_temp()) > 0:
                results.update({url: faults})

            progress()

    print()
    print(f"{len(results)} projects with profanity.")
    export = json.dumps(results, indent=2)
    with open("output.json", "w") as live_file:
        live_file.write(export)
        cprint("Wrote to output.json", "blue")


if __name__ == "__main__":
    title()
    cprint("✔ Opening input file...", "green")
    with open("input.txt", "r") as urls:
        create_csv(urls.readlines())
