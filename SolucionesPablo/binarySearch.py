arr1 = [10,20,30,40,50];
arr2 = [40,10,35,15,40,20];

result = [];

for i in arr2:
	for j in arr1:
		if i==j:
			result.append(arr2.index(j));
		else:
			result.append(-1);

print result;