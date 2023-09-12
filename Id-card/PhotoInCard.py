from PIL import Image

def photoincard():
    i=1
    while (i!=11):    
        name1= f"Card{i}"
        name2 = f"Class7 ({i})"
        
        # Open the background image
        im = Image.open(f"C:\\Users\\Lenovo\\OneDrive\\Desktop\\Projects\\Id-card\\Processing Photo\\Card Text\\{name1}.jpg")

        # Open the photo image
        im2 = Image.open(f"C:\\Users\\Lenovo\\OneDrive\\Desktop\\Projects\\Id-card\\Processing Photo\\Photo 7\\{name2}.jpg")

        # Setting the points for cropped image with a slight increase to both left and right
        left = 40   # Adjust this value to increase cropping to the left
        top = 10
        right = 1060  # Adjust this value to increase cropping to the right
        bottom = 1200

        # Crop the photo image
        im3 = im2.crop((left, top, right, bottom))

        # Resize the cropped photo image to (400, 200)
        im3.thumbnail((421, 205))

        # Paste the cropped and resized photo onto the background image
        im.paste(im3, (207, 207))

        # Saving the resulting image
        im.save(f"C:\\Users\\Lenovo\\OneDrive\\Desktop\\Projects\\Id-card\\Final Card\\Final Card {i}.jpg")
        
        if(i== i%2):
            print("Adding Photos in card...")
            
        i=i+1
        
        

