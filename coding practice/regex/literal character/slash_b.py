import re
text="The average distance from the " \
"Earth to the Moon is approximately 384,400 kilometers. Light travels at a speed of about 299,792,458 meters per second, meaning it takes roughly 1.3 seconds for a radio signal to reach the lunar surface."

print(re.findall(r"\bE\w*",text)) #it is a word boundary gives the ,matches the position from where the word start and ends 