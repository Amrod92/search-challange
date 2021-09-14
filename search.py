import numpy as np

import json
import sys

# Opening JSON file
data = json.load(open('search_dataset.json', encoding='utf-8'))

argsCLA = str(sys.argv[1:])
target = {39 : None, 91 : None, 93 : None}
# The target function delete the ASCII character from the list
query = str(argsCLA).translate(target)

def levenshtein_distance(word, objData):
 
    word1 = len(word) + 1
    word2 = len(objData) + 1
    # Returns a new array of length 
    matrix = np.zeros ((word1, word2))
    # Length for the search item
    for x in range (word1):
        matrix [x, 0] = x
    # Length for the item inside the JSON
    for y in range (word2):
        matrix [0, y] = y

    # Variables x and y are needed to compare letter by letter - row and column wise.
    for x in range (1, word1):
        for y in range (1, word2):
            # If the two letter are equal the position at matrix[x,y] is the minimun value
            if word[x-1] == objData[y-1]:
                matrix [x,y] = min(
                    matrix[x-1, y] + 1,
                    matrix[x-1, y-1],
                    matrix[x, y-1] + 1
                )
            else:
                matrix [x,y] = min(
                    matrix[x-1,y] + 1,
                    matrix[x-1,y-1] + 1,
                    matrix[x,y-1] + 1
                )
 
    # Rounding score to decimal number
    return round(matrix[word1 - 1, word2 - 1])

def main(data, query):
    # Loop thought the JSON file and each object, name and brand, are passed inside the levenshtein_distance function to return the score
    for obj in data:
        obj["score"] = levenshtein_distance(query, obj["name"]+" "+obj["brand"])

    # Sorting returned data by score
    data.sort(key= lambda x:x['score'])
    # Slice to first ten
    first_ten = data[:10]
    
    for obj in first_ten:
        print(f"Score: {obj['score']}, ID: '{obj['id']}', Name: '{obj['name']}', Brand: '{obj['brand']}'")

if __name__ == "__main__":
    main(data, query)