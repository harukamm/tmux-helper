#!/usr/bin/env python
# -*- coding: utf-8 -*-

import util

def layout():
  # The following command does not work well
  # select-layout tiled => Always splits a window vertically first, so does
  #    not save the direction.
  count, w, h = util.display(['window_panes', 'client_width', 'client_height'])
  env = util.harukam_env()

  m = {
    "HOME_DESKTOP": {
      4: "0c9d,272x64,0,0{136x64,0,0[136x32,0,0,14,136x31,0,33,17],135x64,137,0[135x32,137,0,15,135x31,137,33,16]}",
      6: "b6cc,272x64,0,0{90x64,0,0[90x32,0,0,6,90x31,0,33,4],90x64,91,0[90x32,91,0,7,90x31,91,33,2],90x64,182,0[90x32,182,0,5,90x31,182,33,3]}"
    },
    "HOME_ASUS": {
    },
    "HOME_MAC": {
    },
    "OFFICE": {
    }
  }

  assert env
  assert env in m
  assert count in m[env]

  layout = m[env][count]
  util.run_cmd(['tmux', 'select-layout', layout])

def run(cmd):
  assert 0 < len(cmd)
  first = cmd[0]

  if first == "layout":
    layout()
  else:
    raise Exception("not found command: " + first)
