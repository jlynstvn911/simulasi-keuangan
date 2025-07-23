import yfinance as yf
import time
import pandas as pd

def get_stock_price(ticker_symbol):
    try:
        stock = yf.Ticker(ticker_symbol)

        # Ambil data selama 5 hari terakhir, jaga-jaga kalau 1 hari kosong
        hist = stock.history(period="5d")

        if hist.empty:
            print(f"Tidak ada data untuk {ticker_symbol}. Coba lagi nanti.")
            return

        latest_close = hist['Close'].dropna().iloc[-1]
        print(f"Harga penutupan terakhir {ticker_symbol}: {latest_close:.2f}")
    
    except Exception as e:
        print(f"Terjadi error: {e}")
        print("Mungkin kamu kena rate-limit dari Yahoo. Coba lagi nanti.")

# Jalankan loop manual biar bisa pakai berkali-kali
while True:
    ticker = input("\nMasukkan kode saham (atau ketik 'exit' untuk keluar): ").upper()
    if ticker == 'EXIT':
        print("Keluar dari program.")
        break

    get_stock_price(ticker)

    # Delay ringan biar tidak diblokir Yahoo
    time.sleep(2)