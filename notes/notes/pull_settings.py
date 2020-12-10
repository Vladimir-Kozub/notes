import os, sys

settings_file = os.path.join(os.path.dirname(sys.argv[0]), 'settings.txt')
settings_pyfile = os.path.join(os.path.dirname(sys.argv[0]), 'settings.py')

if os.path.exists(settings_file):
    var_to_conf = dict({})
    
    with open(settings_file) as f:
        for line in f.readlines():
            var_to_conf[line.split()[0]] = line[:-1]

    with open(settings_pyfile) as f:
        in_data = f.read()
    out_data = ''
    
    for line in in_data.split('\n'):
        if len(line.split()) > 0 and  line.split()[0] in var_to_conf:
            out_data +=  var_to_conf[line.split()[0]] +'\n'
        else:
            out_data += line+'\n'
        
    with open(settings_pyfile, 'wt') as f:
        f.write(out_data)        
