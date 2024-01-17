
```
🚩 Flags GitHub projects with low commit numbers and unprofessional code.
```


<img src=https://user-images.githubusercontent.com/44041512/215307227-54858b69-7e9a-4cb0-becc-26877a74f8fc.gif height=300>


# Compatibility
⚠️ Tested and built for `macOS Ventura`

# Additional Features
1. Colorful Interface.
2. Shows probability of offensiveness.
3. Neat progress bar.
4. Ignores any paths containing: `.git`, `package.json`, `package-lock.json`, `yarn.lock`, `.png`, `.jpg`, `.svg`, `node_modules`

# Usage
> If you have previously installed `profanity-filter`, please uninstall it before running this script.

Install pip requirements:
```console
pip install -r requirements.txt
```

Edit `input.txt` to have your list of repos:
```
https://github.com/rominf/profanity-filter.git
https://github.com/b0kch01/portfolio.git
https://github.com/b0kch01/NitroType-Bot.git
https://github.com/b0kch01/Essay-Checker.git
```

Run `main.py`
```console
python main.py
```
You will get a `output.json` of this schema:
> `.csv` did not have enough dimensions to represent all the information I wished to show.  
> With a descent JSON viewer, you can see the entire output pretty well.
```json
{
  "https://github.com/rominf/profanity-filter.git\n": {
    "temp/README.md": [
      "67 - 0.9995242724249979 - pf.censor(\"That's bullshit!\")",
      "152 - 0.9999803891853934 - pf.is_profane(\"That's bullshit!\")",
      "156 - 0.9995379247905744 - pf.censor(\"Fuck orange chocolates\")"
    ],
    "temp/tests/test_profanity_filter.py": [
      "60 - 0.9053110522059576 - assert shiiit_word == Word(uncensored='shiiit', censored='******', original_profane_word='shit')"
    ],
    "commit_number": 94,
    "lines_checked": 8095
  },
  "https://github.com/b0kch01/Essay-Checker.git": {
    "temp/index.js": [
      "216 - 0.8954458564053954 - chew the fat",
      "959 - 0.8437034442612683 - ugly"
    ],
    "commit_number": 22,
    "lines_checked": 1394
  }
}
```

# Licensing
You may do whatever you want with the code. However, I ask you to respect the licensing for the libraries used in this project. 
