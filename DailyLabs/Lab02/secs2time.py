##Well I completely misinterpreted what the question was asking.... I wrote the code to do this.... ENJOY!

##First I'm going to get an input from the user asking for a time in seconds
##Take that number and divide it by 60 to get minutes
##Take minutes and do remainder with seconds and assign that number to seconds
##Take minutes and divide by 60 to get hours
##Take hours and do remainder with minutes and assign that number to minutes
##Output all 3 variables: hours, minutes, seconds

seconds = int(input("Give me a time in seconds:"))
minutes = seconds // 60
hours = minutes // 60
minutes = -1 * ((hours * 60) - minutes)
seconds = -1 * (((hours * 60 * 60) + (minutes * 60)) - seconds
)
print(hours, minutes, seconds)


