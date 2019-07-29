# Write a function that takes a list of pin objects, each with a height attribute, and a number of columns
# and returns a grid layout. You put the next pin in the shortest column so far. If there is a tie, insert the pin
# into the leftmost column. Return a list which contains a list for each column. The column lists each
# contain the pins in that column.
#
# pins = [ {'id':1, 'height':300},
# {'id':2, 'height':200},
# {'id':3, 'height':250},
# {'id':4, 'height':350},
# {'id':5, ‘height':100}]

# layout(pins, 2) will return this output:
# [
# # This list has the pins for the first column
# [ {'id': 1, 'height': 300},
# {'id': 4, 'height': 350} ],
# # This list has the pins for the second column
# [ {'id': 2, 'height': 200},
# {'id': 3, 'height': 250},
# {'id': 5, 'height': 100}]
# ]


def layout(pins, num_columns):
    result = [None] * num_columns
    column_heights = {} # Keeps track of all column heights
    for i in range(num_columns):
        result[i] = [] # Adds 2D structure
        column_heights[i] = 0 # Set all heights to 0
    min_height = 0
    for pin in pins:
        for index, height in column_heights.items():
            if height == min_height:
                result[index].append(pin)
                column_heights[index] += pin.height
                min_height = min(column_heights.values())
                break
    print(result)
    return result


class Pin:
    def __init__(self, pin_id, height):
        self.id = pin_id
        self.height = height

    def __repr__(self):
        return "{id: " + str(self.id) + ", height: " + str(self.height) + "}"


pins = [Pin(1, 300), Pin(2, 200), Pin(3, 250), Pin(4, 350), Pin(5, 100)]
# {'id':1, 'height':300},
# {'id':2, 'height':200},
# {'id':3, 'height':250},
# {'id':4, 'height':350},
# {'id':5, 'height':100} ]
layout(pins, 2)