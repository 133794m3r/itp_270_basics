#deer = 10
#hunters = 20
#grass = 5
deer=int(input("Enter how many deer there are: "))
hunters = int(input("Enter how many hunters there are: "))
grass = int(input("Enter how much grass there is: "))
if deer > hunters:
	print("The hunters should all be able to have a deer this year and leave some for the next year.")
elif hunters > deer:
	print("There are too many hunters someone's going home empty handed.")
else:
	print("Everyone should be able to bring home a deer.")
	
if deer > grass:
	print("There's not enough grass for the deer! They'll go hungry.")
elif grass > deer:
	print("This year the forests will be over grown.")
else:
	print("The fields should be manageble to walk through.")

