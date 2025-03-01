COLOR_TO_HEX = {"aqua": "#00ffff", "amber": "#ffbf00", "amethyst": "#9966cc", "amaranth": "#e52b50", "apricot": "#fbceb1",
                "beige": "#f5f5dc", "blond": "#faf0be", "buff": "#f0dc82", "camel": "#c19a6b", "carmine": "#960018" }

print(COLOR_TO_HEX)

color_name = input("Enter a color: ").lower()
while color_name != "":
    print(color_name, "has hex -", COLOR_TO_HEX.get(color_name, "Invalid color"))

    color_name = input("Enter a color name: ").lower()