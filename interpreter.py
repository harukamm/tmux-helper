#!/usr/bin/env python
# -*- coding: utf-8 -*-

import util, sys

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
      4: "90ea,272x62,0,0{136x62,0,0[136x31,0,0,13,136x30,0,32,16],135x62,137,0[135x31,137,0,14,135x30,137,32,15]}",
      6: "188a,272x62,0,0{90x62,0,0[90x31,0,0,7,90x30,0,32,10],90x62,91,0[90x31,91,0,8,90x30,91,32,11],90x62,182,0[90x31,182,0,9,90x30,182,32,12]}"
    },
    "HOME_MAC": {
      4: "49f3,238x54,0,0{119x54,0,0[119x27,0,0,13,119x26,0,28,16],118x54,120,0[118x27,120,0,14,118x26,120,28,15]}",
      6: "9de9,238x54,0,0{78x54,0,0[78x27,0,0,7,78x26,0,28,10],78x54,79,0[78x27,79,0,8,78x26,79,28,11],80x54,158,0[80x27,158,0,9,80x26,158,28,12]}"
    },
    "OFFICE": {
      4: "93cb,245x79,0,0{122x79,0,0[122x39,0,0,13,122x39,0,40,16],122x79,123,0[122x39,123,0,14,122x39,123,40,15]}",
      6: "dddc,245x79,0,0{81x79,0,0[81x39,0,0,7,81x39,0,40,10],81x79,82,0[81x39,82,0,8,81x39,82,40,11],81x79,164,0[81x39,164,0,9,81x39,164,40,12]}"
    }
  }

  util.exit0_ifnot(env, "no env")
  util.exit0_ifnot(env in m, "unknown env: " + env)
  util.exit0_ifnot(count in m[env], "not supported count: " + str(count))

  layout = m[env][count]
  exitcode, _ = util.run_cmd(['tmux', 'select-layout', layout])

  util.exit0_ifnot(exitcode == 0, "select-layout failed")

def run(cmd):
  util.exit0_ifnot(0 < len(cmd))
  first = cmd[0]

  try:
    if first == "layout":
      layout()
    else:
      raise Exception("not found command: " + first)
  except Exception as e:
    util.exit0_ifnot(False, "exception: " + str(e))
