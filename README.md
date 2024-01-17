```
🚩 Flags GitHub projects with low commit numbers and unprofessional code.
```

<div align=center>
<img width="600" alt="Screenshot of JudgeJudy at work!" src="https://github.com/b0kch01/JudgeJudy/assets/44041512/48dc3af5-565b-4e0c-a8e7-c524f63ac81e">
</div>



# Compatibility
⚠️ Tested and built for `macOS Sonoma`

# Additional Features
- [x] Colorful Interface.
- [x] Shows probability of offensiveness.
- [x] Neat progress bar.
- [x] Ignores irrelevant files/directories such as: `.git`, `yarn.lock`, `.png`, `.svg`, `node_modules`
- [x] Basic statistics on commit history

# Usage
1. Install pip requirements:
   > ⚠️ It is HIGHLY recommended that you make a fresh environment before continuing, especially if you have previously used this program before.
    ```console
    pip install -r requirements.txt
    ```

3. Edit `input.txt` to have your list of repos:
    ```
    https://github.com/rominf/profanity-filter.git
    https://github.com/b0kch01/portfolio.git
    https://github.com/b0kch01/NitroType-Bot.git
    https://github.com/b0kch01/Essay-Checker.git
    ```

4. Run `main.py`
    ```console
    python main.py
    ```
## Expected Output
You will get a `output.json` of this schema:
> With a descent JSON viewer, you can see the entire output pretty well.
```json
{
  "https://github.com/b0kch01/JudgeJudy.git": {
    "flagged_files": {
      "temp/README.md": [
        "44 - 0.9978561926422669 - \"67 - 0.9995242724249979 - pf.censor(\\\"That's bullshit!\\\")\",",
        "45 - 0.9978032306917134 - \"152 - 0.9999803891853934 - pf.is_profane(\\\"That's bullshit!\\\")\",",
        "46 - 0.9980430642000068 - \"156 - 0.9995379247905744 - pf.censor(\\\"Fuck orange chocolates\\\")\"",
        "49 - 0.7175500954181105 - \"60 - 0.9053110522059576 - assert shiiit_word == Word(uncensored='shiiit', censored='******', original_profane_word='shit')\"",
        "56 - 0.7213216593841532 - \"216 - 0.8954458564053954 - chew the fat\",",
        "57 - 0.8444989517065041 - \"959 - 0.8437034442612683 - ugly\""
      ],
      "commit_number": 10,
      "lines_checked": 278
    },
    "first_commit": "2023-01-28 09:07:57 PM",
    "last_commit": "2024-01-16 01:22:56 PM",
    "most_additions": "3 files changed, 168 insertions(+)"
  },
  "https://github.com/b0kch01/aselfasliefj.git": {
    "error": "Cloning into 'temp'...\nremote: Repository not found.\nfatal: repository 'https://github.com/b0kch01/aselfasliefj.git/' not found\n"
  },
  "https://github.com/b0kch01/valorant-cheat.git": {
    "first_commit": "2021-03-20 08:00:16 PM",
    "last_commit": "2021-12-05 01:25:42 PM",
    "most_additions": "3 files changed, 152 insertions(+)"
  }
}
```

# Licensing
You may do whatever you want with the code. However, I ask you to respect the licensing for the libraries used in this project. 
