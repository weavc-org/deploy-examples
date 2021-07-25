#! /usr/bin/env zxpy
# script to setup vagrant vms as docker contexts

import sys

def get_names(s: str):
  # parse names from 'vagrant status --machine-readable' commands
  names = []
  for l in s.split('\n'):
    if (l == ''): continue
    name = l.split(',')[1]
    if (len(name) > 0 and name not in names): 
      names.append(name)
  return names

if (len(sys.argv) > 1 and sys.argv[1] == 'clean'):
  # remove ssh config files and docker contexts
  ~"rm ~/.ssh/config.d/deploy-examples"
  names = get_names(~"vagrant status --machine-readable")
  for name in names:
    print(~f'docker context rm {name}')
else:
  # add ssh config files and docker contexts
  config = ~"vagrant ssh-config"
  ~"mkdir -p ~/.ssh/config.d"
  ~f"echo {config} | tee ~/.ssh/config.d/deploy-examples"
  ssh_config = ~"cat ~/.ssh/config"
  if ('include config.d/*' not in ssh_config.lower()):
    ~"echo 'Include config.d/*' | tee --append ~/.ssh/config && "

  ~'chmod u+rw,go-rwx ~/.ssh/config ~/.ssh/config.d/deploy-examples'

  names = get_names(~"vagrant status --machine-readable | grep 'state,running'")
  for name in names:
    ~f"docker context create {name} --docker='host=ssh://{name}'"