from PIL import Image , ImageDraw , ImageFont , ImageColor
import PIL
import openpyxl as xl
from openpyxl import load_workbook


def add_text():
    i=2
    j=1
    while i != 12:
        #import from xlsx
        wb = load_workbook(filename = 'students.xlsx')
        sheet = wb['Sheet1']    
        name = str((sheet["B" + str(i)]).value)
        cls = str((sheet["C" + str(i)]).value)
        rollno = str((sheet["D" + str(i)]).value)
        valid = str((sheet["I" + str(i)]).value)
        
        
        textimg = Image.open(f"C:\\Users\\Lenovo\\OneDrive\\Desktop\\Projects\\Id-card\\Processing Photo\\Card QR\\Card{j}.jpg")
        draw = ImageDraw.Draw(textimg)
        
        
        nameFont= ImageFont.truetype ("C:\\Users\\Lenovo\\OneDrive\\Desktop\\Projects\\Id-card\\times.ttf",54)
        otherFont = ImageFont.truetype ("C:\\Users\\Lenovo\\OneDrive\\Desktop\\Projects\\Id-card\\Roboto-Regular.ttf",24)
       
        # Add Text to an image
        draw.text((88,530), name, font=nameFont, fill =(0,0,0))
        draw.text((218,686), cls, font=otherFont, fill =(0,0,0))
        draw.text((218,734), rollno, font=otherFont, fill =(0,0,0))
        draw.text((218,779), valid, font=otherFont, fill =(0,0,0))
        
        #saving
        name2 = f"Card{j}"
        textimg.save(f"C:\\Users\\Lenovo\\OneDrive\\Desktop\\Projects\\Id-card\\Processing Photo\\Card Text\\{name2}.jpg")
        
        if(i== i%2):
            print("Adding text in card...")

        
        i = i + 1
        j= j + 1
    


        
        

        




