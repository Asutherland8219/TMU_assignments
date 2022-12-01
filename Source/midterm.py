""" For loops are meant to be used when each item in the data needs to be looked at. For loops can also be nested and contain different types of criteria. The criteria can be conditional or any other variety. 
While loops are meant to be used to loop through data when you are looking for singular criteria. Typically, while loops have a boolean value (1/0, True/False) that is the trigger if the while loop continues or not.
While loops are often considered riskier due to the increase chances of an infinite loop from faulty logic. 

For loop example: """

students = [
    {
        "Name" : "Alex" ,
        "Grade" :"A",
        "Honors": True,
},
    { 
        "Name" : "Bobby",
        "Grade": "B",
        "Honors": False, 
},
    {
        "Name" : "Carol" ,  
        "Grade": "F",
        "Honors": False,   
    },
    {   "Name" : "Franklin",
        "Grade" :"F",
        "Honors": True,   
}
]

""" Here we are checking to see for students that received an A in the class. We then print the students that did so."""
for student in students:
    if student["Grade"] == "A":
        print(student)
        

""" We will use another set to compare and a while loop to validate our data. """

truth_gate = False

honors_value = { "A" : True, 
    "B" : False,
    "C" : False,
    "D" : False, 
    "F" : False}

""" Lets say we want to add some more verbosity to this problem. We want to add a validity check to make sure the values line up. The values in the basic for loop above are hardcoded and it would be better to get them more dynamically. 
If we turn the truth_gate to True, we will compare values based on the existing list and the honors_value list."""

truth_gate = True
while truth_gate == True:
    for student in students:
        if student["Honors"] != honors_value.get(student["Grade"]):
            print(f"Incorrect values for {student['Name']}")
    truth_gate = False
    
print(truth_gate)           
            
""" Because we have no idea how large this list might be, we can use the while flag to go through the entire length of the list and ensure each student is validated correctly. 
We put the truth gate outside of the for loop so it is triggered correctly. """

""" QUESTION 2 """

""" If both items of the list are the same length, we can simply use a zip function to create a zip object and then loop through that appending the non zero values to a list. 
In this case the lists are also both identical in output as well. """
            
input_list1 = [ 1, 0, 3, 0, 5, 0, 7, 0, 9]

input_list2 = [ 0, 2, 0, 4, 0, 6, 0, 8, 0]

t = zip(input_list1, input_list2)

mixed_list = []

for each in list(t):
    for y in each:
        if y == 0:
            continue
        else:
            mixed_list.append(y)
            
# print(mixed_list)

""" If both items are not of equal length, we instead can use index slicing to cut the index values from each into their own respective list """

# print(input_list1[::2])

new_list = []
for x in input_list2:
    if x%2 == 0:
        new_list.append(x)
# print(new_list)
    
    
""" QUESTION 3 """

list1 = [ 1, 0, 3, 0, 5, 0, 7, 0, 9]

list2 = [ 0, 2, 0, 4, 0, 6, 0, 8, 0,]

def mix_list(list1, list2):
    mixed_list = []
    # check if the same length to run a zip function 
    if len(list1) != len(list2):
            t = zip(list1, list2)
            for each in list(t):
                for y in each:
                    if y == 0:
                        continue
                    else:
                        mixed_list.append(y)

    else:               
        for index1, item1 in enumerate(list1):
            # slide the odds 
            if index1%2 !=  1 :
                mixed_list.append(item1)
        
        # for index2, item2 in enumerate(list2):
        #     if index2%2 == 1:
        #      mixed_list.append(item2)
             
    # now we have to sort the list, we know the lowest value is zero in this case
    # how many items there are     
    # n = len(mixed_list)
    # lowest = mixed_list[0]
    # index = 0
    # order_list = []
    
    # while len(mixed_list) > 0: 
    #     for val in range(n):
    #         if val < lowest:
    #             lowest = mixed_list[val]
    #         index += 1
    #         if index == len(mixed_list):
    #             order_list.append(lowest)
    #             mixed_list.pop(lowest)
    #         if mixed_list:
    #             lowest = mixed_list[0]
    #         val = 0


    return (mixed_list)

print( mix_list(list1, list2))


def greeting(value):
    # value check to make sure it is correct 
    value = int(value)
    
    time_range = [{"Good Morning" : {  600, 1159 } }, 
                    {"Good Afternoon" : {  1200, 559 } },
                    {"Good Evening"   : { 600, 2100 } }
    ]
    for time_frame in time_range:  
        if  value in list(time_frame.values()):
            print(value.keys())
        
