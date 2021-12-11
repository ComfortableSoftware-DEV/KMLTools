#! /usr/bin/env /usr/bin/python


import maidenhead_C
from makeKML_C import makeKML_C
MH = maidenhead_C.maidenhead()


with makeKML_C(fileName_="output.kml") as KML:
	KML.documentTop()
	_point_ = KML.point(numTabs_=2)
	KML.placemark(geometry_=_point_, numTabs_=1)
	KML.documentEnd()
	print(KML.STR_TO_RETURN)

#
