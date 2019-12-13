#!/usr/bin/env python
# -*- coding: utf-8 -*-

import util

def layout():
  # The following command does not work well
  # 1. select-layout 67bf,272x64,0,0.. => Only works with fixed window size
  # 2. select-layout tiled => Splits a window vertically first (not horizontally)
  a = util.tmux_cmd(['list-pane', '-F', ['pane_index']])
  print(a)
  w_count, w, h = util.display(['window_panes', 'client_width', 'client_height'])
  print(w_count)

def run(cmd):
  assert 0 < len(cmd)
  first = cmd[0]

  if first == "layout":
    layout()
  else:
    raise Exception("not found command: " + first)
