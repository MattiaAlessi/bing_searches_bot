import tkinter as tk
from tkinter import scrolledtext
import customtkinter as ctk
import threading
import pyautogui
import time
import random
import nltk
from nltk.corpus import words
import os
import sys
import json

# Variabile globale per controllare l'esecuzione
execution_active = False



# Funzione per generare pause casuali
def sleep_random(min_time=1, max_time=3):
    time.sleep(random.uniform(min_time, max_time))


# Funzione per eseguire le ricerche casuali per l'account principale con errori di scrittura
def perform_random_searches_main_account():
    global execution_active
    execution_active = True
    interrupt_button.configure(state=tk.NORMAL)
    log_text.insert(tk.END, "Starting random searches for the main account...\n")

    def operations():
        try:
            nltk.download('words')

            def generate_random_words(num_words):
                dictionary = words.words()
                random_words = random.sample(dictionary, num_words * 3)  # Generates three times the necessary words
                return [" ".join(pairs[:3]) for pairs in zip(random_words[::3], random_words[1::3], random_words[2::3])]  # Combines in groups of 3

            def introduce_typo(word):
                """ Introduce a random typo into a word """
                if len(word) <= 2:
                    return word

                typo_type = random.choice(["swap", "delete", "replace"])
                index = random.randint(0, len(word) - 2)

                if typo_type == "swap":
                    word_list = list(word)
                    word_list[index], word_list[index + 1] = word_list[index + 1], word_list[index]
                    return "".join(word_list)
                elif typo_type == "delete":
                    return word[:index] + word[index + 1:]
                elif typo_type == "replace":
                    replacement = random.choice("abcdefghijklmnopqrstuvwxyz")
                    return word[:index] + replacement + word[index + 1:]

            def generate_queries_with_typos(queries):
                """ Introduce random typos into 2 or 3 words per sentence """
                modified_queries = []
                for query in queries:
                    words_in_query = query.split()
                    typo_count = random.randint(2, 3)
                    typo_indices = random.sample(range(len(words_in_query)), typo_count)
                    for i in typo_indices:
                        words_in_query[i] = introduce_typo(words_in_query[i])
                    modified_queries.append(" ".join(words_in_query))
                return modified_queries

            try:
                num_searches = int(searches_entry.get())
                if num_searches <= 0:
                    log_text.insert(tk.END, "Enter a valid number of searches.\n")
                    return
            except ValueError:
                log_text.insert(tk.END, "Enter a valid number of searches.\n")
                return

            random_queries = generate_random_words(num_searches)
            random_queries_with_typos = generate_queries_with_typos(random_queries)

            pyautogui.hotkey('win', 'r')
            sleep_random(1, 2)  # Usa la funzione globale sleep_random
            pyautogui.write('msedge')
            pyautogui.press('enter')
            sleep_random(3, 5)  # Usa la funzione globale sleep_random

            for i, query in enumerate(random_queries_with_typos):
                if not execution_active:
                    break
                log_text.insert(tk.END, f"Search number: {i+1} for the main account\n")

                pyautogui.hotkey('ctrl', 't')
                sleep_random(1, 2)  # Usa la funzione globale sleep_random

                for word in query.split():
                    pyautogui.write(word, interval=random.uniform(0.1, 0.2))
                    pyautogui.press('space')
                    sleep_random(0.3, 0.6)  # Usa la funzione globale sleep_random

                pyautogui.press('enter')
                sleep_random(3, 5)  # Usa la funzione globale sleep_random
                pyautogui.hotkey("ctrl", "w")
                sleep_random(1, 2)  # Usa la funzione globale sleep_random

            log_text.insert(tk.END, "Random searches completed for the main account.\n")
            pyautogui.hotkey('alt', 'f4')

        except Exception as e:
            log_text.insert(tk.END, f"Error during random searches: {e}\n")

        finally:
            interrupt_button.configure(state=tk.DISABLED)

    threading.Thread(target=operations).start()

# Funzione per interrompere l'esecuzione
def stop_execution():
    global execution_active
    execution_active = False
    log_text.insert(tk.END, "Execution interrupted by the user.\n")
    interrupt_button.configure(state=tk.DISABLED)

# Configurazione di CustomTkinter
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("dark-blue")

# Creazione della finestra principale
root = ctk.CTk()
root.title("Bing Rewards Automation")
root.geometry("900x700")

# Frame principale
main_frame = ctk.CTkFrame(root, corner_radius=15)
main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

# Titolo dell'applicazione
title_label = ctk.CTkLabel(main_frame, text="Bing Searches", font=("Arial", 24, "bold"))
title_label.pack(pady=20)

# Campo di input per il numero di ricerche
searches_label = ctk.CTkLabel(main_frame, text="Number of searches:", font=("Arial", 14))
searches_label.pack(pady=5)
searches_entry = ctk.CTkEntry(main_frame, width=300, font=("Arial", 14))
searches_entry.pack(pady=10)

# Pulsante per avviare le ricerche casuali sull'account principale
random_searches_main_button = ctk.CTkButton(
    main_frame,
    text="Start Random Searches (Main Account)",
    command=perform_random_searches_main_account,
    font=("Arial", 16),
    width=200,
    height=40
)
random_searches_main_button.pack(pady=10)

# Pulsante per interrompere il programma
interrupt_button = ctk.CTkButton(
    main_frame,
    text="Interrupt",
    command=stop_execution,
    font=("Arial", 16),
    width=200,
    height=40,
    state=tk.DISABLED
)
interrupt_button.pack(pady=10)

# Area di testo per i log
log_text = scrolledtext.ScrolledText(main_frame, wrap=tk.WORD, width=80, height=20, font=("Arial", 12))
log_text.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

# Avvio della GUI
root.mainloop()