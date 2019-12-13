#!/usr/bin/env python
# -*- coding: utf-8 -*-

import subprocess
import shlex, sys, re

def run_cmd(cmd):
  # args = shlex.split(cmd)
  proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
  out, _ = proc.communicate()
  exitcode = proc.returncode

  trim_out = out.decode().strip()
  return exitcode, trim_out

def parse_value(value):
  try:
    return int(value)
  except ValueError:
    return value

def to_format(variables, sep):
  formats = []
  for var in variables:
    assert re.match(r'^[a-z_]+$', var)
    formats.append('#{' + var + '}')
  return sep.join(formats)

def parse_variables(out, variable_names, sep):
  res = out.split(sep)
  assert len(res) == len(variable_names)
  assert any(0 < len(v) for v in res)
  values = list(map(parse_value, res))

  m = {}
  for i in range(len(variable_names)):
    name = variable_names[i]
    value = values[i]
    m[name] = value
  return m

def display(variables, sep='|'): 
  form = to_format(variables, sep)

  code, out = run_cmd(['tmux', 'display', '-p', form])
  return parse_variables(out, variables, sep).values()

def tmux_cmd(cmd, sep='|'):
  variables = None
  form = ''
  for i in range(len(cmd) - 1):
    if cmd[i] != '-F':
      continue
    if isinstance(cmd[i + 1], list):
      variables = cmd[i + 1]
      form = to_format(variables, sep)
      cmd[i + 1] = form

  code, out = run_cmd(['tmux'] + cmd)
  if variables is None:
    return out

  lines = out.split()
  return list(map(lambda line: parse_variables(line, variables, sep), lines))
