from PIL import Image, ImageDraw, ImageFont

size = 256
img = Image.new("RGBA", (size, size), (0, 0, 0, 255))
d = ImageDraw.Draw(img)

# зелёное кольцо
d.ellipse((16, 16, size - 16, size - 16),
          outline=(0, 255, 65, 255), width=14)

# символ >_
try:
    font = ImageFont.truetype("consola.ttf", 130)
except Exception:
    font = ImageFont.load_default()

text = ">_"
bbox = d.textbbox((0, 0), text, font=font)
w, h = bbox[2] - bbox[0], bbox[3] - bbox[1]
d.text(((size - w) / 2 - bbox[0],
        (size - h) / 2 - bbox[1] - 10),
       text, fill=(0, 255, 65, 255), font=font)

# сохраняем .ico во всех нужных размерах
img.save("icon.ico",
         sizes=[(16, 16), (32, 32), (48, 48),
                (64, 64), (128, 128), (256, 256)])
print("icon.ico создан!")