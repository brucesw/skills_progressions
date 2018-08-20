def remove_duplicates(d):
	ret = {}
	for i in d.keys():
		for skill in d[i]:
			if skill not in ret:
				ret[skill] = i
			if i > ret[skill]:
				ret[skill] = i
	#print ret
	return invert(ret)

def invert(d):
	ret = {}
	for skill in d.keys():
		if d[skill] not in ret:
			ret[d[skill]] = []
		ret[d[skill]].append(skill)
	return ret