# File to convert a pvpPoke exported csv to the format that our website uses
import csv

# The csv file exported from PvPoke with the entire list of eligible pokemon
monList = "/Users/shreyash/Documents/devtrees/PoGoBlr/G20Cup.csv"
# The file to write the Pokemon List to
writeList = "/Users/shreyash/Documents/devtrees/PoGoBlr/dreeverbeku/mysite/monlist.txt"
# writeList = "/Users/shreyash/Documents/devtrees/PoGoBlr/testOut.txt"

finalList = "["

with open(monList, "r") as file:
    csvFile = csv.DictReader(file)
    for line in csvFile:
        mon = line["Pokemon"]
        mon = mon.replace(" (Alolan)", "-alolan")
        mon = mon.replace(" (Galarian)", "-galarian")
        mon = mon.replace(" (Hisuian)", "-hisuian")
        mon = mon.replace(" (Defense)", "_defense")
        mon = mon.replace(" (Speed)", "_speed")
        mon = mon.replace(" (Land)", "_land")
        mon = mon.replace(" (Sky)", "_sky")
        mon = mon.replace(" (Female)", "_female")
        mon = mon.replace(" (Midnight)", "_midnight")
        mon = mon.replace(" (Snowy)", "_snowy")
        mon = mon.replace(" (Rainy)", "_rainy")
        mon = mon.replace(" (Sunny)", "_sunny")
        mon = mon.replace(" (Trash)", "_trash")
        mon = mon.replace(" (Super)", "_super")
        mon = mon.replace(" (Large)", "_large")
        mon = mon.replace(" (Average)", "_average")
        mon = mon.replace(" (Small)", "_small")
        mon = mon.replace(" (Sunshine)", "_sunshine")
        mon = mon.replace(" (Sensu)", "_sensu")
        mon = mon.replace(" (Baile)", "_baile")
        mon = mon.replace(" (Pom-Pom)", "_pom_pom")
        mon = mon.replace(" (Male)", "")
        mon = mon.replace(" (50% Forme)", "")
        mon = mon.replace(" (10% Forme)", "")
        mon = mon.replace(" (Pa'u)", "_pau")
        mon = mon.replace(" (Mow)", "_mow")
        mon = mon.replace(" (Wash)", "_wash")
        mon = mon.replace(" (Plant)", "_plant")
        mon = mon.replace(" (Frost)", "_frost")
        mon = mon.replace(" (Sandy)", "_sandy")
        mon = mon.replace(" (Overcast)", "_overcast")
        mon = mon.replace(" (Standard)", "_standard")
        mon = mon.replace(" (Midday)", "_midday")
        mon = mon.replace(" (Dusk)", "_dusk")
        mon = mon.replace(" (Midnight)", "_midnight")
        mon = mon.replace("Tapu ", "Tapu_")
        mon = mon.replace("-Z", "_Z")
        mon = mon.replace("'d", "d")
        mon = mon.replace(" (Shadow)", "_shadow")

        if mon.count("(") > 0:
            print(mon)
        else:
            if len(finalList) > 2:
                #First pokmeon doesn't need a , before it
                finalList = finalList + ", '" + mon.lower() + "'"
            else:
                finalList = finalList + "'" + mon.lower() + "'"

finalList = finalList + "]"
listFile = open(writeList, 'w')
listFile.write(finalList)
listFile.close()
