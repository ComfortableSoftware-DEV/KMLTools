

from CF.CONST_D import _00_VALS as CFV


class makeKML_C(object):

	# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
	# start of __init__
	# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
	def __init__(self, *,
			fileName_,
	):
		# fold here ⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2
		self.FILENAME = fileName_
		self.STR_TO_RETURN = ""
		self.FILE_STARTED = False
		self.FILE_WRITTEN = False
		self.FILE_ENDED = False
		# fold here ⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2
	# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
	# end of __init__
	# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*

	# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
	# * start of documentTop
	# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
	def documentTop(self, *,
			name_,
			isVisible_=1,
			isOpen_=0,
			authorName_=None,
			link_=None,
			address_=None,
			addressDetails_=None,
			phoneNumber_=None,
			snippet_=None,
			snippetMaxLines_=2,
			description_=None,
			camera_=None,
			lookat_=None,
			timePrimitive_=None,
			styleUrl_=None,
			styleSelector_=None,
			region_=None,
			extendedData_=None,
	):
		# fold here ⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1

		self.STR_TO_RETURN += f"""<?xml version="1.0" encoding="UTF-8"?>
<kml xmlns="http://www.opengis.net/kml/2.2" xmlns:gx="http://www.google.com/kml/ext/2.2" xmlns:kml="http://www.opengis.net/kml/2.2" xmlns:atom="http://www.w3.org/2005/Atom">
<Document>
	<name>{name_}</name>
	<visibility>{isVisible_}</visibility>
	<open>{isOpen_}</open>
"""
		# 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱
		if (
				(authorName_ is not None)
		):
			self.STR_TO_RETURN += f"""	<author>
		<atom:name>{authorName_}</atom:name>
	</author>
"""
		# ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2
		# * 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱
		if (
				(link_ is not None)
		):
			self.STR_TO_RETURN += f"""	<atom:link href="{link_}"/>"""
		# * ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2
		# * 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱
		if (
				(address_ is not None)
		):
			self.STR_TO_RETURN += f"""	"""
		# * ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2
		# fold here ⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1
	# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
	# * end of documentTop
	# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
