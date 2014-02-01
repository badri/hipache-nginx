import sys

template = sys.argv[1]
vars = dict([(arg.split('=', 1))  for arg in sys.argv[2:]])
with open(template) as f:
    text = f.read()
    text = text % vars
    sys.stdout.write(text)