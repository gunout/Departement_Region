import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta
import warnings
warnings.filterwarnings('ignore')

class ReunionCollectiviteFinanceAnalyzer:
    def __init__(self, collectivite_name, collectivite_type):
        self.collectivite = collectivite_name
        self.type = collectivite_type  # 'departement' ou 'region'
        self.colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#F9A602', '#6A0572', 
                      '#AB83A1', '#5CAB7D', '#2A9D8F', '#E76F51', '#264653']
        
        self.start_year = 2002
        self.end_year = 2025
        
        # Configuration spécifique pour chaque collectivité
        self.config = self._get_collectivite_config()
        
    def _get_collectivite_config(self):
        """Retourne la configuration spécifique pour chaque collectivité réunionnaise"""
        if self.type == "departement":
            configs = {
                "Département Réunion": {
                    "population_base": 865000,
                    "budget_base": 1850 if self.type == "departement" else 950,
                    "type": self.type,
                    "specialites": ["action_sociale", "education", "routes", "culture", "environnement", "sante"]
                }
            }
        else:  # région
            configs = {
                "Région Réunion": {
                    "population_base": 865000,
                    "budget_base": 950,
                    "type": self.type,
                    "specialites": ["developpement_economique", "lycees", "formation", "transport", "amenagement", "tourisme"]
                }
            }
        
        return configs.get(self.collectivite, configs["Département Réunion" if self.type == "departement" else "Région Réunion"])
    
    def generate_financial_data(self):
        """Génère des données financières pour la collectivité"""
        print(f"🏛️ Génération des données financières pour {self.collectivite}...")
        
        # Créer une base de données annuelle
        dates = pd.date_range(start=f'{self.start_year}-01-01', 
                             end=f'{self.end_year}-12-31', freq='Y')
        
        data = {'Annee': [date.year for date in dates]}
        
        # Données démographiques
        data['Population'] = self._simulate_population(dates)
        
        # Recettes
        data['Recettes_Totales'] = self._simulate_total_revenue(dates)
        data['Impots_Locaux'] = self._simulate_tax_revenue(dates)
        data['Dotations_Etat'] = self._simulate_state_grants(dates)
        data['Autres_Recettes'] = self._simulate_other_revenue(dates)
        data['Fonds_Europeens'] = self._simulate_european_funds(dates)
        
        # Dépenses
        data['Depenses_Totales'] = self._simulate_total_expenses(dates)
        data['Fonctionnement'] = self._simulate_operating_expenses(dates)
        data['Investissement'] = self._simulate_investment_expenses(dates)
        data['Charge_Dette'] = self._simulate_debt_charges(dates)
        data['Personnel'] = self._simulate_staff_costs(dates)
        
        # Indicateurs financiers
        data['Epargne_Brute'] = self._simulate_gross_savings(dates)
        data['Dette_Totale'] = self._simulate_total_debt(dates)
        data['Taux_Endettement'] = self._simulate_debt_ratio(dates)
        data['Taux_Fiscalite'] = self._simulate_tax_rate(dates)
        
        # Investissements spécifiques adaptés à La Réunion
        if self.type == "departement":
            data['Investissement_Action_Sociale'] = self._simulate_social_investment(dates)
            data['Investissement_Education'] = self._simulate_education_investment(dates)
            data['Investissement_Routes'] = self._simulate_roads_investment(dates)
            data['Investissement_Sante'] = self._simulate_health_investment(dates)
            data['Investissement_Culture'] = self._simulate_culture_investment(dates)
        else:  # région
            data['Investissement_Lycees'] = self._simulate_highschool_investment(dates)
            data['Investissement_Formation'] = self._simulate_training_investment(dates)
            data['Investissement_Transport'] = self._simulate_transport_investment(dates)
            data['Investissement_Economie'] = self._simulate_economy_investment(dates)
            data['Investissement_Tourisme'] = self._simulate_tourism_investment(dates)
        
        df = pd.DataFrame(data)
        
        # Ajouter des tendances spécifiques à La Réunion
        self._add_collectivite_trends(df)
        
        return df
    
    def _simulate_population(self, dates):
        """Simule la population de La Réunion (croissance forte)"""
        base_population = self.config["population_base"]
        
        population = []
        for i, date in enumerate(dates):
            # Croissance démographique forte à La Réunion
            growth_rate = 0.015  # 1.5% de croissance annuelle
            
            growth = 1 + growth_rate * i
            population.append(base_population * growth)
        
        return population
    
    def _simulate_total_revenue(self, dates):
        """Simule les recettes totales de la collectivité"""
        base_revenue = self.config["budget_base"]
        
        revenue = []
        for i, date in enumerate(dates):
            # Croissance variable selon le type de collectivité
            if self.type == "departement":
                growth_rate = 0.038
            else:
                growth_rate = 0.042
                
            growth = 1 + growth_rate * i
            noise = np.random.normal(1, 0.07)
            revenue.append(base_revenue * growth * noise)
        
        return revenue
    
    def _simulate_tax_revenue(self, dates):
        """Simule les recettes fiscales"""
        if self.type == "departement":
            base_tax = self.config["budget_base"] * 0.25
        else:
            base_tax = self.config["budget_base"] * 0.20
        
        tax_revenue = []
        for i, date in enumerate(dates):
            growth = 1 + 0.03 * i
            noise = np.random.normal(1, 0.08)
            tax_revenue.append(base_tax * growth * noise)
        
        return tax_revenue
    
    def _simulate_state_grants(self, dates):
        """Simule les dotations de l'État (importantes pour les DOM)"""
        if self.type == "departement":
            base_grants = self.config["budget_base"] * 0.55
        else:
            base_grants = self.config["budget_base"] * 0.60
        
        grants = []
        for i, date in enumerate(dates):
            year = date.year
            # Augmentation des dotations pour les DOM
            if year >= 2010:
                increase = 1 + 0.01 * (year - 2010)
            else:
                increase = 1
            
            noise = np.random.normal(1, 0.05)
            grants.append(base_grants * increase * noise)
        
        return grants
    
    def _simulate_european_funds(self, dates):
        """Simule les fonds européens (importants pour La Réunion)"""
        if self.type == "departement":
            base_funds = self.config["budget_base"] * 0.08
        else:
            base_funds = self.config["budget_base"] * 0.12
        
        funds = []
        for i, date in enumerate(dates):
            year = date.year
            # Cycles des fonds européens
            if 2007 <= year <= 2013:
                multiplier = 1.2  # Période de programmation 2007-2013
            elif 2014 <= year <= 2020:
                multiplier = 1.4  # Période de programmation 2014-2020
            elif year >= 2021:
                multiplier = 1.3  # Période de programmation 2021-2027
            else:
                multiplier = 1.0
            
            growth = 1 + 0.025 * i
            noise = np.random.normal(1, 0.15)
            funds.append(base_funds * growth * multiplier * noise)
        
        return funds
    
    def _simulate_other_revenue(self, dates):
        """Simule les autres recettes"""
        if self.type == "departement":
            base_other = self.config["budget_base"] * 0.12
        else:
            base_other = self.config["budget_base"] * 0.08
        
        other_revenue = []
        for i, date in enumerate(dates):
            growth = 1 + 0.028 * i
            noise = np.random.normal(1, 0.09)
            other_revenue.append(base_other * growth * noise)
        
        return other_revenue
    
    def _simulate_total_expenses(self, dates):
        """Simule les dépenses totales"""
        base_expenses = self.config["budget_base"] * 0.98
        
        expenses = []
        for i, date in enumerate(dates):
            growth = 1 + 0.036 * i
            noise = np.random.normal(1, 0.06)
            expenses.append(base_expenses * growth * noise)
        
        return expenses
    
    def _simulate_operating_expenses(self, dates):
        """Simule les dépenses de fonctionnement"""
        if self.type == "departement":
            base_operating = self.config["budget_base"] * 0.70
        else:
            base_operating = self.config["budget_base"] * 0.65
        
        operating = []
        for i, date in enumerate(dates):
            growth = 1 + 0.033 * i
            noise = np.random.normal(1, 0.05)
            operating.append(base_operating * growth * noise)
        
        return operating
    
    def _simulate_investment_expenses(self, dates):
        """Simule les dépenses d'investissement"""
        if self.type == "departement":
            base_investment = self.config["budget_base"] * 0.28
        else:
            base_investment = self.config["budget_base"] * 0.33
        
        investment = []
        for i, date in enumerate(dates):
            year = date.year
            # Plans d'investissement spécifiques aux DOM
            if year in [2007, 2013, 2019, 2024]:
                multiplier = 1.6
            elif year in [2009, 2015, 2021]:
                multiplier = 0.8
            else:
                multiplier = 1.0
            
            growth = 1 + 0.03 * i
            noise = np.random.normal(1, 0.16)
            investment.append(base_investment * growth * multiplier * noise)
        
        return investment
    
    def _simulate_debt_charges(self, dates):
        """Simule les charges de la dette"""
        if self.type == "departement":
            base_debt_charge = self.config["budget_base"] * 0.06
        else:
            base_debt_charge = self.config["budget_base"] * 0.05
        
        debt_charges = []
        for i, date in enumerate(dates):
            year = date.year
            if year >= 2005:
                increase = 1 + 0.008 * (year - 2005)
            else:
                increase = 1
            
            noise = np.random.normal(1, 0.10)
            debt_charges.append(base_debt_charge * increase * noise)
        
        return debt_charges
    
    def _simulate_staff_costs(self, dates):
        """Simule les dépenses de personnel"""
        if self.type == "departement":
            base_staff = self.config["budget_base"] * 0.40
        else:
            base_staff = self.config["budget_base"] * 0.35
        
        staff_costs = []
        for i, date in enumerate(dates):
            growth = 1 + 0.032 * i
            noise = np.random.normal(1, 0.04)
            staff_costs.append(base_staff * growth * noise)
        
        return staff_costs
    
    def _simulate_gross_savings(self, dates):
        """Simule l'épargne brute"""
        if self.type == "departement":
            base_saving = self.config["budget_base"] * 0.04
        else:
            base_saving = self.config["budget_base"] * 0.05
        
        savings = []
        for i, date in enumerate(dates):
            year = date.year
            if year >= 2010:
                improvement = 1 + 0.007 * (year - 2010)
            else:
                improvement = 1
            
            noise = np.random.normal(1, 0.14)
            savings.append(base_saving * improvement * noise)
        
        return savings
    
    def _simulate_total_debt(self, dates):
        """Simule la dette totale"""
        if self.type == "departement":
            base_debt = self.config["budget_base"] * 0.80
        else:
            base_debt = self.config["budget_base"] * 0.75
        
        debt = []
        for i, date in enumerate(dates):
            year = date.year
            if year in [2007, 2013, 2019, 2024]:
                change = 1.2
            elif year in [2009, 2015, 2021]:
                change = 0.9
            else:
                change = 1.0
            
            noise = np.random.normal(1, 0.09)
            debt.append(base_debt * change * noise)
        
        return debt
    
    def _simulate_debt_ratio(self, dates):
        """Simule le taux d'endettement"""
        ratios = []
        for i, date in enumerate(dates):
            if self.type == "departement":
                base_ratio = 0.75
            else:
                base_ratio = 0.70
            
            year = date.year
            if year >= 2010:
                improvement = 1 - 0.009 * (year - 2010)
            else:
                improvement = 1
            
            noise = np.random.normal(1, 0.06)
            ratios.append(base_ratio * improvement * noise)
        
        return ratios
    
    def _simulate_tax_rate(self, dates):
        """Simule le taux de fiscalité (moyen)"""
        rates = []
        for i, date in enumerate(dates):
            if self.type == "departement":
                base_rate = 0.82
            else:
                base_rate = 0.78
            
            year = date.year
            if year >= 2010:
                increase = 1 + 0.004 * (year - 2010)
            else:
                increase = 1
            
            noise = np.random.normal(1, 0.03)
            rates.append(base_rate * increase * noise)
        
        return rates
    
    # Méthodes d'investissement spécifiques au Département
    def _simulate_social_investment(self, dates):
        """Simule l'investissement dans l'action sociale"""
        base_investment = self.config["budget_base"] * 0.08
        
        investment = []
        for i, date in enumerate(dates):
            year = date.year
            if year in [2005, 2010, 2015, 2020]:
                year_multiplier = 1.8
            else:
                year_multiplier = 1.0
            
            growth = 1 + 0.035 * i
            noise = np.random.normal(1, 0.15)
            investment.append(base_investment * growth * year_multiplier * noise)
        
        return investment
    
    def _simulate_education_investment(self, dates):
        """Simule l'investissement éducatif (collèges)"""
        base_investment = self.config["budget_base"] * 0.06
        
        investment = []
        for i, date in enumerate(dates):
            year = date.year
            if year in [2008, 2014, 2020]:
                year_multiplier = 1.7
            else:
                year_multiplier = 1.0
            
            growth = 1 + 0.032 * i
            noise = np.random.normal(1, 0.18)
            investment.append(base_investment * growth * year_multiplier * noise)
        
        return investment
    
    def _simulate_roads_investment(self, dates):
        """Simule l'investissement dans les routes"""
        base_investment = self.config["budget_base"] * 0.05
        
        investment = []
        for i, date in enumerate(dates):
            year = date.year
            if year in [2006, 2012, 2018, 2023]:
                year_multiplier = 1.9
            else:
                year_multiplier = 1.0
            
            growth = 1 + 0.03 * i
            noise = np.random.normal(1, 0.16)
            investment.append(base_investment * growth * year_multiplier * noise)
        
        return investment
    
    def _simulate_health_investment(self, dates):
        """Simule l'investissement dans la santé"""
        base_investment = self.config["budget_base"] * 0.04
        
        investment = []
        for i, date in enumerate(dates):
            year = date.year
            if year in [2009, 2015, 2021]:
                year_multiplier = 1.8
            else:
                year_multiplier = 1.0
            
            growth = 1 + 0.034 * i
            noise = np.random.normal(1, 0.17)
            investment.append(base_investment * growth * year_multiplier * noise)
        
        return investment
    
    def _simulate_culture_investment(self, dates):
        """Simule l'investissement culturel"""
        base_investment = self.config["budget_base"] * 0.03
        
        investment = []
        for i, date in enumerate(dates):
            year = date.year
            if year in [2010, 2016, 2022]:
                year_multiplier = 1.7
            else:
                year_multiplier = 1.0
            
            growth = 1 + 0.028 * i
            noise = np.random.normal(1, 0.15)
            investment.append(base_investment * growth * year_multiplier * noise)
        
        return investment
    
    # Méthodes d'investissement spécifiques à la Région
    def _simulate_highschool_investment(self, dates):
        """Simule l'investissement dans les lycées"""
        base_investment = self.config["budget_base"] * 0.07
        
        investment = []
        for i, date in enumerate(dates):
            year = date.year
            if year in [2008, 2014, 2020]:
                year_multiplier = 1.8
            else:
                year_multiplier = 1.0
            
            growth = 1 + 0.035 * i
            noise = np.random.normal(1, 0.17)
            investment.append(base_investment * growth * year_multiplier * noise)
        
        return investment
    
    def _simulate_training_investment(self, dates):
        """Simule l'investissement dans la formation"""
        base_investment = self.config["budget_base"] * 0.06
        
        investment = []
        for i, date in enumerate(dates):
            year = date.year
            if year in [2009, 2015, 2021]:
                year_multiplier = 1.9
            else:
                year_multiplier = 1.0
            
            growth = 1 + 0.036 * i
            noise = np.random.normal(1, 0.18)
            investment.append(base_investment * growth * year_multiplier * noise)
        
        return investment
    
    def _simulate_transport_investment(self, dates):
        """Simule l'investissement dans les transports"""
        base_investment = self.config["budget_base"] * 0.08
        
        investment = []
        for i, date in enumerate(dates):
            year = date.year
            if year in [2007, 2013, 2019, 2024]:
                year_multiplier = 2.0
            else:
                year_multiplier = 1.0
            
            growth = 1 + 0.04 * i
            noise = np.random.normal(1, 0.20)
            investment.append(base_investment * growth * year_multiplier * noise)
        
        return investment
    
    def _simulate_economy_investment(self, dates):
        """Simule l'investissement dans l'économie"""
        base_investment = self.config["budget_base"] * 0.05
        
        investment = []
        for i, date in enumerate(dates):
            year = date.year
            if year in [2010, 2016, 2022]:
                year_multiplier = 1.7
            else:
                year_multiplier = 1.0
            
            growth = 1 + 0.033 * i
            noise = np.random.normal(1, 0.16)
            investment.append(base_investment * growth * year_multiplier * noise)
        
        return investment
    
    def _simulate_tourism_investment(self, dates):
        """Simule l'investissement dans le tourisme"""
        base_investment = self.config["budget_base"] * 0.04
        
        investment = []
        for i, date in enumerate(dates):
            year = date.year
            if year in [2011, 2017, 2023]:
                year_multiplier = 1.8
            else:
                year_multiplier = 1.0
            
            growth = 1 + 0.035 * i
            noise = np.random.normal(1, 0.19)
            investment.append(base_investment * growth * year_multiplier * noise)
        
        return investment
    
    def _add_collectivite_trends(self, df):
        """Ajoute des tendances réalistes adaptées à La Réunion"""
        for i, row in df.iterrows():
            year = row['Annee']
            
            # Développement initial (2002-2005)
            if 2002 <= year <= 2005:
                if self.type == "departement":
                    df.loc[i, 'Investissement_Action_Sociale'] *= 1.4
                    df.loc[i, 'Investissement_Routes'] *= 1.5
                else:
                    df.loc[i, 'Investissement_Lycees'] *= 1.4
                    df.loc[i, 'Investissement_Transport'] *= 1.6
            
            # Plan de développement réunionnais (2006-2010)
            if 2006 <= year <= 2010:
                df.loc[i, 'Dotations_Etat'] *= 1.12
                df.loc[i, 'Fonds_Europeens'] *= 1.25
                df.loc[i, 'Investissement'] *= 1.18
            
            # Impact de la crise financière (2008-2009)
            if 2008 <= year <= 2009:
                df.loc[i, 'Recettes_Totales'] *= 0.94
                df.loc[i, 'Investissement'] *= 0.82
            
            # Développement du tourisme et des infrastructures (2011-2015)
            elif 2011 <= year <= 2015:
                if self.type == "departement":
                    df.loc[i, 'Investissement_Sante'] *= 1.3
                else:
                    df.loc[i, 'Investissement_Tourisme'] *= 1.5
                    df.loc[i, 'Investissement_Transport'] *= 1.4
            
            # Crise sociale de 2018 et plan de soutien
            if year == 2018:
                df.loc[i, 'Dotations_Etat'] *= 1.15
                if self.type == "departement":
                    df.loc[i, 'Investissement_Action_Sociale'] *= 1.4
            
            # Impact de la crise COVID-19 (2020-2021)
            if 2020 <= year <= 2021:
                if year == 2020:
                    # Baisse des recettes mais soutien de l'État et de l'Europe
                    df.loc[i, 'Autres_Recettes'] *= 0.75
                    df.loc[i, 'Dotations_Etat'] *= 1.18
                    df.loc[i, 'Fonds_Europeens'] *= 1.22
            
            # Plan de relance post-COVID spécifique aux DOM (2022-2025)
            if year >= 2022:
                df.loc[i, 'Investissement'] *= 1.16
                if self.type == "departement":
                    df.loc[i, 'Investissement_Sante'] *= 1.3
                else:
                    df.loc[i, 'Investissement_Economie'] *= 1.4
                    df.loc[i, 'Investissement_Formation'] *= 1.35
    
    def create_financial_analysis(self, df):
        """Crée une analyse complète des finances de la collectivité"""
        plt.style.use('seaborn-v0_8')
        fig = plt.figure(figsize=(20, 24))
        
        # 1. Évolution des recettes et dépenses
        ax1 = plt.subplot(4, 2, 1)
        self._plot_revenue_expenses(df, ax1)
        
        # 2. Structure des recettes
        ax2 = plt.subplot(4, 2, 2)
        self._plot_revenue_structure(df, ax2)
        
        # 3. Structure des dépenses
        ax3 = plt.subplot(4, 2, 3)
        self._plot_expenses_structure(df, ax3)
        
        # 4. Investissements
        ax4 = plt.subplot(4, 2, 4)
        self._plot_investments(df, ax4)
        
        # 5. Dette et endettement
        ax5 = plt.subplot(4, 2, 5)
        self._plot_debt(df, ax5)
        
        # 6. Indicateurs de performance
        ax6 = plt.subplot(4, 2, 6)
        self._plot_performance_indicators(df, ax6)
        
        # 7. Démographie
        ax7 = plt.subplot(4, 2, 7)
        self._plot_demography(df, ax7)
        
        # 8. Investissements sectoriels
        ax8 = plt.subplot(4, 2, 8)
        self._plot_sectorial_investments(df, ax8)
        
        plt.suptitle(f'Analyse des Comptes de {self.collectivite} - La Réunion ({self.start_year}-{self.end_year})', 
                    fontsize=16, fontweight='bold')
        plt.tight_layout()
        plt.savefig(f'{self.collectivite.replace(" ", "_")}_financial_analysis.png', dpi=300, bbox_inches='tight')
        plt.show()
        
        # Générer les insights
        self._generate_financial_insights(df)
    
    def _plot_revenue_expenses(self, df, ax):
        """Plot de l'évolution des recettes et dépenses"""
        ax.plot(df['Annee'], df['Recettes_Totales'], label='Recettes Totales', 
               linewidth=2, color='#2A9D8F', alpha=0.8)
        ax.plot(df['Annee'], df['Depenses_Totales'], label='Dépenses Totales', 
               linewidth=2, color='#E76F51', alpha=0.8)
        
        ax.set_title('Évolution des Recettes et Dépenses (M€)', 
                    fontsize=12, fontweight='bold')
        ax.set_ylabel('Montants (M€)')
        ax.legend()
        ax.grid(True, alpha=0.3)
    
    def _plot_revenue_structure(self, df, ax):
        """Plot de la structure des recettes"""
        years = df['Annee']
        width = 0.8
        
        bottom = np.zeros(len(years))
        categories = ['Impots_Locaux', 'Dotations_Etat', 'Fonds_Europeens', 'Autres_Recettes']
        colors = ['#264653', '#2A9D8F', '#E76F51', '#F9A602']
        labels = ['Impôts Locaux', 'Dotations État', 'Fonds Européens', 'Autres Recettes']
        
        for i, category in enumerate(categories):
            ax.bar(years, df[category], width, label=labels[i], bottom=bottom, color=colors[i])
            bottom += df[category]
        
        ax.set_title('Structure des Recettes (M€)', fontsize=12, fontweight='bold')
        ax.set_ylabel('Montants (M€)')
        ax.legend()
        ax.grid(True, alpha=0.3, axis='y')
    
    def _plot_expenses_structure(self, df, ax):
        """Plot de la structure des dépenses"""
        years = df['Annee']
        width = 0.8
        
        bottom = np.zeros(len(years))
        categories = ['Fonctionnement', 'Investissement', 'Charge_Dette', 'Personnel']
        colors = ['#264653', '#2A9D8F', '#E76F51', '#F9A602']
        labels = ['Fonctionnement', 'Investissement', 'Charge Dette', 'Personnel']
        
        for i, category in enumerate(categories):
            ax.bar(years, df[category], width, label=labels[i], bottom=bottom, color=colors[i])
            bottom += df[category]
        
        ax.set_title('Structure des Dépenses (M€)', fontsize=12, fontweight='bold')
        ax.set_ylabel('Montants (M€)')
        ax.legend()
        ax.grid(True, alpha=0.3, axis='y')
    
    def _plot_investments(self, df, ax):
        """Plot des investissements"""
        if self.type == "departement":
            ax.plot(df['Annee'], df['Investissement_Action_Sociale'], label='Action Sociale', 
                   linewidth=2, color='#264653', alpha=0.8)
            ax.plot(df['Annee'], df['Investissement_Education'], label='Éducation', 
                   linewidth=2, color='#2A9D8F', alpha=0.8)
            ax.plot(df['Annee'], df['Investissement_Routes'], label='Routes', 
                   linewidth=2, color='#E76F51', alpha=0.8)
            ax.plot(df['Annee'], df['Investissement_Sante'], label='Santé', 
                   linewidth=2, color='#F9A602', alpha=0.8)
            ax.plot(df['Annee'], df['Investissement_Culture'], label='Culture', 
                   linewidth=2, color='#6A0572', alpha=0.8)
        else:
            ax.plot(df['Annee'], df['Investissement_Lycees'], label='Lycées', 
                   linewidth=2, color='#264653', alpha=0.8)
            ax.plot(df['Annee'], df['Investissement_Formation'], label='Formation', 
                   linewidth=2, color='#2A9D8F', alpha=0.8)
            ax.plot(df['Annee'], df['Investissement_Transport'], label='Transport', 
                   linewidth=2, color='#E76F51', alpha=0.8)
            ax.plot(df['Annee'], df['Investissement_Economie'], label='Économie', 
                   linewidth=2, color='#F9A602', alpha=0.8)
            ax.plot(df['Annee'], df['Investissement_Tourisme'], label='Tourisme', 
                   linewidth=2, color='#6A0572', alpha=0.8)
        
        ax.set_title('Répartition des Investissements (M€)', fontsize=12, fontweight='bold')
        ax.set_ylabel('Montants (M€)')
        ax.legend()
        ax.grid(True, alpha=0.3)
    
    def _plot_debt(self, df, ax):
        """Plot de la dette et du taux d'endettement"""
        # Dette totale
        ax.bar(df['Annee'], df['Dette_Totale'], label='Dette Totale (M€)', 
              color='#264653', alpha=0.7)
        
        ax.set_title('Dette et Taux d\'Endettement', fontsize=12, fontweight='bold')
        ax.set_ylabel('Dette (M€)', color='#264653')
        ax.tick_params(axis='y', labelcolor='#264653')
        ax.grid(True, alpha=0.3, axis='y')
        
        # Taux d'endettement en second axe
        ax2 = ax.twinx()
        ax2.plot(df['Annee'], df['Taux_Endettement'], label='Taux d\'Endettement', 
                linewidth=3, color='#E76F51')
        ax2.set_ylabel('Taux d\'Endettement', color='#E76F51')
        ax2.tick_params(axis='y', labelcolor='#E76F51')
        
        # Combiner les légendes
        lines1, labels1 = ax.get_legend_handles_labels()
        lines2, labels2 = ax2.get_legend_handles_labels()
        ax.legend(lines1 + lines2, labels1 + labels2, loc='upper left')
    
    def _plot_performance_indicators(self, df, ax):
        """Plot des indicateurs de performance"""
        # Épargne brute
        ax.bar(df['Annee'], df['Epargne_Brute'], label='Épargne Brute (M€)', 
              color='#2A9D8F', alpha=0.7)
        
        ax.set_title('Indicateurs de Performance', fontsize=12, fontweight='bold')
        ax.set_ylabel('Épargne Brute (M€)', color='#2A9D8F')
        ax.tick_params(axis='y', labelcolor='#2A9D8F')
        ax.grid(True, alpha=0.3, axis='y')
        
        # Taux de fiscalité en second axe
        ax2 = ax.twinx()
        ax2.plot(df['Annee'], df['Taux_Fiscalite'], label='Taux de Fiscalité', 
                linewidth=3, color='#F9A602')
        ax2.set_ylabel('Taux de Fiscalité', color='#F9A602')
        ax2.tick_params(axis='y', labelcolor='#F9A602')
        
        # Combiner les légendes
        lines1, labels1 = ax.get_legend_handles_labels()
        lines2, labels2 = ax2.get_legend_handles_labels()
        ax.legend(lines1 + lines2, labels1 + labels2, loc='upper left')
    
    def _plot_demography(self, df, ax):
        """Plot de l'évolution démographique"""
        ax.plot(df['Annee'], df['Population'], label='Population', 
               linewidth=2, color='#264653', alpha=0.8)
        
        ax.set_title('Évolution Démographique', fontsize=12, fontweight='bold')
        ax.set_ylabel('Population', color='#264653')
        ax.tick_params(axis='y', labelcolor='#264653')
        ax.grid(True, alpha=0.3)
    
    def _plot_sectorial_investments(self, df, ax):
        """Plot des investissements sectoriels"""
        years = df['Annee']
        width = 0.8
        
        bottom = np.zeros(len(years))
        if self.type == "departement":
            categories = ['Investissement_Action_Sociale', 'Investissement_Education', 
                         'Investissement_Routes', 'Investissement_Sante', 'Investissement_Culture']
            colors = ['#264653', '#2A9D8F', '#E76F51', '#F9A602', '#6A0572']
            labels = ['Action Sociale', 'Éducation', 'Routes', 'Santé', 'Culture']
        else:
            categories = ['Investissement_Lycees', 'Investissement_Formation', 
                         'Investissement_Transport', 'Investissement_Economie', 'Investissement_Tourisme']
            colors = ['#264653', '#2A9D8F', '#E76F51', '#F9A602', '#6A0572']
            labels = ['Lycées', 'Formation', 'Transport', 'Économie', 'Tourisme']
        
        for i, category in enumerate(categories):
            ax.bar(years, df[category], width, label=labels[i], bottom=bottom, color=colors[i])
            bottom += df[category]
        
        ax.set_title('Répartition Sectorielle des Investissements (M€)', fontsize=12, fontweight='bold')
        ax.set_ylabel('Montants (M€)')
        ax.legend()
        ax.grid(True, alpha=0.3, axis='y')
    
    def _generate_financial_insights(self, df):
        """Génère des insights analytiques adaptés à La Réunion"""
        print(f"🏛️ INSIGHTS ANALYTIQUES - {self.collectivite} (La Réunion)")
        print("=" * 60)
        
        # 1. Statistiques de base
        print("\n1. 📈 STATISTIQUES GÉNÉRALES:")
        avg_revenue = df['Recettes_Totales'].mean()
        avg_expenses = df['Depenses_Totales'].mean()
        avg_savings = df['Epargne_Brute'].mean()
        avg_debt = df['Dette_Totale'].mean()
        
        print(f"Recettes moyennes annuelles: {avg_revenue:.2f} M€")
        print(f"Dépenses moyennes annuelles: {avg_expenses:.2f} M€")
        print(f"Épargne brute moyenne: {avg_savings:.2f} M€")
        print(f"Dette moyenne: {avg_debt:.2f} M€")
        
        # 2. Croissance
        print("\n2. 📊 TAUX DE CROISSANCE:")
        revenue_growth = ((df['Recettes_Totales'].iloc[-1] / 
                          df['Recettes_Totales'].iloc[0]) - 1) * 100
        population_growth = ((df['Population'].iloc[-1] / 
                             df['Population'].iloc[0]) - 1) * 100
        
        print(f"Croissance des recettes ({self.start_year}-{self.end_year}): {revenue_growth:.1f}%")
        print(f"Croissance de la population ({self.start_year}-{self.end_year}): {population_growth:.1f}%")
        
        # 3. Structure financière (spécificités réunionnaises)
        print("\n3. 📋 STRUCTURE FINANCIÈRE:")
        tax_share = (df['Impots_Locaux'].mean() / df['Recettes_Totales'].mean()) * 100
        state_share = (df['Dotations_Etat'].mean() / df['Recettes_Totales'].mean()) * 100
        europe_share = (df['Fonds_Europeens'].mean() / df['Recettes_Totales'].mean()) * 100
        investment_share = (df['Investissement'].mean() / df['Depenses_Totales'].mean()) * 100
        
        print(f"Part des impôts locaux dans les recettes: {tax_share:.1f}%")
        print(f"Part des dotations de l'État dans les recettes: {state_share:.1f}%")
        print(f"Part des fonds européens dans les recettes: {europe_share:.1f}%")
        print(f"Part de l'investissement dans les dépenses: {investment_share:.1f}%")
        
        # 4. Dette et fiscalité
        print("\n4. 💰 ENDETTEMENT ET FISCALITÉ:")
        avg_debt_ratio = df['Taux_Endettement'].mean() * 100
        avg_tax_rate = df['Taux_Fiscalite'].mean()
        last_debt_ratio = df['Taux_Endettement'].iloc[-1] * 100
        
        print(f"Taux d'endettement moyen: {avg_debt_ratio:.1f}%")
        print(f"Taux d'endettement final: {last_debt_ratio:.1f}%")
        print(f"Taux de fiscalité moyen: {avg_tax_rate:.2f}")
        
        # 5. Spécificités de la collectivité réunionnaise
        print(f"\n5. 🌟 SPÉCIFICITÉS DE {self.collectivite.upper()} (LA RÉUNION):")
        print(f"Type de collectivité: {self.config['type']}")
        print(f"Spécialités: {', '.join(self.config['specialites'])}")
        
        # 6. Événements marquants spécifiques à La Réunion
        print("\n6. 📅 ÉVÉNEMENTS MARQUANTS LA RÉUNION:")
        print("• 2002-2005: Développement initial et renforcement des infrastructures")
        print("• 2006-2010: Plan de développement réunionnais et investissements européens")
        print("• 2011-2015: Développement du tourisme et des infrastructures")
        print("• 2018: Crise sociale et plan de soutien")
        print("• 2020-2021: Impact de la crise COVID-19 et plans de soutien")
        print("• 2022-2025: Plan de relance post-COVID spécifique aux DOM")
        
        # 7. Recommandations adaptées à La Réunion
        print("\n7. 💡 RECOMMANDATIONS STRATÉGIQUES:")
        if self.type == "departement":
            print("• Renforcer l'action sociale face aux défis démographiques")
            print("• Moderniser les collèges et les infrastructures éducatives")
            print("• Développer les infrastructures routières pour désenclaver les territoires")
            print("• Améliorer l'accès aux soins et aux services de santé")
        else:
            print("• Développer les lycées et la formation professionnelle")
            print("• Améliorer les transports régionaux (routes, transports en commun)")
            print("• Soutenir le développement économique et l'innovation")
            print("• Promouvoir le tourisme durable et responsable")
        
        print("• Valoriser les fonds européens et les programmes de coopération")
        print("• Développer les énergies renouvelables et l'autonomie énergétique")
        print("• Préserver la biodiversité unique de La Réunion")
        print("• Renforcer la coopération régionale dans l'océan Indien")

