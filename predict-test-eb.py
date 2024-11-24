import requests


url = 'http://app-env.eba-yprhmskx.us-east-1.elasticbeanstalk.com/predict'

water_sample_id = 'water-230'

water_sample = {
    "ph": 5.821262,
    "hardness": 204.048890,
    "solids": 37174.005414,
    "chloramines": 7.867815,
    "sulfate": 329.019554,
    "conductivity": 466.783264,
    "organic_carbon": 13.988707,
    "trihalomethanes": 96.826961,
    "turbidity": 4.371079
}

response = requests.post(url, json=water_sample).json()
print(response)

if response['potability'] == True:
    print(f'Water sample id {water_sample_id} is potable water')
else:
    print(f'Water sample id {water_sample_id} is Non-potable water')