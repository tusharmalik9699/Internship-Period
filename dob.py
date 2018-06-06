import datetime
year = datetime.datetime.now().year
year_of_birth = int(input("Enter your birth year :"))
print "You are %i years old !" %(year - year_of_birth)