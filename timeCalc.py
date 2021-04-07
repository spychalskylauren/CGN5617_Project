import random

def main(fileIn, timesFile, fileOut):
    
    cdf = CDF_calc(timesFile)
    
    records = read_file(fileIn)
    
    times = ["000-059", "100-159", "200-259", "300-359", "400-459", "500-559",
             "600-659", "700-759", "800-859", "900-959","1000-1059","1100-1159",
             "1200-1259","1300-1359","1400-1459","1500-1559","1600-1659","1700-1759",
             "1800-1859","1900-1959","2000-2059","2100-2159","2200-2259","2300-2359"]
    soc = ["low","medium","high"]
    
    headers = []
    
    for s in soc:
        for t in times:
            head = "soc="+s+":"+t
            headers.append(head)
    
    random.seed(10000)
    
    for r in records:
        tripDist = [0 for x in range(len(cdf)*3)]
        for trip in range(int(r["Trips"])):
            rand = random.random()
            index = 0
            while cdf[index] < rand:
                index += 1
            soc = random.randint(0,2)
            tripDist[(soc*24)+index] += 1
        tripTimes = dict(zip(headers, tripDist))
        r.update(tripTimes)
    
    write_file(fileOut, records)
    

def CDF_calc(fileIn):
    
    f = open(fileIn,"r",encoding='utf-8-sig')

    # Initialize list of times
    times = []

    # For each line of data in the file
    for y in f:
        # Read each line 
        line = y.replace("\n","").replace(",","")
        times.append(int(line))

    # Close file
    f.close()
    
    timeBuckets = [0 for x in range(24)]
    total = 0
    
    for t in times:
        if t < 100:
            timeBuckets[0] += 1
        elif t < 200:
            timeBuckets[1] += 1
        elif t < 300:
            timeBuckets[2] += 1
        elif t < 400:
            timeBuckets[3] += 1
        elif t < 500:
            timeBuckets[4] += 1
        elif t < 600:
            timeBuckets[5] += 1
        elif t < 700:
            timeBuckets[6] += 1
        elif t < 800:
            timeBuckets[7] += 1
        elif t < 900:
            timeBuckets[8] += 1
        elif t < 1000:
            timeBuckets[9] += 1
        elif t < 1100:
            timeBuckets[10] += 1
        elif t < 1200:
            timeBuckets[11] += 1
        elif t < 1300:
            timeBuckets[12] += 1
        elif t < 1400:
            timeBuckets[13] += 1
        elif t < 1500:
            timeBuckets[14] += 1
        elif t < 1600:
            timeBuckets[15] += 1
        elif t < 1700:
            timeBuckets[16] += 1
        elif t < 1800:
            timeBuckets[17] += 1
        elif t < 1900:
            timeBuckets[18] += 1
        elif t < 2000:
            timeBuckets[19] += 1
        elif t < 2100:
            timeBuckets[20] += 1
        elif t < 2200:
            timeBuckets[21] += 1
        elif t < 2300:
            timeBuckets[22] += 1
        elif t < 2400:
            timeBuckets[23] += 1
        total += 1
        
    pdf = [(timeBuckets[x]/total) for x in range(len(timeBuckets))]
    cdf = [0 for x in range(len(pdf))]
            
    for i in range(len(pdf)):
        if i == 0:
            cdf[i] = pdf[i]
        else:
            cdf[i] = cdf[i-1] + pdf[i]
                
    return cdf

# Function will take a list of csv files and read them into a list of file classes
# Input:  file path
#         String
# Output: list of file data
#         list[dictionary]
def read_file(file):
    # Open file
    f = open(file,"r",encoding='utf-8-sig')

    # Read first line and save headers
    l = f.readline()
    header = l.replace("\n","").split(",")

    # Initialize list of records
    records = []

    # For each line of data in the file
    for y in f:

        # Read each line and save data in dictionary using headers as keys
        line = y.replace("\n","").split(",")
        record = dict(zip(header, line))

        # Add record to list of records
        records.append(record)

    # Close file
    f.close()

    # Return list of files
    return records

# Write list of dictionaries with uniform keys to a csv file
# Input:  List of dictionaries with uniform keys
#         list[Dictionary]
# Output: csv file
def write_file(filename, records):

    # Open output file
    f = open(filename, "w")

    # Create list of key values for headers
    keys = list(records[0].keys())

    # Write headers in first row
    f.write(keys[0])
    for i in keys[1:]:
        f.write(","+str(i))
    f.write("\n")

    # Write values in subsequent rows
    for i in records:
        f.write(str(i[keys[0]]))
        for j in keys[1:]:
            f.write(","+str(i[j]))
        f.write("\n")

    # Close output file
    f.close()
    
    return 0