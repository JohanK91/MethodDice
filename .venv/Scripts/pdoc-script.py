#!C:\Users\vigge\onedrive\dokument\github\methoddice\.venv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'pdoc3==0.9.2','console_scripts','pdoc'
__requires__ = 'pdoc3==0.9.2'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('pdoc3==0.9.2', 'console_scripts', 'pdoc')()
    )
