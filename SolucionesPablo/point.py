from __future__ import division;
from sys import argv;

script, filename = argv;

txt = open(filename);
rawData = txt.read();

data = rawData.lstrip(">");
data = data.split(">");

data[:] = [i.split("\n", 1) for i in data];

distance = 0;

data = data[0];

print data;

data[0] = list(data[0]);
data[1] = list(data[1]);

for i in range(0, len(data[0])):
	if data[0][i] != data[1][i]:
		distance +=1;

print distance;