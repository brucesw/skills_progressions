from dictionaries import *
from helpers import *

# this does main portion of the work
# just a modified search algorithm
def expand_prerequisites(skill, prereq_list, depth, ret):
	if skill not in prereq_list:
		return
	for s in prereq_list[skill]:
		#print s, depth
		if depth not in ret:
			ret[depth] = []
		if s not in ret[depth]:
			ret[depth].append(s)
		expand_prerequisites(s, prereq_list, depth + 1, ret)

# this is the main function call to get the prerequisites
# for a skill.  argument must be an abbreviation
def get_prereqs(skill):
	if skill not in prerequisites_dict:
		return False, {}

	d = {}

	expand_prerequisites(skill, prerequisites_dict, 0, d)

	ret = remove_duplicates(d)

	return True, ret

# this just displays the output from get_prereqs()
# in a way that is easy to read
def print_prerequisites(skill):
	success, prereqs = get_prereqs(skill)
	if not success:
		print 'Skill {0} not added yet or spelled wrong.'.format(skills_dict[skill])
		return
	
	print 'prerequisites for {0} ({1}):\n'.format(skills_dict[skill], skill)

	for i in sorted(prereqs.keys(), reverse = True):
		for s in prereqs[i]:
			print '{0}  ({1})'.format(skills_dict[s], s)
		print ''

	print '===>{0}  ({1})'.format(skills_dict[skill], skill)
