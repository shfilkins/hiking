import math
distance = float(raw_input("Enter the distance of the hike, eg 6.25km: "))
start_elevation = float(raw_input("Enter the starting elevation of your hike: "))
goal_elevation = float(raw_input("Enter the ending elevation of your hike: "))
elevation_gain = goal_elevation - start_elevation

print "\nYour hiking distance is: %.2f kilometers." % distance 
#print "Your starting elevation is %d meters.\n" % start_elevation
#print "Your ending elevation is %d meters.\n" % goal_elevation
print "The elevation gain is %d meters.\n" % elevation_gain


z = float(distance/3)*60 
y = float(elevation_gain/308) * 30
oneway_distance = float((z + y)/60)
roundtrip_distance = float(oneway_distance + float(z/60))
#this uses math.modf to separate the hours from the mins at the decimal point.
#it returns two values (mins, hours), i get these into the variables
#below, onewaymins and onewayhours for oneway and the others for roundtrip.
onewaymins, onewayhours = math.modf(oneway_distance)
roundwaymins, roundwayhours = math.modf(roundtrip_distance)

#This is to turn the decimal value into one based on the clock.  Example: oneway_distance
#will return 2.42 for a time.  .42 is 25 mins, but to get it you need to multiply * 60.
onewaymin1 = onewaymins*60
roundwaymin1 = roundwaymins*60
 
print "Your distance, %.2f km, divided by your speed, 3 km/hr is %.2f minutes." % (distance, z)
print "Your elevation time is your elevation gain/308 * 30.  This is %.2f minutes.\n" % y
print "Your total ONE-WAY time to your goal is %d hours, %d mins.\n" % (onewayhours, onewaymin1)
print "Your total ROUND TRIP time to your goal is %d hours, %d mins." % (roundwayhours, roundwaymin1)






