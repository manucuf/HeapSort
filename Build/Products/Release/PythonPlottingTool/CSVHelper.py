import csv

# Returns key value table strucured by csv columns
def readFile(csvfile, delimiter=';'):
    header = []
    table = []
    with open(csvfile, 'rt') as file:
        rowcounter = 0

        # Read csv file using delimiter. ';' default delimiter
        reader = csv.reader(file, delimiter=delimiter)
        for row in reader:
            if (rowcounter == 0):

                header = row  # stores header array
                for entry in header:
                    if entry == '':
                        header.remove(entry)

            # is not header
            else :

                for entry in row:
                    if entry == '':
                        row.remove(entry)
                
                # check is table row is a valid row (same lenght of header)

                if (len(row) == len(header)):

                    # Creates a dictionary for every row
                    tablerow = {}
                    for index, item in enumerate(row):
                        tablerow[header[index]] = item

                    # Appends rows to table array
                    table.append(tablerow)

            rowcounter += 1
        return table
