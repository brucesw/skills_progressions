# abbreviation: full length skill name
skills_dict = {
	'halfairplane': 'Half airplane',
	'arabiancrashdive': 'Arabian crash dive',
	'arabiantofeet': 'Arabian to feet',
	'barani': 'Barani',
	'frontflip': 'Front flip',
	'full': 'Full',
	'forwardroll': 'Forward roll',
	'stomachdrop': 'Stomach drop',
	'34front': 'Three quarter front',
	'1n3': 'One and three quarters front',
	'arabian1n3': 'Arabian one and three quarters',
	'arabian1n3rollout': 'Arabian one and three rollout',
	'2n3': 'Two and three quarters front',
	'arabian2n3': 'Arabian two and three quarters',
	'halfout': 'Half out',
	'baraniballout': 'Barani ballout',
	'ballout': 'Ballout',
	'doubleporpoise': 'Double porpoise',
	'babytriff': 'Baby triff (half out ballout)',
	'1n3rollout': 'One and three rollout',
	'34frontrollout': 'Three quarter front rollout',
	'halfouttostomach': 'Half out to stomach',
	'fullcruisetostomach':'Full cruise to stomach',
	'fullcruiseduck': 'Full cruise duck under',
	'fulltoback': 'Full to back',
	'baranitoback': 'Barani to back',
	'baranicruisetostomach': 'Barani cruise to stomach',
	'baranicruiseduck': 'Barani cruise duck under',
	'baranifull': 'Barani full',
	'fullfull': 'Full full',
	'baranicruiseroll': 'Barani cruise rollout',
	'fullcruiseroll': 'Full cruise rollout (miller light)',
	'fullrudi': 'Full rudi',
	'miller': 'Miller',
	'backtostomach': 'Back drop to stomach drop',
	'porpoise': 'Porpoise',
	'halfhalf': 'Half half',
	'halfrudi': 'Half rudi',
}

# abbreviation: list of prerequisite skills abbreviations
prerequisites_dict = {
	'34front': ['stomachdrop'],
	'frontflip': ['34front'],
	'barani': ['frontflip'],
	'ballout': ['porpoise'],
	'porpoise': ['backtostomach', 'frontflip'],
	'baraniballout': ['ballout', 'barani'],
	'1n3': ['ballout'],
	'halfout': ['baraniballout', '1n3'],
	'fullrudi': ['baranicruiseroll'],
	'miller': ['fullcruiseroll', 'fullrudi'],
	'fullcruiseroll': ['baranicruiseroll', 'fullfull'],
	'baranicruiseroll': ['baranifull', '1n3rollout'],
	'1n3rollout': ['1n3', '34frontrollout'],
	'baranifull': ['baranicruiseduck', 'halfout'],
	'baranicruiseduck': ['baranicruisetostomach'],
	'baranicruisetostomach': ['baranitoback'],
	'baranitoback': ['barani'],
	'fullfull': ['fullcruiseduck', 'baranifull'],
	'fullcruiseduck': ['baranicruiseduck', 'fullcruisetostomach', 'arabian1n3'],
	'arabian1n3': ['1n3', 'arabiantofeet'],
	'arabiantofeet': ['arabiancrashdive'],
	'arabiancrashdive': ['halfairplane', '34front'],
	'full': ['arabiancrashdive', 'barani'],
	'halfhalf': ['halfout', 'arabian1n3'],
	'halfrudi': ['rudiout', 'arabian1n3rollout'],
	'arabian1n3rollout': ['1n3rollout', 'arabian1n3']
}

def invert_skills_dict(d):
	ret = {}
	for abbr in d.keys():
		ret[d[abbr]] = abbr
	return ret

# full length skill name: abbreviation
inverted_skills_dict = invert_skills_dict(skills_dict)