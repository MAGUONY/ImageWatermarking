from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageDraw, ImageFont


def quitProgram():
    quit()


def browseFile():
    filename = filedialog.askopenfilename(initialdir="/Pictures", title="Select a File",
                                          filetypes=(("Image files", "*.jpg*"),))
    applyWatermark(filename)


def applyWatermark(image):

    def watermarkingDone():
        # Create an Image Object from an Image
        theImage = Image.open(image)
        width, height = theImage.size

        draw = ImageDraw.Draw(theImage)
        text = str(textEntry.get())

        # fontSizeEntry.get()
        font = ImageFont.truetype('arial.ttf', int(fontSizeEntry.get()))
        textWidth, textHeight = draw.textsize(text, font)

        # Calculate the x,y coordinates of the text
        margin = 10
        x = width - textWidth - margin
        y = height - textHeight - margin

        # Draw watermark in the bottom right corner
        draw.text((x, y), text=text, font=font, fill="#FF0000")
        # str(colorEntry.get()))
        theImage.show()

        # Save watermarked image
        theImage.save(f"Images/{str(nameEntry.get())}.jpg")
        editWindow.destroy()

    editWindow = Tk()
    editWindow.title("Watermark")

    textLabel = Label(editWindow, text="Text of the watermark: ")
    textLabel.grid(column=0, row=0)

    textEntry = Entry(editWindow)
    textEntry.grid(column=1, row=0, pady=5)

    fontSizeLabel = Label(editWindow, text="Size of the font: ")
    fontSizeLabel.grid(column=0, row=1)

    fontSizeEntry = Entry(editWindow)
    fontSizeEntry.grid(column=1, row=1, pady=5)

    nameLabel = Label(editWindow, text="Name of the watermarked image: ")
    nameLabel.grid(column=0, row=3)

    nameEntry = Entry(editWindow)
    nameEntry.grid(column=1, row=3, pady=5)

    applyButton = Button(editWindow, text="Apply watermark", command=watermarkingDone, width=20, height=3, bg="green")
    applyButton.grid(column=0, row=4)

    editWindow.mainloop()


FONT_NAME = "Times New Roman"
GREY = "#4c4c4c"

theWindow = Tk()
theWindow.title("Image Watermarking")
theWindow.minsize(600, 400)
theWindow.config(bg=GREY)

welcomeLabel = Label(text="Welcome to the Image Watermarking Application!", font=(FONT_NAME, 22, "bold"), bg=GREY)
welcomeLabel.grid(column=0, row=0)

buttonLabel = Label(text="Select image to apply watermark", font=(FONT_NAME, 18), bg=GREY)
buttonLabel.grid(column=0, row=1, pady=60)

uploadImage = PhotoImage(file="Images/upload-photo.png")
selectButton = Button(text="Select your picture", image=uploadImage, command=browseFile)
selectButton.grid(column=0, row=2)

exitButton = Button(text="Exit", command=quitProgram, width=20, height=3, bg="red")
exitButton.grid(column=0, row=3, pady=30)

theWindow.mainloop()
