# Password Strength Checker

**Author:** Kujalarajan V  
**Project:** IBM SkillsBuild Cyber Security 2026 – BharatCares

## Project description
Password Strength Checker is a small Python cybersecurity-awareness project. It estimates how difficult a password may be to guess and gives practical suggestions. It uses the offline `zxcvbn` password-strength estimator, which looks for common patterns such as dictionary words, sequences, repeated characters, dates, and predictable substitutions.

The program reads the password with Python's `getpass` module so it is not echoed on the terminal. It does not write passwords to a file, database, or network service.

## Technologies used
- Python 3.9 or later
- `zxcvbn` Python package
- Python standard library: `getpass`

## Dataset / reference links
This project does not require a separately downloaded dataset. The `zxcvbn` package includes the pattern dictionaries used by its estimator.

Useful reference material:
- zxcvbn project and methodology: https://github.com/dropbox/zxcvbn
- OWASP Authentication Cheat Sheet: https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html
- NIST Digital Identity Guidelines (SP 800-63B): https://pages.nist.gov/800-63-4/sp800-63b.html

## Project files
- `KujalarajanV_PasswordStrengthChecker.ipynb` — notebook version with explanation, code, and test cases.
- `KujalarajanV_PasswordStrengthChecker.py` — runnable Python script.
- `requirements.txt` — Python dependency list.
- `KujalarajanV_ProjectReport.docx` — project documentation.

## Setup instructions
1. Install Python 3.9 or later.
2. Open a terminal in the project folder.
3. (Recommended) Create and activate a virtual environment:
   - Windows: `python -m venv .venv` then `.venv\\Scripts\\activate`
   - macOS/Linux: `python3 -m venv .venv` then `source .venv/bin/activate`
4. Install dependencies:
   ```bash
   python -m pip install -r requirements.txt
   ```

## Run the project
Run the script:
```bash
python KujalarajanV_PasswordStrengthChecker.py
```

Or open `KujalarajanV_PasswordStrengthChecker.ipynb` in Jupyter Notebook / JupyterLab, install the requirements, and run the cells from top to bottom. The interactive notebook cell uses hidden password input when supported.

## How it works
1. The user enters a password.
2. `zxcvbn` analyses likely guessing patterns.
3. The project displays a score from 0 to 4, a strength label, an illustrative guessing-time estimate, and suggestions.
4. The program does not intentionally save or transmit the entered password.

## Example interpretation
- 0 — Very Weak
- 1 — Weak
- 2 — Fair
- 3 — Strong
- 4 — Very Strong

The estimated attack time is an educational estimate based on a particular offline-hashing scenario. It is not a guarantee.

## Limitations and responsible use
- This is an educational estimator, not a complete security audit.
- Results depend on the attack assumptions and estimator version.
- A strong score does not make password reuse safe.
- Do not enter a real password that protects an important account into a demo or shared computer. Use a made-up test password for demonstrations.
- Prefer a unique password for every account and use a reputable password manager and multi-factor authentication where available.
