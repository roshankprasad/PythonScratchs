Actors = [("Rajkumar",35,"Mumbai"),
              ("Hrithik",40,"Mumbai-east"),
              ("Ajay",50,"South-Mumbai")]
#
# for actor in Actors:
#     print('{},{},{}'.format(actor[0],actor[1],actor[2]))
print("Success!")

outfile = open("myfile.csv",'w')
for actor in Actors:
    outfile.write('{},{},{}'.format(actor[0],actor[1],actor[2]))
    outfile.write("\n")
outfile.close()