#!/usr/bin/env python
# -*- coding: utf-8 -*-

import util, interpreter
import sys

def main():
  cmd = sys.argv[1:]
  interpreter.run(cmd)
    
if __name__== "__main__":
  main()
