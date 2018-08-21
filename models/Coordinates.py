class Coordinates:
   'Common base class for coordinate information'

   def __init__(self, lat, lon, time):
      self.lat = lat
      self.lon = lon
      self.time = time

   def displayCoordinates(self):
      print "Latitude : ", self.lat,  ", Longitute: ", self.lon, ", time of event ", time