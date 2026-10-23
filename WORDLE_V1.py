# WORDLE BECAUSE WHY NOT :O
#Version 1.2
import tkinter as tk
import random
import time

Words=["apple","bread","world","house","light","water","heart","plant","music","smile",
"grass","table","chair","sweet","fruit","dream","cloud","beach","flame","brick",
"stone","river","storm","field","earth","honey","peace","dance","ghost","sugar",
"wrist","flour","brown","black","white","green","silly","happy","quiet","magic",
"grape","piano","queen","tiger","zebra","mouse","camel","eagle","snail","lemon",
"mango","pearl","candy","toast","grill","shirt","pants","socks","boots","flute",
"drums","knife","spoon","plate","couch","clock","bloom","shine","globe",
"charm","crown","angel","flock","trick","slide","trace","paint","sweep",
"crane","blend","spark","frost","vivid","grind","flair","coast","bliss","roast",
"shade","crisp","wring","plush","drink","flint","bacon","sauce","bread","spear",
"flask","laser","cable","power","motor","chain","metal","screw","drill","wires",
"input","error","value","logic","pixel","image","frame","sound","video","flash",
"model","track","score","skill","level","round","match","train","block","build",
"miner","sword","armor","magic","witch","angel","devil","light","flame","storm",
"shiny","fluff","puffy","brave","sharp","solid","quick","smart","funny","crazy",
"pride","honor","truth","faith","grace","lucky","quiet","sweet","fresh","spice",
"robin","horse","sheep","goose","eagle","crowd","whale","shark","turtle","otter",
"snake","gecko","crab","spoon","chili","pizza","pasta","berry","cream","sugar",
"flour","yeast","baker","butter","onion","garlic","salad","meaty","fries","chips",
"smoke","steam","bloom","petal","leafy","cacti","shrub","roots","vines","grass",
"rocks","cliff","ocean","beach","shore","coral","waves","tides","storm","winds",
"smile","laugh","dream","sweep","build","fight","dance","drink","speak","think",
"write","learn","teach","stand","plant","paint","shine","climb","throw","catch",
"bloom","sleep","watch","swim","bake","shake","serve","carry","press","count",
"shout","clean","drift","crawl","crash","blend","spark","move","growl","chase",
"flame","slide","glide","crank","grasp","punch","grind","drain","blast","shock",
"happy","quiet","brave","sweet","sharp","solid","silly","funny","angry","tired",
"crazy","proud","fresh","lucky","smart","bliss","clean","fluff","moody","quick",
"heavy","light","storm","frost","sunny","witty","flaky","greed","noisy","cozyy",
"vivid","ready","early","chill","fuzzy","leafy","dream","swift","tight","loose",
"mildy","dusty","rocky","windy","spicy","salty","juicy","sweet","weird","kindy"]
b=0
b2=0
p="     "
end=0
def reset():
    global end,Words,w,l,t,line,a
    w=Words[random.randint(0,len(Words)-1)]
    l=["","","","",""]
    t=["","","","",""]

    line=1
    a=""

reset()
#this line is 6 or 7 long
window = tk.Tk()
window.title("BLEH")
window.geometry(str(410) + "x" + str(390))
canvas = tk.Canvas(window, width=(410), height=(390), bg="white")
canvas.pack()

