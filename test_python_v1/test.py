#TODO: 
#      CLeanup van de code en comments plaatsen voor vervolg
#      
#      
from inference_sdk import InferenceHTTPClient
import csv
gebruikte_afbeelding = "C:/Users/Wim/OneDrive/Communication and Multimedia Design/IWP Project 2024-2025/test_images/people-6545894_1920.jpg"

CLIENT = InferenceHTTPClient(
    api_url="https://detect.roboflow.com",
    api_key="f6TNF6A6YL6zZBAnXKrA"
)

result = CLIENT.infer(gebruikte_afbeelding, model_id="people-detection-general/7")
vraag_type = str("eens/oneens")
#----------------------Verwerken van de resultaten------------------------------
breedte_afbeelding = result.image.width
hoogte_afbeelding = result.image.height
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




print (result)
print( '\n' + "---------------------Formatted results----------------" + '\n')



