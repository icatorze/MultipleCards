import csv
from PIL import Image, ImageDraw, ImageFont

contas = []

with open('./contacts.csv', 'rb') as csvfile:
    contatos = csv.reader(csvfile, delimiter=',', quotechar='|')

    for c in contatos:
        contas.append(c)

font = ImageFont.truetype('Arial.ttf', size=20)

color = 'rgb(255,255,255)'
(x, y) = (220, 150)

for l in contas:
    image = Image.open('./puppy.png')
    draw = ImageDraw.Draw(image)
    d = 0
    for i in l:
        draw.text((x,y+d), i, fill=color, font=font)
        d+=20
    filename = './signaturecard-{}.png'.format(l[0])
    image.save(filename)

