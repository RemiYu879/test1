import tkinter as tk
import json


with open('kabeposter//kabeposter_000000000000_keypoints.json') as f:
    
    js=json.load(f)
   

    root=tk.Tk()
    root.geometry("1500x1500")
    canvas=tk.Canvas(root, bg="white")
    canvas.pack(fill=tk.BOTH, expand=True)
    
    
    canvas.create_line(js['people'][0]['pose_keypoints_2d'][6],js['people'][0]['pose_keypoints_2d'][7],js['people'][0]['pose_keypoints_2d'][3],js['people'][0]['pose_keypoints_2d'][4],width=3)
    canvas.create_line(js['people'][0]['pose_keypoints_2d'][3],js['people'][0]['pose_keypoints_2d'][4],js['people'][0]['pose_keypoints_2d'][15],js['people'][0]['pose_keypoints_2d'][16])

    canvas.create_line(js['people'][1]['pose_keypoints_2d'][6],js['people'][1]['pose_keypoints_2d'][7],js['people'][1]['pose_keypoints_2d'][3],js['people'][1]['pose_keypoints_2d'][4],width=3)
    canvas.create_line(js['people'][1]['pose_keypoints_2d'][3],js['people'][1]['pose_keypoints_2d'][4],js['people'][1]['pose_keypoints_2d'][15],js['people'][1]['pose_keypoints_2d'][16])
    root.mainloop()

