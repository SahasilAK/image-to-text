import tkinter as tk
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfile
import pytesseract

#tesseract.exe location
pytesseract.pytesseract.tesseract_cmd = r'C:\OCR\Tesseract.exe'

window = tk.Tk()
window.title('Image to Text')

def open_file():
    browse_text.set('Loading...')
    file = askopenfile(parent=window, mode='rb', title='choose a file', filetype=[('jpg file','*.jpg'),('png file','*.png')])

    if file:
        text = pytesseract.image_to_string(Image.open(file))
        with open('data.txt', 'w') as data_file:
            data_file.write(text)

        text_box = tk.Text(window, height=10, width=50, padx=15, pady=15)
        text_box.insert(1.0,text)
        text_box.tag_configure("center")
        text_box.tag_add('center', 1.0, 'end')
        text_box.grid(column=1,row=3)
        browse_text.set('Browse')

canvas = tk.Canvas(window, width=600, height=300)
canvas.grid(columnspan=3,rowspan=3)

logo = Image.open('logo/logo.png')
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.image = logo
logo_label.grid(column=1,row=0)

dis_info = tk.Label(window, text='Select a PDF file to convert to text', font='Raleway')
dis_info.grid(columnspan=3, column=0, row=1)

browse_text = tk.StringVar()
browse_btn = tk.Button(window, textvariable=browse_text, command=lambda:open_file(), font="Raleway", bg='#20bebe', fg='white', height=2, width=15)
browse_text.set("Browse")
browse_btn.grid(column=1, row=2)

canvas = tk.Canvas(window, width=600,height=250)
canvas.grid(columnspan=3)
window.mainloop()
