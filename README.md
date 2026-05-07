# 🛰️ GoMining Infrastructure: Yield Optimization & On-Chain Analysis
> **Système de pilotage de performance pour une ferme de minage BTC virtualisée.**

![Status](https://img.shields.io/badge/Status-Operational-brightgreen)
![Data Pipeline](https://img.shields.io/badge/Pipeline-Python_|_Pandas_|_Notion_API-blue)
![ROI](https://img.shields.io/badge/ROI-115%25_/_14_months-gold)

## 🎯 Vision du Projet
Ce repository n'est pas un simple log de transactions. C'est une **architecture de monitoring de données Web3** visant à optimiser l'efficience énergétique et la rentabilité d'une infrastructure de minage de **104.75 TH/s**. 

L'objectif : Transformer des données brutes on-chain en **intelligence décisionnelle**.

---

## 🛠️ Architecture du Système
Le projet repose sur un pipeline de données en 3 étapes :
1. **Extraction :** Récupération des logs de rewards et de maintenance via les smart contracts GoMining.
2. **Traitement (ETL) :** Script Python (`src/analyzer.py`) utilisant Pandas pour calculer le coût réel du TH/s par rapport à la volatilité du BTC.
3. **Visualisation :** Synchronisation vers un Dashboard Notion pour le pilotage stratégique (OpEx vs RevEx).

---

## 📊 Métriques d'Ingénierie & Performance
| Métrique | Valeur | Impact Business |
| :--- | :--- | :--- |
| **Hashrate** | 104.75 TH/s | Capacité de production brute stable. |
| **Energy Efficiency** | 17.61 W/TH | Optimisation des coûts opérationnels (OpEx). |
| **Yield Strategy** | Game-Fi Reinvestment | Neutralisation des frais de maintenance via les mécaniques d'écosystème. |
| **Financial Health** | +115% ROI | Validation de la stratégie de croissance sur 14 mois. |

---

| "AI & Infrastructure Developer | 104 TH/s Mining Management".
| "Current Stack" : Python, HTML/CSS, Prompt Engineering, Crypto-Forensics.


## 📂 Structure du Repository (Modulaire)
```text
├── data/               # Datasets structurés (CSV/JSON)
├── src/                # Scripts d'analyse & Core Logic
│   ├── analyzer.py   # Logique de calcul du ROI & Net Profit
│   └── utils.py        # Helpers pour le formatage des données
├── docs/               # Schémas d'architecture & Rapports mensuels
└── README.md           # Documentation technique
