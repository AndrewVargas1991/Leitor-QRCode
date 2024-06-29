# pip install pillow
# pip install pyzbar

from PIL import Image
from pyzbar.pyzbar import decode
from tkinter import filedialog

arquivo = filedialog.askopenfilename()
conteudo = decode(Image.open(arquivo))

# print(conteudo) # Caso você queira imprimir a lista do conteúdo
print(f'Conteúdo do QRCode: {conteudo[0].data.decode('utf-8')}')

input('\nAperte ENTER para sair...')