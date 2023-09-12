from PIL import Image , ImageDraw , ImageFont , ImageColor
import PIL

def qrincard():
    im = Image.open("C:\\Users\\Lenovo\\OneDrive\\Desktop\\Projects\\Id-card\\Template.jpg")

    code = 1
    while code != 11:
        name = f"qrcode{code}"
        im2 = Image.open(f"C:\\Users\\Lenovo\\OneDrive\\Desktop\\Projects\\Id-card\\Processing Photo\\Qrcode\\{name}.jpg")
        # Create a copy of the base template to paste the QR code onto
        im3 = im.copy()
        # Paste the QR code image onto the copied template at the specified position (204, 820)
        im3.paste(im2, (204, 820))
        #saving the image
        name2 = f"Card{code}"
        im3 = im3.save(f"C:\\Users\\Lenovo\\OneDrive\\Desktop\\Projects\\Id-card\\Processing Photo\\Card QR\\{name2}.jpg")
        
        if(code== code%2):
            print("Adding QR in card...")

        
        code= code + 1
        



    






