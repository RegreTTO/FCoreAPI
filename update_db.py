import colorama

from Bd_Scripts import parse_products, parse_recipes

colorama.init()

print(colorama.Fore.CYAN, "PRODUCTS", colorama.Fore.RESET)
parse_products.main()

print(colorama.Fore.CYAN, "RECIPES", colorama.Fore.RESET)
parse_recipes.main()
