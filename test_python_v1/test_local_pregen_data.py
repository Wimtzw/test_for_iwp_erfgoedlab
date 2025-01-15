import csv
vraag_type = str("eens/oneens")
result = {
    'inference_id': '34481634-3c9e-4505-985d-4362a6c84dc6',
    'time': 0.17981237000094552,
    'image': {
        'width': 1920,
        'height': 1280
    },
    'predictions': [{
        'x': 1556.0,
        'y': 990.0,
        'width': 132.0,
        'height': 298.0,
        'confidence': 0.8895930051803589,
        'class': 'person',
        'class_id': 0,
        'detection_id': '492bbae0-8c34-4406-b6fa-ef4c861f31f0'
    }, {
        'x': 1091.0,
        'y': 392.5,
        'width': 126.0,
        'height': 293.0,
        'confidence': 0.8557357788085938,
        'class': 'person',
        'class_id': 0,
        'detection_id': 'cb0b0bc2-d488-45e0-acf0-ee80022d838e'
    }, {
        'x': 1568.0,
        'y': 323.5,
        'width': 138.0,
        'height': 303.0,
        'confidence': 0.8412771821022034,
        'class': 'person',
        'class_id': 0,
        'detection_id': 'b2efdf87-0837-40fb-8552-113e868276ea'
    }, {
        'x': 963.5,
        'y': 396.0,
        'width': 143.0,
        'height': 262.0,
        'confidence': 0.8255714178085327,
        'class': 'person',
        'class_id': 0,
        'detection_id': '32688cf4-c619-44b8-a372-9a42d0543d83'
    }, {
        'x': 521.0,
        'y': 880.0,
        'width': 152.0,
        'height': 292.0,
        'confidence': 0.8153543472290039,
        'class': 'person',
        'class_id': 0,
        'detection_id': 'df9c87e7-36d5-4f6f-8071-9ea7067e04d9'
    }, {
        'x': 651.5,
        'y': 888.0,
        'width': 153.0,
        'height': 308.0,
        'confidence': 0.805401623249054,
        'class': 'person',
        'class_id': 0,
        'detection_id': '09d168e5-06d3-457b-b084-48a4a9abe6f2'
    }, {
        'x': 580.5,
        'y': 1145.5,
        'width': 185.0,
        'height': 267.0,
        'confidence': 0.737318754196167,
        'class': 'person',
        'class_id': 0,
        'detection_id': 'c9bf2ba7-bad3-4e98-a428-18556817eb4c'
    }, {
        'x': 1139.5,
        'y': 793.0,
        'width': 167.0,
        'height': 308.0,
        'confidence': 0.7250109910964966,
        'class': 'person',
        'class_id': 0,
        'detection_id': '0d3e0fd8-614e-4df2-9cff-c229aee3a1c8'
    }, {
        'x': 1838.0,
        'y': 967.5,
        'width': 164.0,
        'height': 321.0,
        'confidence': 0.7116686105728149,
        'class': 'person',
        'class_id': 0,
        'detection_id': 'b76e658d-05cc-4a5c-92e3-64f4096b7bc5'
    }, {
        'x': 355.5,
        'y': 229.5,
        'width': 179.0,
        'height': 293.0,
        'confidence': 0.59388267993927,
        'class': 'person',
        'class_id': 0,
        'detection_id': '7c12cf6e-5510-4cec-854b-45fc9c4f6db9'
    }, {
        'x': 861.0,
        'y': 432.0,
        'width': 124.0,
        'height': 180.0,
        'confidence': 0.5002357959747314,
        'class': 'person',
        'class_id': 0,
        'detection_id': 'f74bd4a6-7564-4ac2-bb04-bdfb6346d755'
    }]
}
print("----------------Printing Everything------------------")
for key, value in result.items():
    print(f"{key}: {value}")

print("\n------------Printing only the detections-------------\n")
printable_predictions = result.get("predictions")
print("The class of the below object is",type(printable_predictions))
print(printable_predictions)
print("\n------------Printing out only one item-------------\n")
print("The class of the below object is",type(printable_predictions[1]))
for key, value in zip(printable_predictions[1].keys(), printable_predictions[1].values()):
	print(f"{key}: {value}")
print("\n------------Only listing the X and Y of that item -------------\n")
keys_to_extract = ['x', 'y']
printable_predictions_x_y = dict(filter(lambda item: item[0] in keys_to_extract, printable_predictions[1].items()))
print("The class of the below object is",type(printable_predictions_x_y))
print(printable_predictions_x_y)
print("\n------------Now to list the X and Y of all items -------------\n")
xy_data = list()
for item_in_list in range(len(printable_predictions)):
	xy_data.append(dict(filter(lambda item: item[0] in keys_to_extract, printable_predictions[item_in_list].items())))
	print(xy_data)
print("The class of the above object is",type(xy_data))
print("\n------------Yes, print should be moved 1 block down. Next,  normalize -------------\n")
print(xy_data[1])
print("This gives back a range between 0 and 100 to where this person was standing. X =",0.052083 * xy_data[1].get("x"))
print("\n------------Normalize now works... todo next time: build loop for X and Y, send it to joost for processing -------------\n")
outfile = open('test_sample_data.csv', 'w')
fields = ['ID', 'X', 'Y', 'Type_vraag']
write = csv.writer(outfile)
write.writerow(fields)
rows = list()
for item_in_xy_data in range(len(xy_data)):
	xy_temp_data_x =(0.052083 * xy_data[item_in_xy_data].get("x")
    )
	xy_temp_data_y =(0.078125 * xy_data[item_in_xy_data].get("y")
    )
	xy_temp_data_number = item_in_xy_data
	xy_temp_data_xy ={
		"Naam" : "Persoon " + str(item_in_xy_data),
		"X": xy_temp_data_x,
		"Y": xy_temp_data_y,
		"Type_vraag": vraag_type
    }
	rows += [item_in_xy_data, xy_temp_data_x, xy_temp_data_y, vraag_type]
	print('\n Value of xy_temp_data_xy is')
	print(xy_temp_data_xy)
	print('\n')
	write.writerow(xy_temp_data_xy)
    #Gives jumbled output 
	#write.writerow({item_in_xy_data, xy_temp_data_x, xy_temp_data_y, vraag_type})
	
print('\n printing the list variant of data \n')
print(rows)
print(type(rows))
print('\n ----------printing the dict version of data---------------')
print(xy_temp_data_xy)
print(type(xy_temp_data_xy))
#write.writerow(xy_temp_data_xy)    


#Writing the ouput in here goes mostly ok, but puts everything into a single field
# outfile = open('test.csv', 'w')
# fields = ['ID', 'X', 'Y', 'Type_vraag']
# write = csv.writer(outfile)
#write.writerow(rows)