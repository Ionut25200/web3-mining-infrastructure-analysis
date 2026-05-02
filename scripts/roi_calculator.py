import pandas as pd
import os

def calculate_mining_roi():
    # Définition du chemin relatif vers les données
    base_dir = os.path.dirname(__file__)
    data_path = os.path.join(base_dir, '../data/Monthly_performance.csv')
    
    try:
        # Lecture du fichier de performance
        df_perf = pd.read_csv(data_path)
        
        # Nettoyage : on ignore la ligne 'TOTAL' si elle est présente dans le fichier
        df_perf = df_perf[df_perf['Mois'] != 'TOTAL']
        
        # Calcul des totaux
        total_invested = abs(df_perf['Dépenses (GOMINING)'].sum())
        total_rewards = df_perf['Récompenses (GOMINING)'].sum()
        
        # Calcul du ROI
        if total_invested > 0:
            roi_percentage = (total_rewards / total_invested) * 100
        else:
            roi_percentage = 0
            
        print(f"==========================================")
        print(f"   RAPPORT D'INFRASTRUCTURE GOMINING      ")
        print(f"==========================================")
        print(f"Statut : Opérationnel")
        print(f"Investissement Cumulé : {total_invested:.2f} GOMINING")
        print(f"Récompenses Cumulées  : {total_rewards:.2f} GOMINING")
        print(f"------------------------------------------")
        print(f"ROI NET SUR 14 MOIS   : {roi_percentage:.2f}%")
        print(f"==========================================")

    except FileNotFoundError:
        print("Erreur : Le fichier de données est introuvable dans /data.")
    except Exception as e:
        print(f"Une erreur est survenue : {e}")

if __name__ == "__main__":
    calculate_mining_roi()
