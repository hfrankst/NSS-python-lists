planet_list = ["Mercury", "Mars"]
print(planet_list)
planet_list.append('Jupiter')
print(planet_list)
planet_list.append('Saturn')
print(planet_list)
planet_list.extend(['Neptune', 'Uranus'])
print(planet_list)
planet_list.append('Pluto')
print(planet_list)

rockey_planets = planet_list[slice(0, 2)]
print('The Rockey Planets: ' + str(rockey_planets))

del planet_list[6]
print(planet_list)

satellites = [('Cassini', 'Saturn'), ('Rover', 'Mars'), ('Galileo', 'Jupiter')]

for planet in planet_list:
	for satellite in satellites:
		if satellite[1] is planet:
			print('The {} satellite landed on {}'.format(satellite[0], planet))