def render():
    global cube,l,t,end,w
    if end==0:
        x = 20
        y = 320
        weg = 0
        weg2 = 4
        canvas.delete("all")
        # RENDER BLOCKS
        for i in range(5):
            for i in range(5):
                if l[weg2]=="":
                    cube = canvas.create_rectangle(x, y, x + 60, y - 60, fill="white")
                elif l[weg2][weg]=="0":
                    cube = canvas.create_rectangle(x, y, x + 60, y - 60, fill="white")
                elif l[weg2][weg]=="1":
                    cube = canvas.create_rectangle(x, y, x + 60, y - 60, fill="yellow")
                elif l[weg2][weg]=="2":
                    cube = canvas.create_rectangle(x, y, x + 60, y - 60, fill="green")
                if t[weg2]!="":
                    canvas.create_text(x+30, y-30, text=(t[weg2][weg]), fill="black", font=("Arial", 30))
                weg += 1
                x = x + 60
            weg=0
            x = 20
            y = y - 60
            weg2 -=1
        for i in range(5):
            cube = canvas.create_rectangle(20+(i*60),320,80+(i*60),380, fill="white")
        canvas.create_line(20, 320, 320, 320, fill="black", width=5)
    elif end== 1:
        for i in range(5):
            cube = canvas.create_rectangle(20+(i*60),320,80+(i*60),380, fill="green")
            canvas.create_text(50+(i*60),350, text=(w[i]), fill="black", font=("Arial", 30))
        canvas.create_line(20, 320, 320, 320, fill="black", width=5)
    elif end==2:
        for i in range(5):
            cube = canvas.create_rectangle(20+(i*60),320,80+(i*60),380, fill="red")
            canvas.create_text(50+(i*60),350, text=(w[i]), fill="black", font=("Arial", 30))
        canvas.create_line(20, 320, 320, 320, fill="black", width=5)

    cube = canvas.create_rectangle(340,20,400,80, fill="white")
    canvas.create_text(370,50, text=("NÄCHSTES"), fill="black", font=("Arial", 8))
    cube = canvas.create_rectangle(340,100,400,160, fill="red")
    canvas.create_text(370,130, text=("LÖSEN"), fill="black", font=("Arial", 10))
    cube = canvas.create_rectangle(340,180,400,240, fill="lightblue")
    canvas.create_text(370,210, text=("Set Word"), fill="black", font=("Arial", 10))


def move(event):
    global a,b,line,l,t,end,p
    if end==0:
        if event.keysym== "BackSpace":
            a = a[:-1]
        elif event.keysym== "Return":
            EINGABE()
            a=""
            line+=1
            if line==6 and end==0:
                end=2
                render()
                return False
        elif len(event.keysym)==1:
            a=a+event.keysym
        t[line-1]=a
        t[line-1]=t[line-1].ljust(5, "_")
        render()
    elif end==-1 and b==0:
        if event.keysym== "BackSpace":
            a = a[:-1]
        elif event.keysym== "Return":
            p=a.ljust(5, "_")
            a=""
            b=1
            friend()
            return
        elif len(event.keysym)==1:
            a=a+event.keysym
        p=a.ljust(5, "_")
        friend()

window.bind("<Key>", move)

def EINGABE():
    #blub
    global w,l,t,end,p,line
    z=""
    for i in range(5):
        if  t[line-1][i].lower() ==w[i].lower():
            z=z+"2"
        elif t[line-1][i].lower() in w.lower():
            z=z+"1"
        else:
            z=z+"0"
    l[line-1]=z
    render()
    if z=="22222":
        end=1
    render()

def friend():
    global p,end,w,cube,b
    canvas.delete("all")
    if b==1:
        w=p
        end=0
        render()
    else:
        canvas.create_text(200,200, text=("WHAT WORD"), fill="black", font=("Arial", 30))
        for i in range(5):
            cube = canvas.create_rectangle(20+(i*60),320,80+(i*60),380, fill="white")
            canvas.create_text(50+(i*60),350, text=(p[i]), fill="black", font=("Arial", 30))



def mouse_pos(event):
    global mx, my
    mx, my = event.x, event.y
canvas.bind("<Motion>", mouse_pos)

def mouse_click(event):
    global mx,my,end,a,b2,b
    if end!=-1:
        if mx>=340 and mx<=400 and my>=20 and my<=80:
            reset()
            end=0
            render()
        elif mx>=340 and mx<=400 and my>=100 and my<=160:
            end=2
            render()
        elif mx>=340 and mx<=400 and my>=180 and my<=240:
            reset()
            b2=1
            b=0
            end=-1
            a=""
            friend()

canvas.bind("<Button-1>", mouse_click)

render()
window.mainloop()# Schreibe hier Deinen Code :-)
