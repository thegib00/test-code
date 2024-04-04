#csv is used for the reader() method.
import csv

#dictionary containing movies as keys and their times/ratings as values.
dictionary = {}

#opens 'movies.csv' and splits the rows into lists, seperated by ','.
with open('movies.csv', 'r') as movies:
    file = csv.reader(movies, delimiter=',')

    #adds row into the dictionary.
    for row in file:
        try:
            #NOTE: This is wrong because it doesnt add the times for duplicate movie names.
            dictionary[str(row[1])] = [str(row[0]), str(row[2])]
        except Exception as e:
            print(e)

#testing contents of dictionary.
print(dictionary)
