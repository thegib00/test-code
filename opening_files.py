#csv is used for the reader() method.
import csv

#file name as input.
newFile = str(input())

#dictionary structure is as follows: movie_name: {times: [], ratings: []}.
dictionary = {}

#set holding dictionary names.
dict_names = []

#opens 'movies.csv' and splits the rows into lists, seperated by ','.
with open(newFile, 'r') as movies:
    file = csv.reader(movies, delimiter=',')

    #adds row into the dictionary.
    for row in file:
        try:
            #if row[1] is not in dictionary, then add it.
            if row[1] not in dictionary:
                dictionary[str(row[1])] = {'times':[str(row[0])], 'ratings':[str(row[2])]}

                #add dictionary names to dict_names list if not already there.
                if row[1] in dict_names:
                    pass
                elif row[1] not in dict_names:
                    dict_names.append(str(row[1]))

            #if row[1] is already in dictionary, then add it to a nested dict.
            elif row[1] in dictionary:
                try:
                    dictionary[str(row[1])]['times'].append(row[0])
                    dictionary[str(row[1])]['ratings'].append(row[1])
                except Exception as e:
                    print(e)

                #add dictionary names to dict_names list if not already there.
                if row[1] in dict_names:
                    pass
                elif row[1] not in dict_names:
                    dict_names.append(str(row[1]))
            
        except Exception as e:
            print(e)

#function to prevent dict_names value from exceeding 44 characters long.
def shorten(value):
    if len(value) > 44:
        shorten_by = 44 - len(value)
        return value[:shorten_by]
    else:
        return value

#function to return the show times in the correct format.
def showTimes(times):
    combined = ' '.join(times)
    return combined

#output contents in table with NAME | RATING | TIMES.
for value in dict_names:
    changed_value = shorten(value)
    show_times = showTimes(dictionary[value]['times'])
    rating = dictionary[value]['ratings'][0]
    
    print(f'{changed_value:<44} | {rating:>5} | {show_times}')




