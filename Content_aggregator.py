import requests
import tkinter as tk
from tkinter import ttk
from tkinter import *

root = tk.Tk()
root.title("News Aggregator")
root.geometry("600x600")   

API_KEY = '824aa7931d3e41439a6e555e593352fb'
BASE_URL = 'https://newsapi.org/v2/everything'

def fetch_news():
    keyword = keyword_entry.get()
    params = {
        'q': keyword,
        'language': 'en',
        'apiKey': API_KEY
    }

    response = requests.get(BASE_URL, params=params)
    data = response.json()

    if data['status'] == 'ok':
        news_text.delete(1.0, tk.END)  # Clear existing text in Text widget
        articles = data['articles']
        for index, article in enumerate(articles, start=1):
            title = article['title']
            source = article['source']['name']
            description = article['description']
            url = article['url']
            
            news_text.insert(tk.END, f"Article {index}:\n")
            news_text.insert(tk.END, f"Source: {source}\n")
            news_text.insert(tk.END, f"Title: {title}\n")
            news_text.insert(tk.END, f"Description: {description}\n")
            news_text.insert(tk.END, f"URL: {url}\n\n")
    else:
        news_text.delete(1.0, tk.END)  # Clear existing text
        news_text.insert(tk.END, "Failed to fetch news. Check your API key or parameters.")  

keyword_label = tk.Label(root, text="Enter a keyword:")
keyword_label.pack(pady=10)

keyword_entry = tk.Entry(root)
keyword_entry.pack(pady=5)

fetch_button = tk.Button(root, text="Fetch News", command=fetch_news)
fetch_button.pack()

news_text = tk.Text(root, wrap="word", height=15, width=70)
news_text.pack(pady=10)

root.mainloop()
