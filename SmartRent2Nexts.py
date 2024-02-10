from src.app.menu import show_menu_principal

# Condição para não executar como script
# quando ser importado por outro script.
# - Executará quando script: `python SmartRent2Nexts.py`
# - Não executará como biblioteca: `import SmartRent2Nexts`
if(__name__ == '__main__'):
    show_menu_principal()