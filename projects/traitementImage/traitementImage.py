from PIL import Image, ImageEnhance, ImageFilter

def color_filter(image):
    """
    Applique un filtre de couleur à une image en utilisant la bibliothèque PIL.
    :param image_path: Le chemin de l'image à modifier.
    :param color: La couleur du filtre (un tuple de valeurs RGB).
    :param opacity: L'opacité du filtre (une valeur flottante comprise entre 0 et 1).
    :return: L'image modifiée.
    """
    # Choix de la couleur
    
    choice_is_correct = False
    while not choice_is_correct:
        choice = input("Choissisez une couleur dans le format 'R/G/B'.\n   >>>")
        try:
            R, G, B = choice.split("/")
            if 0 <= R <= 255 and 0 <= G <= 255 and 0 <= B <= 255:
                color = (R, G, B)
                choice_is_correct = True
            else:
                print("Les valeurs doivent être comprises entre 0 et 255 inclus")
        except:
            print("Format incorrect, réessayez.")

    # Choix de l'opacité
    choice_is_correct = False
    while not choice_is_correct:
        choice = input("Choissisez l'opacité du filtre, la valeur doit être comprise en 0 et 1.\n   >>>")
        try:
            if 0 <= choice <= 1:
                opacity = choice
                choice_is_correct = True
            else:
                print("La valeur doit être comprise en 0 et 1.")
        except:
            print("Entrez un nombre flottant.")

    

    # Création d'une image vierge de la même taille que l'image d'origine
    colored_image = Image.new('RGBA', image.size, color=(0, 0, 0, 0))

    # Remplissage de l'image vierge avec la couleur du filtre et l'opacité désirée
    colored_image.paste(color, (0, 0, image.size[0], image.size[1]))
    colored_image = ImageEnhance.Brightness(colored_image).enhance(opacity)

    # Application du filtre de couleur à l'image originale
    image = Image.alpha_composite(image, colored_image)

    # Retour de l'image modifiée
    return image

def transpose_filter(image):
    """
    Renvoie une image renversée selon l'axe horizontal, vertical ou diagonal.
    :param image_path: Le chemin de l'image à renverser.
    :param mode: Le mode de renversement ('horizontal', 'vertical' ou 'diagonal').
    :return: L'image renversée.
    """
    # Choix du mode 
    choice_is_correct = False
    while not choice_is_correct:
        choice = input("Choissisez l'axe de transposition: 1: horizontal, 2: vertical et 3: diagonal.\n   >>>")
        if choice == "1":
            mode = 'horizontal'
        if choice == "2":
            mode = 'vertical'
        if choice == "3":
            mode = 'diagonal'
        else:
            print("Tapez 1, 2 ou 3")

    # Création d'une nouvelle image vide de la même taille que l'image d'origine
    flipped_image = Image.new('RGBA', image.size)

    # Traitement de l'image en fonction du mode de renversement demandé
    if mode == 'horizontal':
        flipped_image = image.transpose(method=Image.FLIP_LEFT_RIGHT)
    elif mode == 'vertical':
        flipped_image = image.transpose(method=Image.FLIP_TOP_BOTTOM)
    elif mode == 'diagonal':
        flipped_image = image.transpose(method=Image.TRANSPOSE)
    
    # Retour de l'image renversée
    return flipped_image

def blur_filter(image):
    """
    Applique un filtre de flou à une image en utilisant la bibliothèque PIL.
    :param image_path: Le chemin de l'image à modifier.
    :param radius: Le rayon du flou (une valeur entière).
    :return: L'image modifiée.
    """
    # Choix du rayon de flou 
    choice_is_correct = False
    while not choice_is_correct:
        choice = input("Choissisez le rayon de flou (entier positif).\n   >>>")
        try:
            if int(choice) > 0:
                radius = choice
                choice_is_correct = True
            else:
                print("L'entier doit être positif")
        except:
            print("Vous devez entrer un entier.")

    # Application du filtre de flou à l'image
    image_filtered = image.filter(ImageFilter.GaussianBlur(radius))

    # Retour de l'image modifiée
    return image_filtered

