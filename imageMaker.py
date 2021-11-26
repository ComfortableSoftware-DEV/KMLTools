#! /usr/bin/env /usr/bin/python


import maidenhead_C
MH = maidenhead_C.maidenhead()


print(f"""{MH.latLonToMaidenhead(lat_=  0, lon_=-180, chrs_=12)}""")


#
