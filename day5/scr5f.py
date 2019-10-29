#!/usr/bin/env python
import platform
import sys
import os
import site
import json
import yaml

# 1. version
ver = platform.python_version()
print(ver)
# 2. virtual environment (name)
mycmd = 'pyenv version'
namevenv = str(os.popen(mycmd).read()).split()
# 3. python executable location
py_location = "({0}/{1})".format(namevenv[3][:-1], namevenv[0])
# 4. pip location (each python version has its own version of pip)
pipcmd = 'pip --version'
pip_location = str(os.popen(pipcmd).read()).split()
# 5. PYTHONPATH
# 6. installed packages: name, version
packages_cmd = "pip freeze"
packages = str(os.popen(packages_cmd).read()).split('\n')
pack_dict = {}
for i in packages:
    if i:
        a = i.split('==')
        print(a[0], a[1])
        pack_dict.update({a[0]: a[1]})
# 7. site-packages location

# Script should output result to *.json and *.yaml files.
# make final dict
f_dict = {}
f_dict["python_version"] = ver
f_dict["name_virt_env"] = namevenv[0]
f_dict["python_location"] = py_location
f_dict["pip_location"] = pip_location[3]
f_dict["pythonpath"] = sys.path
f_dict["installed_packs"] = pack_dict
f_dict["site_packages_location"] = site.getsitepackages()

# create json file
with open('result.json', 'w') as fp:
    json.dump(f_dict, fp, indent=4)

# create yaml file
with open('result.yml', 'w') as outfile:
    yaml.dump(f_dict, outfile, default_flow_style=False)

