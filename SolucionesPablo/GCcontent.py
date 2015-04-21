from __future__ import division;
from sys import argv;

script, filename = argv;

txt = open(filename);
rawData = txt.read();

data = rawData.lstrip(">");
data = data.split(">");

data[:] = [i.split("\n", 1) for i in data];
print data;
strNames = [];
for i in data:
	strNames.append(i[0]);

data[:] = [i[1].split("\n") for i in data];
data[:] = ["".join(i) for i in data];

max = [0, 0];
for i in range(0, len(data)):
	GC = 0;
	for j in data[i]:
		if j == "G" or j == "C":
			GC += 1;
			
	GCpercent = 100*GC/len(data[i]);
	#strNames[i].append(GCpercent);
	if GCpercent > max[0]:
		max = [GCpercent, strNames[i]];
	
	if i == len(data)-1:
		print max[1];
		print max[0];