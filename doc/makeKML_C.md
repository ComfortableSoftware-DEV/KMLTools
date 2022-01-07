

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
    - Accounts for gx: modes.
    - Defaults to clampToGround.
    - Only the first mode found will be returned.
      1. relativeToGround
      2. clampToGround
      3. absolute
      4. clampToSeaFloor
      5. relativeToSeaFloor
      - ### absolute_=False
        - The altitude value will be interpreted by GE as meters above sea level.
      - ### clampToGround_=False  ***NOTE*** default by else.
        - For a camera, this setting also places the camera relativeToGround, since putting the camera exactly at terrain height would mean that the eye would intersect the terrain \(and the view would be blocked\).
        - Camera items will change this to relativeToGround automatically, a camera clamped to ground would see only the ground the camera is clamped to, nothing else.
      - ### clampToSeaFloor_=False
        - Altitude value is ignored and will be set to local sea floor, relativeToSeaFloor for camera items.
      - ### numTabs_=None
        - The number of tabs to put in front of the tag starting and ending tag lines, will auto adjust internally if needed.
      - ### relativeToGround_=False
        - Interprets the <altitude> as a value in meters above the ground. If the point is over water, the <altitude> will be interpreted as a value in meters above sea level. See <gx:altitudeMode> below to specify points relative to the sea floor.
      - ### relativeToSeaFloor_=False


#
