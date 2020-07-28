#!/usr/bin/env python3

"""Check credit-card-number validity."""

import re


def is_valid(cred: str) -> str:
    """Return whether a credit card is valid."""
    start = re.search(r"^[4|5|6]", cred)
    chars = re.fullmatch(r"[0-9]{16}", cred)
    hyphens = re.fullmatch(r"[0-9]{4}-[0-9]{4}-[0-9]{4}-[0-9]{4}", cred)
    rep = re.search(r"(.)\1{3,}", cred.replace("-", ""))

    if rep:
        print(f"\nrep: {rep.group()}")

    if start and (chars or hyphens) and not rep:
        print("Valid")
    else:
        print("Invalid")


if __name__ == "__main__":
    creds = [
        "4123456789123456",
        "5123-4567-8912-3456",
        "61234-567-8912-3456",
        "4123356789123456",
        "5133-3367-8912-3456",
        "5123 - 3567 - 8912 - 3456",
        "3695-7963-  5827-75",
        "4143-4672-8798-2968-2968",
        "6865---------------3965---------------1564-------------2918",
        "6865396515642918"
    ]

    for cred in creds:
        is_valid(cred)
