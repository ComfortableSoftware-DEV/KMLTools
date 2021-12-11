

  - RNDLEN: The length of random string used for ID and name where defaulted to random strings.

  - self.__init__
    - Initialize the class.
    - ***ALL PARAMS ARE NAMED, NO POSITIONAL PARAMS ARE USED.***
    - (fileName_): `str`.
      - None: no file will be written on exit.
    - self.FILENAME: `str`.
      - Set to the fileName_ parameter.
    - self.STR_TO_RETURN: `str`.
      - The string assembled and or saved to self.FILENAME.
  - self.__enter__:
    - Do all of the things needed to use "with makeKML_C()" work properly
    - returns self.
  - self.__exit__:
    - Code executed when exiting makeKML_C at the end of a with makeKML_C.
    - Writes the file is self.FILENAME is valid.
    - No error checking of self.FILENAME is done.
  - self.altitudeMode:
    - Sets the first found option and builds the altitude mode string.
    - (absolute_): `bool`
      - Sets the altitude mode to meters above sealevel.
    - (clampToGround_): `bool`
      - Sets the altitude mode to ground level, this is the default
