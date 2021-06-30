#Soil texture determination calculation
Oven_dry_sand_fraction = input('please enter your oven dry value')
Hydrometer_reading_for_clay = input ('please enter your R_clay value')
hydrometer_reading_for_blanc1 = input ('please enter your R_C1 value')
hydrometer_reading_for_blanc2 = input ('please eneter your R_C2 value')
hydrometer_reading_for_sand = input ('please enter your R_sand value')

Oven_dry_sand_fraction = float (Oven_dry_sand_fraction)
Hydrometer_reading_for_clay = float (Hydrometer_reading_for_clay)
hydrometer_reading_for_blanc1 = float (hydrometer_reading_for_blanc1)
hydrometer_reading_for_blanc2 = float (hydrometer_reading_for_blanc2)
hydrometer_reading_for_sand = float (hydrometer_reading_for_sand)
percentage_sand = float(((Oven_dry_sand_fraction - (hydrometer_reading_for_sand - hydrometer_reading_for_blanc1))/Oven_dry_sand_fraction) * 100)
percentage_clay = float (((Hydrometer_reading_for_clay - hydrometer_reading_for_blanc2) / Oven_dry_sand_fraction) * 100 )
percentage_silt = float (100 - (percentage_sand + percentage_clay))
 
print ('percentage_sand =', percentage_sand)
print ('percentage_clay=', percentage_clay)
print ('percentage silt =', percentage_silt) 

