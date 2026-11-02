"""
Password Strength Checker
Author: Kujalarajan V
Purpose: Estimate password strength locally without saving or transmitting the password.

Install dependencies:
    pip install -r requirements.txt
Run:
    python KujalarajanV_PasswordStrengthChecker.py
"""

import getpass
import re
from zxcvbn import zxcvbn


def assess_password(password: str) -> dict:
    """Return a strength assessment using zxcvbn's offline estimator."""
    if not isinstance(password, str):
        raise TypeError("Password must be text.")

    if not password:
        return {
            "score": 0,
            "label": "Very Weak",
            "guesses": 1,
            "feedback": ["Enter a password to receive an assessment."],
            "crack_time": "instant",
        }

    result = zxcvbn(password)
    score = result["score"]  # 0 (weak) to 4 (very strong)
    labels = ["Very Weak", "Weak", "Fair", "Strong", "Very Strong"]

    feedback = []
    warning = result.get("feedback", {}).get("warning", "")
    suggestions = result.get("feedback", {}).get("suggestions", [])
    if warning:
        feedback.append(warning)
    feedback.extend(suggestions)

    # Additional general guidance, without revealing or storing the password.
    if len(password) < 12:
        feedback.append("Consider using a longer passphrase (12–16+ characters).")
    if password.lower() == password or password.upper() == password:
        feedback.append("A mix of character types can help, but length and uniqueness matter most.")
    if not feedback:
        feedback.append("Good result. Keep this password unique to one account.")

    return {
        "score": score,
        "label": labels[score],
        "guesses": result.get("guesses", 0),
        "feedback": feedback,
        "crack_time": result.get("crack_times_display", {}).get(
            "offline_slow_hashing_1e4_per_second", "not available"
        ),
    }


def display_result(result: dict) -> None:
    """Print a readable assessment."""
    print("\n--- Password Strength Report ---")
    print(f"Strength: {result['label']} ({result['score']}/4)")
    print(f"Estimated guesses: {result['guesses']:,}")
    print(f"Illustrative offline attack estimate: {result['crack_time']}")
    print("\nSuggestions:")
    for item in result["feedback"]:
        print(f"- {item}")
    print("\nPrivacy note: this program assesses the password locally and does not save it.")


def main() -> None:
    print("PASSWORD STRENGTH CHECKER")
    print("Your input is hidden while typing.")
    password = getpass.getpass("Enter a password to assess: ")
    result = assess_password(password)
    display_result(result)
    # Remove the local variable reference as soon as practical.
    del password


if __name__ == "__main__":
    main()
