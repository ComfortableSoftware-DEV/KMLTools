

# makeKML_C
  - ## \_\_init\_\_ self, *,
    - Initialize the class.
    - ### fileName_=None,
      - Will write a file if this name is valid.
      - You need to get a copy of self.STR_TO_RETURN before the class is destroyed if you are not writing a file.
      - #### self.FILENAME
        - A copy of the fileName_ given on entry.
      - #### self.STR_TO_RETURN
        - The string built by this class, read it before \_\_exit\_\_ is called if you are not writing KML to a file.
        - If the filename is valid this string will be written to self.FILENAME when \_\_exit\_\_ is called.
      - #### self.ROOT_TAB_LEVEL
        - The current tab level of the file when you are using the defaults, not returning strings from document and folder and networkLink containers.
      - #### self.STATUS_LIST
        - Should contain the current container type, items are added when self.document\(\) or self.folder\(\) or self.networkLink\(\) are called
  - ## \_\_enter\_\_ self.STR_TO_RETURN
    - Returns self.
  - ## \_\_exit\_\_ self, *args
    - Writes self.STR_TO_RETURN to self.FILENAME, no error checking.
  - ## altitudeMode_R self, *,
    - Returns a string containing an altitude mode.
    - Only the first mode in alphabetical order will be returned.
      - ### absolute_=False,
      - ### clampToGround_=False,  # default by else:
      - ### clampToSeaFloor_=False,
      - ### numTabs_=None,
      - ### relativeToGround_=False,
      - ### relativeToSeaFloor_=False,


#
