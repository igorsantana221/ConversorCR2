from PIL import Image
import os


#Converter arquivo CR2 em PNG

for file in os.listdir():
    if file.split('.')[-1] in ('jpg', 'jpeg', 'png', 'CR2'):
        print (file)   
        file_name = os.path.basename(file).split('.')[-2]
        imagem = Image.open(file)
        imagem_convertida = imagem.convert('RGB')
        imagem_convertida.save(f'{file_name}.png')