def main():
    """Fonction principale pour La Réunion"""
    print("🏛️ ANALYSE DES COMPTES DU DÉPARTEMENT ET DE LA RÉGION RÉUNION (2002-2025)")
    print("=" * 70)
    
    # Demander à l'utilisateur de choisir une collectivité
    print("Choix de la collectivité:")
    print("1. Département Réunion")
    print("2. Région Réunion")
    
    try:
        choix = int(input("\nChoisissez le numéro de la collectivité à analyser: "))
        if choix == 1:
            collectivite_selectionnee = "Département Réunion"
            collectivite_type = "departement"
        elif choix == 2:
            collectivite_selectionnee = "Région Réunion"
            collectivite_type = "region"
        else:
            raise ValueError
    except (ValueError, IndexError):
        print("Choix invalide. Sélection du Département Réunion par défaut.")
        collectivite_selectionnee = "Département Réunion"
        collectivite_type = "departement"
    
    # Initialiser l'analyseur
    analyzer = ReunionCollectiviteFinanceAnalyzer(collectivite_selectionnee, collectivite_type)
    
    # Générer les données
    financial_data = analyzer.generate_financial_data()
    
    # Sauvegarder les données
    output_file = f'{collectivite_selectionnee.replace(" ", "_")}_financial_data_2002_2025.csv'
    financial_data.to_csv(output_file, index=False)
    print(f"💾 Données sauvegardées: {output_file}")
    
    # Aperçu des données
    print("\n👀 Aperçu des données:")
    print(financial_data[['Annee', 'Population', 'Recettes_Totales', 'Depenses_Totales', 'Dette_Totale']].head())
    
    # Créer l'analyse
    print("\n📈 Création de l'analyse financière...")
    analyzer.create_financial_analysis(financial_data)
    
    print(f"\n✅ Analyse des comptes de {collectivite_selectionnee} terminée!")
    print(f"📊 Période: {analyzer.start_year}-{analyzer.end_year}")
    print("📦 Données: Démographie, finances, investissements, dette")

if __name__ == "__main__":
    main()