class Coordinates:
   'Common base class for coordinate information'

   def __init__(self, lat, lon, timeOfEvent):
      self.lat = lat
      self.lon = lon
      self.timeOfEvent = timeOfEvent

   def _str_(self):
      return "{Latitude : ", self.lat,  ", Longitute: ", self.lon, ", time of event ", self.timeOfEvent,"}"