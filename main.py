from PIL import Image

# Définir les caractères à utiliser pour chaque niveau de noirceur
CARACTERES = "your letter from lightest to darkest"

def pixel_en_caractere(pixel):
    # Convertir la valeur du pixel en caractère
    return CARACTERES[pixel * len(CARACTERES) // 256]

def image_en_texte(chemin_image):
    # Ouvrir l'image et la convertir en niveaux de gris
    image = Image.open(chemin_image).convert("L")

    # Convertir chaque pixel en caractère
    texte = ""
    for y in range(image.height):
        for x in range(image.width):
            texte += pixel_en_caractere(image.getpixel((x, y)))
        texte += "\n"

    return texte

# Convertir l'image en texte
text = image_en_texte(r"your image")

# Afficher le texte
print(texte)
