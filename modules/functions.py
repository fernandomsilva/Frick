#!/usr/bin/env python
# -*- coding: utf-8 -*-
def readGroup(data, element):
	index1 = data.index(element)
	#index2 = data[index1+1:].index(element) + index1 + 1
		
	group = [element[1:]]
	i = index1 + 1
	#for i in range(index1+1, index2):
	while (data[i] != element):
		if (data[i][0] != "\\"):
			group.append(data[i])
		else:
			group.append(readGroup(data, data[i]))
			i = i - 1
		i = i + 1
		
	index1 = data.index(element)
	index2 = data[index1+1:].index(element) + index1 + 1
	
	for i in reversed(range(index1, index2+1)):
		del data[i]
	
	return group