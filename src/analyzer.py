import pandas as pd
import os
import logging
from typing import Optional, Tuple

# Configuration du logging pour un suivi professionnel
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

class MiningAnalyzer:
    """
    Classe dédiée à l'analyse de performance d'infrastructure Web3 (GoMining).
    Permet le calcul du ROI et le monitoring des flux financiers on-chain.
    """

    def __init__(self, file_name: str = 'Monthly_performance.csv'):
        self.base_dir = os.path.dirname(__file__)
        self.data_path = os.path.normpath(os.path.join(self.base_dir, '../data', file_name))
        self.df_perf: Optional[pd.DataFrame] = None

    def load_data(self) -> bool:
        """Charge et nettoie les données du dataset."""
        try:
            if not os.path.exists(self.data_path):
                logging.error(f"Fichier introuvable à l'emplacement : {self.data_path}")
                return False
            
            self.df_perf = pd.read_csv(self.data_path)
            # Nettoyage : suppression de la ligne 'TOTAL' pour ne pas fausser les calculs
            self.df_perf = self.df_perf[self.df_perf['Mois'] != 'TOTAL']
            logging.info("Données chargées avec succès.")
            return True
        except Exception as e:
            logging.error(f"Erreur lors du chargement : {e}")
            return False

    def calculate_metrics(self) -> Tuple[float, float, float]:
        """Exécute les calculs financiers (Investissement, Récompenses, ROI)."""
        if self.df_perf is None:
            return 0.0, 0.0, 0.0

        total_invested = abs(self.df_perf['Dépenses (GOMINING)'].sum())
        total_rewards = self.df_perf['Récompenses (GOMINING)'].sum()
        
        roi_percentage = (total_rewards / total_invested * 100) if total_invested > 0 else 0.0
        
        return total_invested, total_rewards, roi_percentage

    def generate_report(self):
        """Affiche un rapport structuré de l'infrastructure."""
        if not self.load_data():
            return

        invested, rewards, roi = self.calculate_metrics()

        print("\n" + "="*42)
        print(f"{'RAPPORT D\'INFRASTRUCTURE GOMINING':^42}")
        print("="*42)
        print(f" Statut          : Opérationnel")
        print(f" Investissement  : {invested:>12.2f} GOMINING")
        print(f" Récompenses     : {rewards:>12.2f} GOMINING")
        print("-" * 42)
        print(f" ROI NET (14M)   : {roi:>11.2f}%")
        print("="*42 + "\n")

if __name__ == "__main__":
    analyzer = MiningAnalyzer()
    analyzer.generate_report()
