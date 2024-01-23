import re
import sys
from pathlib import Path

from questionary import confirm
from questionary import path


def receive_path() -> Path:
    msg = 'Please enter the path of dir.'
    received_path = Path(path(msg).ask())

    if not received_path.exists():
        msg = 'Passed an unexistent path, do you want to give another path?'
        resp = confirm(msg).ask()
        if resp is False:
            sys.exit()
        return receive_path()

    if not received_path.is_dir():
        msg = 'The path you entered is not a directory, can you try again?'
        resp = confirm(msg).ask()
        if resp is False:
            sys.exit()
        return receive_path()

    return received_path


def main():
    path = receive_path()
    for root, _, files in path.walk():
        for file in files:
            original = root / file
            stripped = root / re.sub(r'[?].*', '', file)
            if original == stripped:
                continue
            print()
            print(f'original: {str(original)}')
            print(f'replaced: {str(stripped)}')
            original.rename(stripped)


if __name__ == '__main__':
    main()
