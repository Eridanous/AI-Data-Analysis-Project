from owlready2 import *


#crimerates = [has_CrimeRate_1975,has_CrimeRate_1976,has_CrimeRate_1977,has_CrimeRate_1978,has_CrimeRate_1979,has_CrimeRate_1980,has_CrimeRate_1981,has_CrimeRate_1982,has_CrimeRate_1983,has_CrimeRate_1984,has_CrimeRate_1985,has_CrimeRate_1986,has_CrimeRate_1987,has_CrimeRate_1988,has_CrimeRate_1989,has_CrimeRate_1990,has_CrimeRate_1991,has_CrimeRate_1992,has_CrimeRate_1993,has_CrimeRate_1994,has_CrimeRate_1995,has_CrimeRate_1996,has_CrimeRate_1997,has_CrimeRate_1998,has_CrimeRate_1999,has_CrimeRate_2000,has_CrimeRate_2001,has_CrimeRate_2002,has_CrimeRate_2003,has_CrimeRate_2004,has_CrimeRate_2005,has_CrimeRate_2006,has_CrimeRate_2007,has_CrimeRate_2008,has_CrimeRate_2009,has_CrimeRate_2010,has_CrimeRate_2011,has_CrimeRate_2012,has_CrimeRate_2013,has_CrimeRate_2014,has_CrimeRate_2015]

def get_year_info(yr):
	onto = get_ontology("file://hero.owl").load()

	with onto:
		hers = onto.search(hasFirstAppearanceYear=yr, hasLocation=onto.search(hasLongtitude='*'))
		if yr==1975:
			crim = onto.search(has_crimerate_1975='*')
		elif yr ==1976:
			crim = onto.search(has_crimerate_1976='*')
		elif yr ==1977:
			crim = onto.search(has_crimerate_1977='*')
		elif yr ==1978:
			crim = onto.search(has_crimerate_1978='*')
		elif yr ==1979:
			crim = onto.search(has_crimerate_1979='*')
		elif yr ==1980:
			crim = onto.search(has_crimerate_1980='*')
		elif yr ==1981:
			crim = onto.search(has_crimerate_1981='*')
		elif yr ==1982:
			crim = onto.search(has_crimerate_1982='*')
		elif yr ==1983:
			crim = onto.search(has_crimerate_1983='*')
		elif yr ==1984:
			crim = onto.search(has_crimerate_1984='*')
		elif yr ==1985:
			crim = onto.search(has_crimerate_1985='*')
		elif yr ==1986:
			crim = onto.search(has_crimerate_1986='*')
		elif yr ==1987:
			crim = onto.search(has_crimerate_1987='*')
		elif yr ==1988:
			crim = onto.search(has_crimerate_1988='*')
		elif yr ==1989:
			crim = onto.search(has_crimerate_1989='*')
		elif yr ==1990:
			crim = onto.search(has_crimerate_1990='*')
		elif yr ==1991:
			crim = onto.search(has_crimerate_1991='*')
		elif yr ==1992:
			crim = onto.search(has_crimerate_1992='*')
		elif yr ==1993:
			crim = onto.search(has_crimerate_1993='*')
		elif yr ==1994:
			crim = onto.search(has_crimerate_1994='*')
		elif yr ==1995:
			crim = onto.search(has_crimerate_1995='*')
		elif yr ==1996:
			crim = onto.search(has_crimerate_1996='*')
		elif yr ==1997:
			crim = onto.search(has_crimerate_1997='*')
		elif yr ==1998:
			crim = onto.search(has_crimerate_1998='*')
		elif yr ==1999:
			crim = onto.search(has_crimerate_1999='*')
		elif yr ==2000:
			crim = onto.search(has_crimerate_2000='*')
		elif yr ==2001:
			crim = onto.search(has_crimerate_2001='*')
		elif yr ==2002:
			crim = onto.search(has_crimerate_2002='*')
		elif yr ==2003:
			crim = onto.search(has_crimerate_2003='*')
		elif yr ==2004:
			crim = onto.search(has_crimerate_2004='*')
		elif yr ==2005:
			crim = onto.search(has_crimerate_2005='*')
		elif yr ==2006:
			crim = onto.search(has_crimerate_2006='*')
		elif yr ==2007:
			crim = onto.search(has_crimerate_2007='*')
		elif yr ==2008:
			crim = onto.search(has_crimerate_2008='*')
		elif yr ==2009:
			crim = onto.search(has_crimerate_2009='*')
		elif yr ==2010:
			crim = onto.search(has_crimerate_2010='*')
		elif yr ==2011:
			crim = onto.search(has_crimerate_2011='*')
		elif yr ==2012:
			crim = onto.search(has_crimerate_2012='*')
		elif yr ==2013:
			crim = onto.search(has_crimerate_2013='*')
		elif yr ==2014:
			crim = onto.search(has_crimerate_2014='*')
		elif yr ==2015:
			crim = onto.search(has_crimerate_2015='*')

		
		#print(str(crim))
		#for c in crim:
		#	print(c.hasLongtitude)

	return hers,crim

h,crim = get_year_info(1999)

print(len(h))
print(len(crim))

#print(str(inf))
#print(str(type(inf)))


