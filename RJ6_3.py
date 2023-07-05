import tkinter as tk
import json
import time

root=tk.Tk()
root.geometry("1500x1500")
canvas=tk.Canvas(root, bg="white")
canvas.pack(fill=tk.BOTH, expand=True)

for i in range(99):
    with open('kabeposter//kabeposter_000000000{}_keypoints.json'.format(f'{i:03}')) as f:
    
        js=json.load(f)

        a=js['people'][0]['pose_keypoints_2d']
        b=js['people'][1]['pose_keypoints_2d']
    
        m1=[
            [a[0],a[1],a[3],a[4]],
            [a[3],a[4],a[6],a[7]],
            [a[6],a[7],a[9],a[10]],
            [a[9],a[10],a[12],a[13]],
            [a[3],a[4],a[15],a[16]],
            [a[15],a[16],a[18],a[19]],
            [a[18],a[19],a[21],a[22]],
            [a[3],a[4],a[24],a[25]],
            [a[24],a[25],a[27],a[28]],
            [a[27],a[28],a[30],a[31]],
            [a[30],a[31],a[33],a[34]],
            [a[33],a[34],a[72],a[73]],
            [a[33],a[34],a[66],a[67]],
            [a[66],a[67],a[69],a[70]],
            [a[24],a[25],a[36],a[37]],
            [a[36],a[37],a[39],a[40]],
            [a[39],a[40],a[42],a[43]],
            [a[42],a[43],a[63],a[64]],
            [a[42],a[43],a[57],a[58]],
            [a[57],a[58],a[60],a[61]],
            [a[0],a[1],a[45],a[46]],
            [a[0],a[1],a[48],a[49]],
            [a[45],a[46],a[51],a[52]],
            [a[48],a[49],a[54],a[55]]
        ]
        m2=[
            [b[0],b[1],b[3],b[4]],
            [b[3],b[4],b[6],b[7]],
            [b[6],b[7],b[9],b[10]],
            [b[9],b[10],b[12],b[13]],
            [b[3],b[4],b[15],b[16]],
            [b[15],b[16],b[18],b[19]],
            [b[18],b[19],b[21],b[22]],
            [b[3],b[4],b[24],b[25]],
            [b[24],b[25],b[27],b[28]],
            [b[27],b[28],b[30],b[31]],
            [b[30],b[31],b[33],b[34]],
            [b[33],b[34],b[72],b[73]],
            [b[33],b[34],b[66],b[67]],
            [b[66],b[67],b[69],b[70]],
            [b[24],b[25],b[36],b[37]],
            [b[36],b[37],b[39],b[40]],
            [b[39],b[40],b[42],b[43]],
            [b[42],b[43],b[63],b[64]],
            [b[42],b[43],b[57],b[58]],
            [b[57],b[58],b[60],b[61]],
            [b[0],b[1],b[45],b[46]],
            [b[0],b[1],b[48],b[49]],
            [b[45],b[46],b[51],b[52]],
            [b[48],b[49],b[54],b[55]]
        ]
        canvas.delete("all")
        
        z=len(m1)
        for x in range(z):
            if m1[x][0] != 0 and m1[x][1] != 0 and m1[x][2] != 0 and m1[x][3] != 0:
                canvas.create_line(m1[x][0],m1[x][1],m1[x][2],m1[x][3],width=3)
            if m2[x][0] != 0 and m2[x][1] != 0 and m2[x][2] != 0 and m2[x][3] != 0:
                canvas.create_line(m2[x][0],m2[x][1],m2[x][2],m2[x][3])

        root.update()
        time.sleep(1)
        

root.mainloop()
