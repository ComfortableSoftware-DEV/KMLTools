

GRID_02_POLY_STR = lambda *, __NAME__, __STYLE__, __WEST__, __SOUTH__, __NORTH__, __EAST__, __ALT__: f"""
		<Placemark>
			<name>{__NAME__}</name>
			<styleUrl>#{__STYLE__}</styleUrl>
			<Polygon>
				<tessellate>1</tessellate>
				<outerBoundaryIs>
					<LinearRing>
						<coordinates>
							{__WEST__:0f},{__SOUTH__},__ALT__ {__WEST__},{__NORTH__},__ALT__ {__EAST__},{__NORTH__},__ALT__ {__EAST__},{__SOUTH__},__ALT__ {__WEST__},{__SOUTH__},__ALT__
						</coordinates>
					</LinearRing>
				</outerBoundaryIs>
			</Polygon>
		</Placemark>
"""

STYLE_STR = lambda f"""
	<Style id="sn_ylw-pushpin0">
		<IconStyle>
			<scale>1.1</scale>
			<Icon>
				<href>http://maps.google.com/mapfiles/kml/pushpin/ylw-pushpin.png</href>
			</Icon>
			<hotSpot x="20" y="2" xunits="pixels" yunits="pixels"/>
		</IconStyle>
		<LineStyle>
			<color>ff00ff00</color>
		</LineStyle>
		<PolyStyle>
			<color>6600ffaa</color>
			<colorMode>random</colorMode>
		</PolyStyle>
	</Style>

"""
class maidenhead(object):
	# fold here ⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1
	def __init__(self):
		pass

	# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
	# start of __init__
	# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
	def __init__(self):
		# fold here ⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2
		self._ONE_TWO_CHAR_LIST_ = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R"]
		self._THREE_FOUR_CHAR_LIST = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
		self._FIVE_SIX_CHAR_LIST_ = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x"]
		self._SEVEN_EIGHT_CHAR_LIST_ = self._THREE_FOUR_CHAR_LIST.copy()
		self._NINE_TEN_CHAR_LIST_ = self._FIVE_SIX_CHAR_LIST_.copy()
		self._ELEVEN_TWELVE_CHAR_LIST_ = self._THREE_FOUR_CHAR_LIST.copy()
		self._THIRTEEN_FOURTEEN_CHAR_LIST = self._FIVE_SIX_CHAR_LIST_.copy()

		self._ONE_TWO_LAT_INC_ = 180 / len(self._ONE_TWO_CHAR_LIST_)
		self._ONE_TWO_LON_INC_ = 360 / len(self._ONE_TWO_CHAR_LIST_)
		self._THREE_FOUR_LAT_INC_ = self._ONE_TWO_LAT_INC_ / len(self._THREE_FOUR_CHAR_LIST)
		self._THREE_FOUR_LON_INC_ = self._ONE_TWO_LON_INC_ / len(self._THREE_FOUR_CHAR_LIST)
		self._FIVE_SIX_LAT_INC_ = self._THREE_FOUR_LAT_INC_ / len(self._FIVE_SIX_CHAR_LIST_)
		self._FIVE_SIX_LON_INC_ = self._THREE_FOUR_LON_INC_ / len(self._FIVE_SIX_CHAR_LIST_)
		self._SEVEN_EIGHT_LAT_INC_ = self._FIVE_SIX_LAT_INC_ / len(self._THREE_FOUR_CHAR_LIST)
		self._SEVEN_EIGHT_LON_INC_ = self._FIVE_SIX_LON_INC_ / len(self._THREE_FOUR_CHAR_LIST)
		self._NINE_TEN_LAT_INC_ = self._SEVEN_EIGHT_LAT_INC_ / len(self._FIVE_SIX_CHAR_LIST_)
		self._NINE_TEN_LON_INC_ = self._SEVEN_EIGHT_LON_INC_ / len(self._FIVE_SIX_CHAR_LIST_)
		self._ELEVEN_TWELVE_LAT_INC_ = self._NINE_TEN_LAT_INC_ / len(self._THREE_FOUR_CHAR_LIST)
		self._ELEVEN_TWELVE_LON_INC_ = self._NINE_TEN_LON_INC_ / len(self._THREE_FOUR_CHAR_LIST)
		self._THIRTEEN_FOURTEEN_LAT_INC_ = self._ELEVEN_TWELVE_LAT_INC_ / len(self._FIVE_SIX_CHAR_LIST_)
		self._THIRTEEN_FOURTEEN_LON_INC_ = self._ELEVEN_TWELVE_LON_INC_ / len(self._FIVE_SIX_CHAR_LIST_)

		self._ONE_TWO_RANGES_ = {
				"EAST": (360 / 2),
				"WEST": -(360 / 2),
				"NORTH": (180 / 2),
				"SOUTH": -(180 / 2),
		}

		self._THREE_FOUR_RANGES_ = {
				"EAST": self._ONE_TWO_LAT_INC_,
				"WEST": (0),
				"NORTH": self._ONE_TWO_LON_INC_,
				"SOUTH": (0),
		}

		self._FIVE_SIX_RANGES_ = {
				"EAST": self._THREE_FOUR_LAT_INC_,
				"WEST": (0),
				"NORTH": self._THREE_FOUR_LON_INC_,
				"SOUTH": (0),
		}

		self._SEVEN_EIGHT_RANGES_ = {
				"EAST": self._FIVE_SIX_LAT_INC_,
				"WEST": (0),
				"NORTH": self._FIVE_SIX_LON_INC_,
				"SOUTH": (0),
		}

		self._NINE_TEN_RANGES_ = {
				"EAST": self._SEVEN_EIGHT_LAT_INC_,
				"WEST": (0),
				"NORTH": self._SEVEN_EIGHT_LON_INC_,
				"SOUTH": (0),
		}

		self._ELEVEN_TWELVE_RANGES_ = {
				"EAST": self._NINE_TEN_LAT_INC_,
				"WEST": (0),
				"NORTH": self._NINE_TEN_LON_INC_,
				"SOUTH": (0),
		}

		self._THIRTEEN_FOURTEEN_RANGES_ = {
				"EAST": self._ELEVEN_TWELVE_LAT_INC_,
				"WEST": (0),
				"NORTH": self._ELEVEN_TWELVE_LON_INC_,
				"SOUTH": (0),
		}

		# fold here ⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2
	# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
	# end of __init__
	# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*

	# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
	# start of makeGrid02
	# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
	def makeGrid02(self):
		# fold here ⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2

		# fold here ⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2
	# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
	# end of makeGrid02
	# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*


	# fold here ⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1
