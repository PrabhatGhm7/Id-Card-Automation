import qrcode as qr
import openpyxl as xl
import sys

#calling workbook
wb = xl.load_workbook("students.xlsx")
sheet = wb["Sheet1"]

#handeling for 0 input
# try:
#     scount = int(input("Enter the number of students: "))
#     if scount == 0:
#         raise ValueError("Please enter a correct number of students")
# except ValueError as err:
#     print("Error:", err)
#     sys.exit()
scount =10

def makeqr():
    i = 2
    global scount

    while i != scount + 2:
        
        #parents information
        name = sheet["F" + str(i)]
        parent = f"Parent's Name: {name.value}"
        home = sheet["G" + str(i)]
        address = f"Address: {home.value}"
        phone = sheet["H" + str(i)]
        phone = f"Phone: {phone.value}"
        info = parent + "\n" + address + "\n" + phone

        # QR code making
        img = qr.make(info)
        img.thumbnail((180,180))
        filename = "qrcode" + str(i-1)
        img.save(f"C:\\Users\\Lenovo\\OneDrive\\Desktop\\Projects\\Id-card\\Processing Photo\\Qrcode\\{filename}.jpg")
        
        if(i== i%2):
            print("Making QR...")

        
        #increment
        i=i+1
        
        