def sharpness_filter(image):
    """
    Applique un filtre de netteté à une image en utilisant la bibliothèque PIL.
    :param image_path: Le chemin de l'image à modifier.
    :param factor: Le facteur de netteté (une valeur flottante comprise entre 0 et 1).
    :return: L'image modifiée.
    """
    # Choix du facteur de netteté
    choice_is_correct = False
    while not choice_is_correct:
        choice = input("Choissisez le facteur de netteté, la valeur doit être comprise en 0 et 1.\n   >>>")
        try:
            if 0 <= choice <= 1:
                factor = choice
                choice_is_correct = True
            else:
                print("La valeur doit être comprise en 0 et 1.")
        except:
            print("Entrez un nombre flottant.")

    # Application du filtre de netteté à l'image
    image_filtered = image.filter(ImageFilter.UnsharpMask(radius=2, percent=150, threshold=3))

    # Ajustement du facteur de netteté
    enhancer = ImageEnhance.Sharpness(image_filtered)
    image_filtered = enhancer.enhance(factor)

    # Retour de l'image modifiée
    return image_filtered

def saturation_filter(image, factor):
    """
    Applique un filtre de saturation à une image en utilisant la bibliothèque PIL.
    :param image_path: Le chemin de l'image à modifier.
    :param factor: Le facteur de saturation (une valeur flottante comprise entre 0 et 1).
    :return: L'image modifiée.
    """

    # Choix du facteur de saturation
    choice_is_correct = False
    while not choice_is_correct:
        choice = input("Choissisez le facteur de saturation, la valeur doit être comprise en 0 et 1.\n   >>>")
        try:
            if 0 <= choice <= 1:
                factor = choice
                choice_is_correct = True
            else:
                print("La valeur doit être comprise en 0 et 1.")
        except:
            print("Entrez un nombre flottant.")

    # Ajustement de la saturation de l'image
    enhancer = ImageEnhance.Color(image)
    image_filtered = enhancer.enhance(factor)

    # Retour de l'image modifiée
    return image_filtered


def contrast_filter(image):
    """
    Applique un filtre de contraste à une image en utilisant la bibliothèque PIL.
    :param image_path: Le chemin de l'image à modifier.
    :param factor: Le facteur de contraste (une valeur flottante).
    :return: L'image modifiée.
    """
    # Choix facteur de contraste
    choice_is_correct = False
    while not choice_is_correct:
        choice = input("Choissisez le facteur de contraste (floattant positif).\n   >>>")
        try:
            if float(choice) > 0:
                factor = int(choice)
                choice_is_correct = True
            else:
                print("Le floattant doit être positif")
        except:
            print("Vous devez entrer un floattant.")

    # Création d'un objet ImageEnhance pour modifier le contraste
    contrast = ImageEnhance.Contrast(image)
    # Application de la modification de contraste en utilisant le facteur spécifié
    filtered_image = contrast.enhance(factor)
    return filtered_image

def apply_filter():
    print("Bienvenue dans l'éditeur d'images python.")

    while 1:
        # Choix de l'image
        print("Choisissez une image à modifier:\n",
              "   - 1: R2D2\n",
              "   - 2: Tigre\n",
              "   - 3: Paysage\n",
              "Pour quitter, tapez 'sortir'."
              )
        
        choice_is_correct = False
        while not choice_is_correct:
            choice = input("   >>>")
            if choice == "1":
                image = Image.open("R2D2.jpg")
                choice_is_correct = True
            elif choice == "2":
                image = Image.open("tigre2.jpg")
                choice_is_correct = True
            elif choice == "3":
                image = Image.open("paysage.jpg")
                choice_is_correct = True
            elif choice.lower() == "sortir":
                return
            else:
                print("Tapez 1, 2 ou 3.")

        # Choix du filtre
        print("Choisissez un filtre à appliquer:\n",
              "   - 1: Filtre de couleur\n",
              "   - 2: Filtre de transposition\n",
              "   - 3: filtre de flou\n",
              "   - 4: filtre de netteté\n",
              "   - 5: filtre de saturation\n",
              "   - 6: filtre de contraste\n",         
              )
        
        choice_is_correct = False
        while not choice_is_correct:
            choice = input("   >>>")
            if choice == "1":
                filtered_image = color_filter(image)
                choice_is_correct = True
            elif choice == "2":
                filtered_image = transpose_filter(image)
                choice_is_correct = True
            elif choice == "3":
                filtered_image = blur_filter(image)
                choice_is_correct = True
            elif choice == "4":
                filtered_image = sharpness_filter(image)
                choice_is_correct = True
            elif choice == "5":
                filtered_image = saturation_filter(image)
                choice_is_correct = True
            elif choice == "6":
                filtered_image = contrast_filter(image)
                choice_is_correct = True
            else:
                print("Tapez 1, 2, 3, 4, 5 ou 6.")

        image_name = input("Choissisez le nom de la nouvelle image.\n   >>>")
        filtered_image.save(f"{image_name}.jpg")
        print("L'image filtrée a bien été enregistrée sous le nom de:", image_name)

apply_filter()
