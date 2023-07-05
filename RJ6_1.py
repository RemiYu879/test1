import json

with open('kabeposter//kabeposter_000000000000_keypoints.json') as f:
    js=json.load(f)
    
    for j in range(6):
        print(js['people'][0]['pose_keypoints_2d'][j])

    for j in range(6):
        print(js['people'][1]['pose_keypoints_2d'][j])


