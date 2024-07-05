import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
import numpy as np
import tkinter as tk
from tkinter import ttk

# Fetch cryptocurrency data
def fetch_data(coin='BTC', currency='EUR', days=500):
    url = f"https://min-api.cryptocompare.com/data/histoday?fsym={coin}&tsym={currency}&limit={days}"
    response = requests.get(url)
    data = response.json()['Data']
    df = pd.DataFrame(data)
    df['time'] = pd.to_datetime(df['time'], unit='s')
    return df

# Predict future prices using linear regression
def predict_prices(df, days_in_future=10):
    df = df[['close']].copy()  # Create a copy to avoid SettingWithCopyWarning
    df['day'] = range(len(df))
    X = df['day'].values.reshape(-1, 1)
    y = df['close'].values
    model = LinearRegression()
    model.fit(X, y)
    future_days = np.array([len(df) + i for i in range(days_in_future)]).reshape(-1, 1)
    predictions = model.predict(future_days)
    return predictions, future_days

# Plot combined historical prices and future price predictions
def plot_combined(df, predictions, future_days, coin, currency):
    plt.figure(figsize=(14, 7))
    sns.set(style="whitegrid")
    
    # Plot historical prices
    #plt.plot(df['time'], df['close'], label='Prix de Fermeture', marker='o', linestyle='-', color='blue')
    
    # Create future dates
    last_date = df['time'].iloc[-1]
    future_dates = pd.date_range(start=last_date, periods=len(future_days) + 1)[1:]
    
    # Combine historical and future dates for plotting
    combined_dates = pd.concat([df['time'], pd.Series(future_dates)])
    combined_prices = pd.concat([df['close'], pd.Series(predictions)])
    
    # Plot future predictions
    plt.plot(combined_dates, combined_prices, label='Prédiction de Prix', marker='o', linestyle='-', color='blue')
    
    # Highlight the highest and lowest points in historical data
    max_price = df['close'].max()
    min_price = df['close'].min()
    max_date = df['time'][df['close'].idxmax()]
    min_date = df['time'][df['close'].idxmin()]
    
    plt.scatter(max_date, max_price, color='green', label=f'Prix le Plus Haut: {max_price:.2f} {currency}', zorder=5)
    plt.scatter(min_date, min_price, color='red', label=f'Prix le Plus Bas: {min_price:.2f} {currency}', zorder=5)
    
    plt.title(f'Prix de Fermeture et Prédictions de {coin} en {currency}')
    plt.xlabel('Date')
    plt.ylabel(f'Prix ({currency})')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(f'{coin}_combined_price_prediction.png')
    plt.show()

# Main function to create the GUI and handle user input
def main():
    def on_submit():
        coin = coin_var.get()
        currency = currency_var.get()
        days = days_var.get()
        days_in_future = days_future_var.get()

        if coin and currency and days and days_in_future:
            df = fetch_data(coin, currency, int(days))
            predictions, future_days = predict_prices(df, int(days_in_future))
            plot_combined(df, predictions, future_days, coin, currency)
        else:
            print("Tous les champs doivent être remplis.")

    root = tk.Tk()
    root.title("Sélection de Cryptomonnaie")

    # Variables
    coin_var = tk.StringVar(value='BTC')
    currency_var = tk.StringVar(value='EUR')
    days_var = tk.StringVar(value='500')
    days_future_var = tk.StringVar(value='10')

    # Labels
    tk.Label(root, text="Choisissez la cryptomonnaie:").grid(row=0, column=0, padx=10, pady=5)
    tk.Label(root, text="Choisissez la devise:").grid(row=1, column=0, padx=10, pady=5)
    tk.Label(root, text="Nombre de jours de données historiques:").grid(row=2, column=0, padx=10, pady=5)
    tk.Label(root, text="Nombre de jours à prévoir:").grid(row=3, column=0, padx=10, pady=5)

    # Comboboxes
    coin_combobox = ttk.Combobox(root, textvariable=coin_var, values=['BTC', 'ETH', 'ADA'], state='readonly')
    coin_combobox.grid(row=0, column=1, padx=10, pady=5)

    currency_combobox = ttk.Combobox(root, textvariable=currency_var, values=['EUR', 'USD'], state='readonly')
    currency_combobox.grid(row=1, column=1, padx=10, pady=5)

    days_combobox = ttk.Combobox(root, textvariable=days_var, values=[str(i) for i in range(100, 1001, 100)], state='readonly')
    days_combobox.grid(row=2, column=1, padx=10, pady=5)

    days_future_combobox = ttk.Combobox(root, textvariable=days_future_var, values=[str(i) for i in range(1, 31)], state='readonly')
    days_future_combobox.grid(row=3, column=1, padx=10, pady=5)

    # Submit Button
    submit_button = tk.Button(root, text="Soumettre", command=on_submit)
    submit_button.grid(row=4, columnspan=2, pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
