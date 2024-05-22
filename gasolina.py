import pandas as pd

def main():
    df = pd.read_csv('gasolina.csv')
    df.rename(columns={'dia': 'Dia', 'venda': 'Preço'}, inplace=True)
    print(df.head())

if __name__ == "__main__":
    main()
df.head()
