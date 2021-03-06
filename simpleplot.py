#!/usr/env/python
#coding:utf-8

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
import matplotlib as mpl
import sys, os, copy, math, re

def thin(anarray):
  i = 1.0
  retarray = []
  while(i<=len(anarray)):
    retarray.append(anarray[int(i)-1])
    i*=1.2
  if int(i) != len(anarray):
    retarray.append(anarray[-1])
  return retarray

def readFile(afile):
  lines = [line.strip() for line in file(afile, "r").readlines()]
  algs = []
  data = []
  for line in lines:
    if line[0]=="#":
      if line.find("#policy") != -1:
        algs.append(line.split(" ")[2])
    else:
      sps = line.split(" ")
      data.append(sps)
  data = map(list, zip(*data)) #transpose 2d array
  data = map(thin, data) #reduce data points
  return (algs, data)

def plotRegret((algs, data)):
  plt.xlabel("t: round")
  plt.ylabel("R(t): regret")
  plt.xscale('log')
  for l in range(2, len(data), 2):
    i=l/2-1
    plt.plot(data[0], data[l], "-", label=algs[i], linewidth=2)
  plt.legend(loc="upper left")
  plt.savefig('regret.pdf')
  plt.show()

if __name__ == '__main__':
  if len(sys.argv)<2:
    print "usage: this logfile"
    sys.exit()
  afile = sys.argv[1]
  result = readFile(afile)
  plotRegret(result)


