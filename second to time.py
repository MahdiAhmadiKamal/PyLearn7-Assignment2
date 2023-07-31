import math

seconds = int (input ("enter time in seconds: "))

hour = math.trunc (seconds/3600)
min = math.trunc ((seconds - hour * 3600)/60)
sec = seconds - hour * 3600 - min * 60

print ("time is", hour,":",min,":",sec)