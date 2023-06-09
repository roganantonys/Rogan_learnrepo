import json

#to read the json file
with open('D:\skillrack1\Rogan_learnrepo\json_modify\ex5.json', 'r') as f:
    ex5=json.load(f)


#adding the data to the json file
ex5.append(
    {
        "id":"0004",
        "type":"coffee",
        "name":"Old Fashioned",
        "ppu":0.55,
        "batters":
			{
				"batter":
					[
						{ "id": "1001", "type": "Regular" },
						{ "id": "1002", "type": "Chocolate" }
					]
			},
		"topping":
			[
				{ "id": "5001", "type": "None" },
				{ "id": "5002", "type": "sugar" },
				{ "id": "5003", "type": "ice cubes" },
				{ "id": "5004", "type": "cream" }
            ]
    }


)

#write the changes in the json file
with open("D:\skillrack1\Rogan_learnrepo\json_modify\ex5.json","w") as f:
    json.dump(ex5,f,indent=4)

    f.close

#to print the content
with open("D:\skillrack1\Rogan_learnrepo\json_modify\ex5.json", "r") as f:
    ex5=json.load(f)

print(ex5)