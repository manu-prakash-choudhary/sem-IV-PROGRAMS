with open ('run.sh', 'w') as rsh:
    rsh.write('''\
#! /bin/bash
echo "I ran this"
echo "more lines"
python3 tp2.py $1
''')