from PIL import Image, ImageDraw, ImageFont

# Criando uma nova imagem com fundo branco
width, height = 400, 200
image = Image.new("RGB", (width, height), "white")
draw = ImageDraw.Draw(image)

# Desenhando um retângulo
draw.rectangle([50, 50, 350, 150], outline="black", width=4)

# Adicionando texto
font = ImageFont.truetype("arial.ttf", 36)
text = "Logo"
text_width, text_height = draw.textsize(text, font=font)
text_position = ((width - text_width) // 2, (height - text_height) // 2)
draw.text(text_position, text, fill="black", font=font)

# Salvando a imagem
image.save("logo.png")

# Exibindo a imagem
image.show()
