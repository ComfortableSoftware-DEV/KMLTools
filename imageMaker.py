#! /usr/bin/env /usr/bin/python


import maidenhead_C
MH = maidenhead_C.maidenhead()


print(f"""{MH.latLonToMaidenhead(lat_= 40.687088, lon_=-111.927630, chrs_=12)}""")


#
