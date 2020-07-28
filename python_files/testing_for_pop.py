#!/usr/bin/env python3

"""Read this docstring."""

import platform


def double(n):
    """Double the input, n."""
    return n * 2


ver = platform.python_version()

print(f"Running via the Python {ver} interpreter.\n")

if ver[0:3] == '3.7':
    print(f"double(15) = {double(15)}")
# Below is fine in 3.8.x but produces an error in 3.7.X, hence the odd
# error in the shebang. (3.7.X is the system-default Python version.)
elif ver[0:3] == '3.8':
    print(f"{double(15) = }")
else:
    print("Somehow we're running Python {ver}...")
