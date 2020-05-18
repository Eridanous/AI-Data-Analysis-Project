from owlready2 import *
import types
import pandas as pd
import re
from NER_watson import text2locations as t2l
from NER_watson import get_locations,locs2locations

ds1 = pd.read_csv('complete-superhero-dataset/SuperheroDataset.csv').fillna(0)
ds2 = pd.read_csv('superhero-set/heroes_information.csv').fillna(0)
ds3 = pd.read_csv('superhero-set/super_hero_powers.csv').fillna(0)
ds4 = pd.read_csv('dc.csv').fillna(0)
ds5 = pd.read_csv('marvel.csv').fillna(0)
ds_crime = pd.read_csv('crime-rates/report.csv')


#print(ds_crime)


## Create the ontology
#onto = get_ontology("file://empty_onto.owl").load()
onto = get_ontology("file://hero.owl").load()
with onto:
	'''
	## Create the main Hero class
	class Hero(Thing):
		pass
	## (disjoint) Subclasses for evil and good heroes:
	class GoodHero(Hero):
		pass
	class EvilHero(Hero):
		pass
	#AllDisjoint([GoodHero,EvilHero])
	## Create the main Location class
	class Location(Thing):
		pass
	## Create the basic roles:
	## Everything may have a name
	class hasName(Thing>>str):
		pass
	## A hero may have a location (either birthplace or base of operations):
	class hasLocation(Hero>>Location):
		pass
	class isLocationOf(Location>>Hero):
		inverse_property = hasLocation
		pass
	## A hero has a year first appeared:
	class hasFirstAppearanceYear(Hero>>int):
		pass
	#class isFirstAppearanceYearOf(Year>>Hero):
	#	inverse_property = hasFirstAppearanceYear
	#	pass

	## A location may have a latitude and a longtitude
	class hasLatitude(Location>>float):
		pass

	class hasLongtitude(Location>>float):
		pass

	crimerate = dict()
	pn_cr = dict()
	#crimerate_names = ["has_crimerate_"+str(i) for i in range(1975,2016)]
	for i in range(1975,2016):
		crimerate[str(i)] = types.new_class("has_crimerate_"+str(i) ,(onto.Location>>float,))
		crimerate[str(i)].python_name = "has_crimerate_"+str(i)
		pn_cr[str(i)]="has_crimerate_"+str(i)

	# AXIOMS
	## Every hero has at least a name
	onto.Hero.is_a.append(onto.hasName.some(str))


	### Parse the datasets and create entities in the ontology:
	#Start with ds1
	## ALAGI
	aligndict=dict()
	for i in range(ds1.shape[0]):
		print(str(i/ds1.shape[0]))
		##Determine alignment and instantiate entity as 'a'
		if ds1["Alignment"][i]=='bad':
			a = EvilHero(ds1['Name'][i])
		elif ds1['Alignment'][i]=='good':
			a = GoodHero(ds1['Name'][i])
		else:
			a = Hero(ds1['Name'][i])
		a.hasName.append(ds1['Name'][i])

		##Add all names and aliases to the entity through the hasName role
		a.hasName.append(ds1['Name'][i])

		if len(ds1['Full name'][i])>2:
			a.hasName.append(ds1['Full name'][i])

		if 'No alter egos' not in ds1['Alter Egos'][i]:
			if ',' in ds1['Alter Egos'][i]:
				for n in ds1['Alter Egos'][i].split(','):
					a.hasName.append(n)
			else:
				a.hasName.append(ds1['Alter Egos'][i])

		if len(ds1['Aliases'][i])>2:
			if ',' in ds1['Aliases'][i]:
				for n in ds1['Aliases'][i].split(','):
					a.hasName.append(n)
			else:
				a.hasName.append(ds1['Aliases'][i])


		## Add the year of First appearance
		years = re.findall("[12][0-9][0-9][0-9]", ds1['First appearance'][i])
		if len(years)>0:
			for y in years:
				#b = Year(y)
				a.hasFirstAppearanceYear.append(int(y))

		## Add all locations:
		llo = ds1['Place of birth'][i]
		if len(llo)>4:
			print(llo)
			latlongs = t2l(llo)
			if len(latlongs)>0:
				for l in latlongs:
					b = Location(l)
					if latlongs[l] is not None:
						b.hasLatitude.append(latlongs[l][0])
						b.hasLongtitude.append(latlongs[l][1])
					a.hasLocation.append(b)

		if len(ds1['Base'][i])>2:
			lcs = ds1['Base'][i]
			llcs = t2l(lcs)
			if len(llcs)>1:
				for l in llcs:
					if l not in Location.instances():
						b = Location(l)
						if llcs[l] is not None:
							b.hasLatitude.append(llcs[l][0])
							b.hasLongtitude.append(llcs[l][1])
						a.hasLocation.append(b)

	###Now ds4 and ds5 (dc, marvel)
	## ALAGI
	onto.save('hero1.owl')
	
	
	for ds in [ds4,ds5]:
		for i in range(ds.shape[0]):
			print(str(i/ds.shape[0]))
			nam = ds['name'][i]
			nam  = nam.replace("\\","")
			nam = nam.replace("%","")
			nam = nam.replace("#","")
			nam = nam.replace('"',"")
			print(nam)
			if '(' in nam:
				nam = nam.replace(')','')
				
				nams = nam.split('(')
			else:
				nams = [nam]
			#print(nams)
			nams = [n for n in nams if 'New Earth' not in n and 'Earth-' not in n]
			#print(nams)
			exists = None
			for n in nams:
				if n in onto.Hero.instances():
					exists = n
			if exists is not None:
				for n in nams:
					if n!=exists:
						a = Hero[exists]
						a.hasName.append(n)

			else:

				if 'Bad' in str(ds['ALIGN'][i]):
					a = onto.EvilHero(nams[0])
				elif 'Good' in str(ds['ALIGN'][i]):
					a = onto.GoodHero(nams[0])
				else:
					a = onto.Hero(nams[0])
				a.hasName.append(nams[0])

				if len(nams)>1:
					a.hasName.append(nams[1])



			if 'YEAR' in ds:
				#if ds['YEAR'][i] not in Year.instances():
				#	b = Year(ds['YEAR'][i])
				a.hasFirstAppearanceYear.append(int(ds['YEAR'][i]))
			else:
				#b = Year(ds['Year'][i])
				a.hasFirstAppearanceYear.append(int(ds['Year'][i]))

	'''
	##Now crime
	for s in ds_crime:
		print(s)
	##ALAGI
	#onto.save('hero2.owl')
	visited = set()
	for i in range(ds_crime.shape[0]):
		print(str(i/ds_crime.shape[0]))
		locs = ds_crime['agency_jurisdiction'][i]

		print(locs)
		ll = get_locations(locs)
		#to_be_parsed = list()
		#for l in ll:
		#	if l not in visited:
		#		to_be_parsed.append(l)
		#		visited.add(l)

		#lli = locs2locations(to_be_parsed)
		#lli = t2l(locs)
		print('done')
		for l in ll:
			'''
			if l not in onto.Location.instances():
				a = onto.Location(l)
				if len(lli[l])>1:
					a.hasLatitude.append(lli[l][0])
					a.hasLongtitude.append(lli[l][1])
			'''
			yr = str(ds_crime['report_year'][i])

			f =0.0
			if ds_crime['crimes_percapita'][i] is not None and 'nan' not in str(ds_crime['crimes_percapita'][i]):
				f = float(ds_crime['crimes_percapita'][i])

			loc = l
			if '1975' in yr:
				onto[loc].has_crimerate_1975.append(f)
			elif '1976' in yr:
				onto[loc].has_crimerate_1976.append(f)
			elif '1977' in yr:
				onto[loc].has_crimerate_1977.append(f)
			elif '1978' in yr:
				onto[loc].has_crimerate_1978.append(f)
			elif '1979' in yr:
				onto[loc].has_crimerate_1979.append(f)
			elif '1980' in yr:
				onto[loc].has_crimerate_1980.append(f)
			elif '1981' in yr:
				onto[loc].has_crimerate_1981.append(f)
			elif '1982' in yr:
				onto[loc].has_crimerate_1982.append(f)
			elif '1983' in yr:
				onto[loc].has_crimerate_1983.append(f)
			elif '1984' in yr:
				onto[loc].has_crimerate_1984.append(f)
			elif '1985' in yr:
				onto[loc].has_crimerate_1985.append(f)
			elif '1986' in yr:
				onto[loc].has_crimerate_1986.append(f)
			elif '1987' in yr:
				onto[loc].has_crimerate_1987.append(f)
			elif '1988' in yr:
				onto[loc].has_crimerate_1988.append(f)
			elif '1989' in yr:
				onto[loc].has_crimerate_1989.append(f)
			elif '1990' in yr:
				onto[loc].has_crimerate_1990.append(f)
			elif '1990' in yr:
				onto[loc].has_crimerate_1990.append(f)
			elif '1991' in yr:
				onto[loc].has_crimerate_1991.append(f)
			elif '1992' in yr:
				onto[loc].has_crimerate_1992.append(f)
			elif '1993' in yr:
				onto[loc].has_crimerate_1993.append(f)
			elif '1994' in yr:
				onto[loc].has_crimerate_1994.append(f)
			elif '1995' in yr:
				onto[loc].has_crimerate_1995.append(f)
			elif '1996' in yr:
				onto[loc].has_crimerate_1996.append(f)
			elif '1997' in yr:
				onto[loc].has_crimerate_1997.append(f)
			elif '1998' in yr:
				onto[loc].has_crimerate_1998.append(f)
			elif '1999' in yr:
				onto[loc].has_crimerate_1999.append(f)
			elif '2000' in yr:
				onto[loc].has_crimerate_2000.append(f)
			elif '2001' in yr:
				onto[loc].has_crimerate_2001.append(f)
			elif '2002' in yr:
				onto[loc].has_crimerate_2002.append(f)
			elif '2003' in yr:
				onto[loc].has_crimerate_2003.append(f)
			elif '2004' in yr:
				onto[loc].has_crimerate_2004.append(f)
			elif '2005' in yr:
				onto[loc].has_crimerate_2005.append(f)
			elif '2006' in yr:
				onto[loc].has_crimerate_2006.append(f)
			elif '2007' in yr:
				onto[loc].has_crimerate_2007.append(f)
			elif '2008' in yr:
				onto[loc].has_crimerate_2008.append(f)
			elif '2009' in yr:
				onto[loc].has_crimerate_2009.append(f)
			elif '2010' in yr:
				onto[loc].has_crimerate_2010.append(f)
			elif '2011' in yr:
				onto[loc].has_crimerate_2011.append(f)
			elif '2012' in yr:
				onto[loc].has_crimerate_2012.append(f)
			elif '2013' in yr:
				onto[loc].has_crimerate_2013.append(f)
			elif '2014' in yr:
				onto[loc].has_crimerate_2014.append(f)
			elif '2015' in yr:
				print(f)
				onto[loc].has_crimerate_2015.append(f)




onto.save('hero2.owl')

