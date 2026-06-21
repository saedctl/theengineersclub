# Password Auditor

A password strength analyser with pattern detection, entropy scoring, and breach checking via the HIBP API.

## What it is

Password Auditor evaluates password strength through multiple lenses: Shannon entropy calculation, common pattern detection (keyboard walks, dates, repeated characters), wordlist comparison, and Have I Been Pwned (HIBP) k-anonymity API checks to see if a password has appeared in known breaches. It supports single password checks and batch auditing from a file.

Password policy enforcement and credential auditing are core GRC and security engineering tasks. Understanding why "P@ssw0rd!" is weak despite meeting most complexity rules — and being able to programmatically evaluate password strength — is practical knowledge that applies to policy writing, application security reviews, and compliance audits.

## What you'll build

- Shannon entropy calculator for password strength scoring
- Pattern detector (keyboard walks, dates, l33t substitutions, repeated chars)
- Wordlist checker against common password lists
- HIBP k-anonymity API integration (checks breach status without sending the password)
- Single password check with detailed strength report
- Batch mode for auditing password files

## Skills developed

- Information theory (Shannon entropy)
- Pattern recognition with regex
- Privacy-preserving API design (k-anonymity)
- Secure password handling practices
- Batch processing and reporting

## How to run

```bash
cd entry/05-passaudit
make install
python src/main.py check "MyP@ssw0rd123" --wordlist --hibp
python src/main.py batch --file passwords.txt
```

## Stretch goals

- Add zxcvbn-style scoring with penalty for common substitutions
- Generate password strength reports in HTML
- Check against multiple wordlists (rockyou, common-passwords, etc.)
- Add a `generate` command that creates strong passwords meeting given criteria
- Estimate crack time based on different attack scenarios (online, offline, GPU)
