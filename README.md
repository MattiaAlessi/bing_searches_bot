# Bing Rewards Automation Bot

The **Bing Rewards Automation Bot** is a simple and intuitive tool designed to automate Bing searches and maximize your **Microsoft Rewards** points.  
It uses a modern **CustomTkinter** GUI and simulates human-like typing and pauses to reduce the risk of detection.

## ✨ Key Features

**🔹 Human-like typing simulation**  
- Types characters with variable speed and random intervals.  
- Each search looks realistic and natural.  

**🔹 Customizable number of searches**  
- Users can enter the number of random searches directly in the GUI.  
- Queries are generated from the **NLTK English corpus**, combined with random typos.  

**🔹 Randomized pauses and delays**  
- Each action (opening tabs, typing, closing) includes random delays.  
- Mimics real user behavior and avoids repetitive patterns.  

**🔹 Interrupt functionality**  
- A dedicated **“Interrupt”** button allows stopping execution at any time.  
- Safe for the system and instantly responsive.  

**🔹 Real-time logging**  
- A log window shows all performed actions (search count, errors, completion).  
- Helps users monitor progress and troubleshoot issues.  

## 🖥️ How It Works

1. Launch the application.  
2. Enter the desired number of searches.  
3. Click **“Start Random Searches”** to begin automation.  
4. The bot opens Microsoft Edge and performs random searches, closing tabs afterward.  
5. You can stop the process anytime with the **“Interrupt”** button.   

## 📋 System Requirements

- **Operating System:** Windows  
- **Required Python libraries:**  
  - `pyautogui`  
  - `nltk`  
  - `customtkinter`  
- **Browser:** Microsoft Edge  

## ⚠️ Disclaimer

This bot is provided for **educational purposes only**.  
Its use may violate Microsoft’s Terms of Service and could result in account suspension.  
The author takes no responsibility for misuse.  
