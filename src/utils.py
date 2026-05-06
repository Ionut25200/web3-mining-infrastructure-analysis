"""
utils.py : Fonctions utilitaires pour le projet GoMining Infrastructure.
"""

def format_currency(value: float, currency: str = "GOMINING") -> str:
    """Formate une valeur numérique en devise avec 2 décimales."""
    return f"{value:>12.2f} {currency}"

def print_header(title: str, width: int = 42):
    """Affiche un en-tête stylisé pour les rapports."""
    print("\n" + "=" * width)
    print(f"{title:^{width}}")
    print("=" * width)

def print_footer(width: int = 42):
    """Affiche un pied de page stylisé."""
    print("=" * width + "\n")
