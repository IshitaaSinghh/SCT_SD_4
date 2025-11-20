import requests
from bs4 import BeautifulSoup
import csv
import tkinter as tk
from tkinter import messagebox

def scrape():
    url = entry_url.get().strip()

    if not url:
        messagebox.showerror("Error", "Please enter a URL.")
        return

    try:
        response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
        soup = BeautifulSoup(response.text, "html.parser")

        name = soup.find("h1").text.strip()
        price = soup.find("p", class_="price_color").text.strip()
        rating = soup.find("p", class_="star-rating")["class"][1]

        with open("products.csv", "a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow([name, price, rating])

        result_label.config(
            text=f"✓ Scraped Successfully!\n\nName: {name}\nPrice: {price}\nRating: {rating}"
        )

    except Exception as e:
        messagebox.showerror("Error", f"Failed to scrape the website.\n\n{e}")

root = tk.Tk()
root.title("Product Web Scraper - SkillCraft Technology")
root.geometry("500x300")

title_label = tk.Label(root, text="Enter product page URL:", font=("Arial", 14))
title_label.pack(pady=10)

entry_url = tk.Entry(root, width=50, font=("Arial", 12))
entry_url.pack(pady=5)

scrape_button = tk.Button(root, text="Scrape Product", font=("Arial", 14), command=scrape)
scrape_button.pack(pady=15)

result_label = tk.Label(root, text="", font=("Arial", 12), justify="left")
result_label.pack(pady=10)

root.mainloop()