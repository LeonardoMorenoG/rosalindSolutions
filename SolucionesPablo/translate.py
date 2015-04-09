from __future__ import division;
from sys import argv;

script, filename = argv;

txt = open(filename);
rawData = txt.read();

data = rawData.lstrip(">");
data = data.split(">");

data[:] = [i.split("\n", 1) for i in data];
print data;

