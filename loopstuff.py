#! /usr/local/bin/python3

cities = ["london",
  "new york",
  "paris",
  "oslo",
  "helsinki"]

for city in cities:
  print(city)

colors = { 'crimson': 0xdc143c,
  'coral': 0xff7f50,
  'teal': 0x008080}

# sends the key, not the value
for color in colors:
  print(color, colors[color]) # decimal colors
