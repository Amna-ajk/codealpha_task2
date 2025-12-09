# import requests
# from tkinter import *
# import threading

# # ---------------------------------------------------------
# # 🔥 PASTE YOUR OPENROUTER API KEY HERE
# # ---------------------------------------------------------
# API_KEY = "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"   # <-- JUST REPLACE THIS

# # ---------------------------------------------------------
# # ChatGPT-Style API Call (Super Simple)
# # ---------------------------------------------------------
# def ask_openrouter(prompt):
#     url = "https://openrouter.ai/api/v1/chat/completions"
#     headers = {
#         "Authorization": f"Bearer {API_KEY}",
#         "Content-Type": "application/json"
#     }

#     data = {
#         "model": "anthropic/claude-instant-v1",
#         "messages": [
#             {"role": "system", "content": "You are a helpful FAQ + general chatbot."},
#             {"role": "user", "content": prompt}
#         ],
#         "max_tokens": 300
#     }

#     response = requests.post(url, headers=headers, json=data)
#     result = response.json()

#     try:
#         return result["choices"][0]["message"]["content"]
#     except:
#         return "Error: Could not understand response."

# # ---------------------------------------------------------
# # Tkinter UI
# # ---------------------------------------------------------
# def send_msg():
#     text = user_entry.get()
#     if text.strip() == "":
#         return
    
#     chat_box.insert(END, "You: " + text + "\n")
#     user_entry.delete(0, END)

#     chat_box.insert(END, "Bot is typing...\n")

#     def work():
#         reply = ask_openrouter(text)
#         chat_box.insert(END, "Bot: " + reply + "\n\n")
#         chat_box.see(END)

#     threading.Thread(target=work, daemon=True).start()

# root = Tk()
# root.title("AI Chatbot (OpenRouter)")
# root.geometry("500x600")

# chat_box = Text(root, font=("Arial", 12))
# chat_box.pack(fill=BOTH, expand=True)

# frame = Frame(root)
# frame.pack(pady=5)

# user_entry = Entry(frame, font=("Arial", 14), width=30)
# user_entry.pack(side=LEFT)

# send_btn = Button(frame, text="Send", command=send_msg)
# send_btn.pack(side=LEFT, padx=5)

# root.mainloop()


# import requests
# from tkinter import *
# import threading

# # ---------------------------------------------------------
# # 🔥 YOUR OPENROUTER API KEY
# # ---------------------------------------------------------
# API_KEY = "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"

# # ---------------------------------------------------------
# # Fixed API Call for OpenRouter
# # ---------------------------------------------------------
# def ask_openrouter(prompt):
#     url = "https://openrouter.ai/api/v1/chat/completions"
#     headers = {
#         "Authorization": f"Bearer {API_KEY}",
#         "HTTP-Referer": "http://localhost:3000",  # Required by OpenRouter
#         "X-Title": "My Chatbot"  # Optional but recommended
#     }

#     data = {
#         "model": "google/gemini-2.0-flash-exp:free",  # Using the model you mentioned
#         "messages": [
#             {"role": "user", "content": prompt}
#         ],
#         "max_tokens": 300
#     }

#     try:
#         response = requests.post(url, headers=headers, json=data, timeout=30)
#         result = response.json()
        
#         print(f"Response status: {response.status_code}")  # Debug print
        
#         # Check if we got a valid response
#         if response.status_code == 200:
#             if "choices" in result and len(result["choices"]) > 0:
#                 return result["choices"][0]["message"]["content"]
#             else:
#                 return f"Error: Unexpected response format. Response: {result}"
#         else:
#             return f"Error {response.status_code}: {result.get('error', {}).get('message', 'Unknown error')}"
            
#     except requests.exceptions.Timeout:
#         return "Error: Request timed out. Try again."
#     except requests.exceptions.ConnectionError:
#         return "Error: Connection failed. Check your internet."
#     except Exception as e:
#         return f"Error: {str(e)}"

# # ---------------------------------------------------------
# # Tkinter UI (unchanged)
# # ---------------------------------------------------------
# def send_msg():
#     text = user_entry.get()
#     if text.strip() == "":
#         return
    
#     chat_box.insert(END, "You: " + text + "\n")
#     user_entry.delete(0, END)

#     chat_box.insert(END, "Bot is typing...\n")

#     def work():
#         reply = ask_openrouter(text)
#         chat_box.insert(END, "Bot: " + reply + "\n\n")
#         chat_box.see(END)

#     threading.Thread(target=work, daemon=True).start()

# root = Tk()
# root.title("AI Chatbot (OpenRouter - Gemini 2.0 Flash Exp)")
# root.geometry("500x600")

# chat_box = Text(root, font=("Arial", 12))
# chat_box.pack(fill=BOTH, expand=True)

# frame = Frame(root)
# frame.pack(pady=5)

# user_entry = Entry(frame, font=("Arial", 14), width=30)
# user_entry.pack(side=LEFT)

# send_btn = Button(frame, text="Send", command=send_msg)
# send_btn.pack(side=LEFT, padx=5)

# root.mainloop()


# import requests
# from tkinter import *
# from tkinter import filedialog, messagebox
# import threading

# # ---------------------------------------------------------
# # 🔥 YOUR OPENROUTER API KEY
# # ---------------------------------------------------------
# API_KEY = "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"

# # ---------------------------------------------------------
# # API Call to OpenRouter
# # ---------------------------------------------------------
# def ask_openrouter(prompt):
#     url = "https://openrouter.ai/api/v1/chat/completions"
#     headers = {
#         "Authorization": f"Bearer {API_KEY}",
#         "HTTP-Referer": "http://localhost:3000",
#         "X-Title": "My Chatbot"
#     }
#     data = {
#         "model": "google/gemini-2.0-flash-exp:free",
#         "messages": [{"role": "user", "content": prompt}],
#         "max_tokens": 300
#     }

#     try:
#         response = requests.post(url, headers=headers, json=data, timeout=30)
#         result = response.json()
#         if response.status_code == 200:
#             if "choices" in result and len(result["choices"]) > 0:
#                 return result["choices"][0]["message"]["content"]
#             else:
#                 return f"Error: Unexpected response format. Response: {result}"
#         else:
#             return f"Error {response.status_code}: {result.get('error', {}).get('message', 'Unknown error')}"
#     except requests.exceptions.Timeout:
#         return "Error: Request timed out. Try again."
#     except requests.exceptions.ConnectionError:
#         return "Error: Connection failed. Check your internet."
#     except Exception as e:
#         return f"Error: {str(e)}"

# # ---------------------------------------------------------
# # Tkinter Chatbot UI
# # ---------------------------------------------------------
# root = Tk()
# root.title("AI Chatbot (OpenRouter - Gemini 2.0 Flash Exp)")
# root.geometry("600x700")
# root.configure(bg="#1E1E2F")

# # Default theme colors
# theme = {"bg": "#1E1E2F", "fg": "#FFFFFF", "user_bg": "#4A90E2", "bot_bg": "#E5E5EA", "entry_bg": "#2E2E3E"}

# # Chatbox with scrollbar
# chat_frame = Frame(root, bg=theme["bg"])
# chat_frame.pack(fill=BOTH, expand=True, padx=5, pady=5)

# scrollbar = Scrollbar(chat_frame)
# scrollbar.pack(side=RIGHT, fill=Y)

# chat_box = Text(chat_frame, font=("Arial", 12), bg=theme["bg"], fg=theme["fg"], 
#                 yscrollcommand=scrollbar.set, wrap=WORD, state=DISABLED, padx=10, pady=10)
# chat_box.pack(fill=BOTH, expand=True)
# scrollbar.config(command=chat_box.yview)

# # Tag config for WhatsApp-style chat bubbles
# chat_box.tag_config("user", foreground=theme["fg"], background=theme["user_bg"], 
#                     lmargin1=10, lmargin2=10, rmargin=50, spacing3=5, font=("Arial", 12, "bold"))
# chat_box.tag_config("bot", foreground="#000000", background=theme["bot_bg"], 
#                     lmargin1=50, lmargin2=10, rmargin=10, spacing3=5, font=("Arial", 12))

# # Entry and buttons
# frame = Frame(root, bg=theme["bg"])
# frame.pack(pady=5)

# user_entry = Entry(frame, font=("Arial", 14), width=35, bg=theme["entry_bg"], fg=theme["fg"], insertbackground="white")
# user_entry.pack(side=LEFT, padx=5)

# # ---------------- Chat Functions ----------------
# def insert_message(sender, msg):
#     chat_box.config(state=NORMAL)
#     if sender == "You":
#         chat_box.insert(END, f"{sender}: {msg}\n", "user")
#     else:
#         chat_box.insert(END, f"{sender}: {msg}\n", "bot")
#     chat_box.see(END)
#     chat_box.config(state=DISABLED)

# def send_msg(event=None):
#     text = user_entry.get()
#     if text.strip() == "":
#         return
#     insert_message("You", text)
#     user_entry.delete(0, END)

#     insert_message("Bot", "Typing...")

#     def work():
#         reply = ask_openrouter(text)
#         # Remove "Typing..." line
#         chat_box.config(state=NORMAL)
#         chat_box.delete("end-2l", "end-1l")
#         chat_box.config(state=DISABLED)
#         insert_message("Bot", reply)

#     threading.Thread(target=work, daemon=True).start()

# def clear_chat():
#     if messagebox.askyesno("Clear Chat", "Are you sure you want to clear the chat?"):
#         chat_box.config(state=NORMAL)
#         chat_box.delete("1.0", END)
#         chat_box.config(state=DISABLED)

# def save_chat():
#     file_path = filedialog.asksaveasfilename(defaultextension=".txt", 
#                                              filetypes=[("Text Files", "*.txt")])
#     if file_path:
#         with open(file_path, "w", encoding="utf-8") as f:
#             f.write(chat_box.get("1.0", END))
#         messagebox.showinfo("Saved", f"Chat saved to {file_path}")

# def toggle_theme():
#     if theme["bg"] == "#1E1E2F":
#         # Switch to light theme
#         theme.update({"bg": "#F0F0F0", "fg": "#000000", "user_bg": "#4A90E2", "bot_bg": "#E5E5EA", "entry_bg": "#FFFFFF"})
#     else:
#         # Switch back to dark
#         theme.update({"bg": "#1E1E2F", "fg": "#FFFFFF", "user_bg": "#4A90E2", "bot_bg": "#E5E5EA", "entry_bg": "#2E2E3E"})
#     # Update widgets
#     root.configure(bg=theme["bg"])
#     chat_frame.configure(bg=theme["bg"])
#     chat_box.configure(bg=theme["bg"], fg=theme["fg"])
#     frame.configure(bg=theme["bg"])
#     user_entry.configure(bg=theme["entry_bg"], fg=theme["fg"])
#     chat_box.tag_config("user", foreground=theme["fg"], background=theme["user_bg"])
#     chat_box.tag_config("bot", background=theme["bot_bg"])

# # ---------------- Buttons ----------------
# send_btn = Button(frame, text="Send", command=send_msg, bg="#4A90E2", fg="white")
# send_btn.pack(side=LEFT, padx=5)

# clear_btn = Button(root, text="Clear Chat", command=clear_chat, bg="#FF5C5C", fg="white")
# clear_btn.pack(side=LEFT, padx=5, pady=5)

# save_btn = Button(root, text="Save Chat", command=save_chat, bg="#4A90E2", fg="white")
# save_btn.pack(side=LEFT, padx=5, pady=5)

# theme_btn = Button(root, text="Toggle Theme", command=toggle_theme, bg="#9B59B6", fg="white")
# theme_btn.pack(side=LEFT, padx=5, pady=5)

# # Bind Enter key
# root.bind("<Return>", send_msg)

# # ---------------- Emojis Support ----------------
# emoji_frame = Frame(root, bg=theme["bg"])
# emoji_frame.pack(pady=5)

# emojis = ["😊", "🤖", "❤", "😂", "👍", "🔥"]
# for e in emojis:
#     btn = Button(emoji_frame, text=e, command=lambda em=e: user_entry.insert(END, em), bg=theme["bg"], fg="white", font=("Arial", 14))
#     btn.pack(side=LEFT, padx=2)

# root.mainloop()


# import requests
# from tkinter import *
# from tkinter import filedialog, messagebox
# import threading
# import time

# # ---------------------------------------------------------
# # 🔥 YOUR OPENROUTER API KEY
# # ---------------------------------------------------------
# API_KEY = "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"

# # ---------------------------------------------------------
# # API Call
# # ---------------------------------------------------------
# def ask_openrouter(prompt):
#     url = "https://openrouter.ai/api/v1/chat/completions"
#     headers = {
#         "Authorization": f"Bearer {API_KEY}",
#         "HTTP-Referer": "http://localhost:3000",
#         "X-Title": "Corporate Chatbot"
#     }
#     data = {
#         "model": "google/gemini-2.0-flash-exp:free",
#         "messages": [{"role": "user", "content": prompt}],
#         "max_tokens": 300
#     }
#     try:
#         response = requests.post(url, headers=headers, json=data, timeout=30)
#         result = response.json()
#         if response.status_code == 200:
#             if "choices" in result and len(result["choices"]) > 0:
#                 return result["choices"][0]["message"]["content"]
#             else:
#                 return f"Error: Unexpected response format."
#         else:
#             return f"Error {response.status_code}: {result.get('error', {}).get('message', 'Unknown error')}"
#     except:
#         return "Error: Could not reach server. Check your connection."

# # ---------------------------------------------------------
# # Main Window
# # ---------------------------------------------------------
# root = Tk()
# root.title("Corporate AI Chatbot")
# root.geometry("600x700")
# root.configure(bg="#F5F5F7")
# root.resizable(False, False)

# # Theme
# theme = {"bg": "#F5F5F7", "fg": "#000000", "user_bg": "#0B93F6", "bot_bg": "#E5E5EA", "entry_bg": "#FFFFFF"}

# # ---------------- Header ----------------
# header = Frame(root, bg="#0B93F6", height=50)
# header.pack(fill=X)
# Label(header, text="Corporate AI Chatbot", bg="#0B93F6", fg="white", font=("Helvetica", 16, "bold")).pack(pady=10)

# # ---------------- Chatbox ----------------
# chat_frame = Frame(root, bg=theme["bg"])
# chat_frame.pack(fill=BOTH, expand=True, padx=10, pady=(5,0))

# scrollbar = Scrollbar(chat_frame)
# scrollbar.pack(side=RIGHT, fill=Y)

# chat_box = Text(chat_frame, font=("Helvetica", 12), bg=theme["bg"], fg=theme["fg"], 
#                 yscrollcommand=scrollbar.set, wrap=WORD, state=DISABLED, padx=10, pady=10, bd=0)
# chat_box.pack(fill=BOTH, expand=True)
# scrollbar.config(command=chat_box.yview)

# chat_box.tag_config("user", foreground="white", background=theme["user_bg"], lmargin1=10, lmargin2=10, rmargin=50, spacing3=8, font=("Helvetica", 12), relief="raised")
# chat_box.tag_config("bot", foreground=theme["fg"], background=theme["bot_bg"], lmargin1=50, lmargin2=10, rmargin=10, spacing3=8, font=("Helvetica", 12), relief="raised")

# # ---------------- Entry & Buttons ----------------
# input_frame = Frame(root, bg=theme["bg"])
# input_frame.pack(fill=X, pady=5)

# user_entry = Entry(input_frame, font=("Helvetica", 14), bg=theme["entry_bg"], fg=theme["fg"], insertbackground=theme["fg"])
# user_entry.pack(side=LEFT, padx=10, pady=5, fill=X, expand=True)

# button_frame = Frame(root, bg=theme["bg"])
# button_frame.pack(fill=X, pady=5)

# def insert_message(sender, msg):
#     chat_box.config(state=NORMAL)
#     if sender=="You":
#         chat_box.insert(END, f"{msg}\n", "user")
#     else:
#         chat_box.insert(END, f"{msg}\n", "bot")
#     chat_box.see(END)
#     chat_box.config(state=DISABLED)

# def send_msg(event=None):
#     text = user_entry.get().strip()
#     if not text: return
#     insert_message("You", text)
#     user_entry.delete(0, END)
#     insert_message("Bot", "Typing...")

#     def work():
#         reply = ask_openrouter(text)
#         # Remove "Typing..."
#         chat_box.config(state=NORMAL)
#         chat_box.delete("end-2l", "end-1l")
#         chat_box.config(state=DISABLED)
#         insert_message("Bot", reply)
#     threading.Thread(target=work, daemon=True).start()

# def clear_chat():
#     if messagebox.askyesno("Clear Chat", "Are you sure you want to clear the chat?"):
#         chat_box.config(state=NORMAL)
#         chat_box.delete("1.0", END)
#         chat_box.config(state=DISABLED)

# def save_chat():
#     file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files","*.txt")])
#     if file_path:
#         with open(file_path,"w",encoding="utf-8") as f:
#             f.write(chat_box.get("1.0", END))
#         messagebox.showinfo("Saved", f"Chat saved to {file_path}")

# def toggle_theme():
#     if theme["bg"]=="#F5F5F7":
#         theme.update({"bg":"#1E1E2F","fg":"white","user_bg":"#0B93F6","bot_bg":"#2E2E3E","entry_bg":"#2E2E3E"})
#     else:
#         theme.update({"bg":"#F5F5F7","fg":"black","user_bg":"#0B93F6","bot_bg":"#E5E5EA","entry_bg":"#FFFFFF"})
#     root.configure(bg=theme["bg"])
#     chat_frame.configure(bg=theme["bg"])
#     chat_box.configure(bg=theme["bg"], fg=theme["fg"])
#     input_frame.configure(bg=theme["bg"])
#     user_entry.configure(bg=theme["entry_bg"], fg=theme["fg"])
#     button_frame.configure(bg=theme["bg"])
#     chat_box.tag_config("user", foreground="white", background=theme["user_bg"])
#     chat_box.tag_config("bot", background=theme["bot_bg"], foreground=theme["fg"])

# send_btn = Button(button_frame, text="Send", command=send_msg, bg="#0B93F6", fg="white", font=("Helvetica",12,"bold"))
# send_btn.pack(side=LEFT, padx=5)

# clear_btn = Button(button_frame, text="Clear", command=clear_chat, bg="#FF5C5C", fg="white", font=("Helvetica",12,"bold"))
# clear_btn.pack(side=LEFT, padx=5)

# save_btn = Button(button_frame, text="Save", command=save_chat, bg="#4CAF50", fg="white", font=("Helvetica",12,"bold"))
# save_btn.pack(side=LEFT, padx=5)

# theme_btn = Button(button_frame, text="Toggle Theme", command=toggle_theme, bg="#9B59B6", fg="white", font=("Helvetica",12,"bold"))
# theme_btn.pack(side=LEFT, padx=5)

# # ---------------- Emoji Panel ----------------
# emoji_frame = Frame(root, bg=theme["bg"])
# emoji_frame.pack(pady=5)
# emojis = ["😊","🤖","❤","😂","👍","🔥"]
# for e in emojis:
#     btn = Button(emoji_frame,text=e,command=lambda em=e:user_entry.insert(END,em), bg=theme["bg"], fg="black", font=("Helvetica",14), bd=0)
#     btn.pack(side=LEFT, padx=3)

# root.bind("<Return>", send_msg)
# root.mainloop()



# import requests
# import json
# from datetime import datetime
# from tkinter import *
# import tkinter.scrolledtext as st
# import threading
# from tkinter import font as tkfont
# import tkinter.messagebox as messagebox

# # ---------------------------------------------------------
# # 🔥 YOUR OPENROUTER API KEY
# # ---------------------------------------------------------
# API_KEY = "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"

# # ---------------------------------------------------------
# # OpenRouter API Call (Professional)
# # ---------------------------------------------------------
# def ask_openrouter(prompt):
#     """Professional API call with comprehensive error handling"""
#     url = "https://openrouter.ai/api/v1/chat/completions"
#     headers = {
#         "Authorization": f"Bearer {API_KEY}",
#         "HTTP-Referer": "https://corp-ai-chat.tech",  # Professional domain
#         "X-Title": "CorpAI Assistant v2.0",
#         "Content-Type": "application/json"
#     }

#     data = {
#         "model": "google/gemini-2.0-flash-exp:free",
#         "messages": [
#             {
#                 "role": "system", 
#                 "content": """You are CorpAI Assistant, a professional AI chatbot for American corporations. 
#                 You provide concise, accurate, and business-appropriate responses. 
#                 Format responses clearly with proper paragraphs. Be helpful, formal, and efficient."""
#             },
#             {"role": "user", "content": prompt}
#         ],
#         "max_tokens": 500,
#         "temperature": 0.7
#     }

#     try:
#         response = requests.post(url, headers=headers, json=data, timeout=45)
        
#         if response.status_code == 200:
#             result = response.json()
#             if "choices" in result and result["choices"]:
#                 return result["choices"][0]["message"]["content"]
#             else:
#                 return "⚠ Response format error. Please try again."
#         elif response.status_code == 401:
#             return "🔒 API Key Error: Invalid or expired credentials."
#         elif response.status_code == 429:
#             return "⏳ Rate limit exceeded. Please wait a moment."
#         else:
#             return f"⚠ API Error {response.status_code}. Please contact support."
            
#     except requests.exceptions.Timeout:
#         return "⏱ Request timeout. Server may be busy."
#     except requests.exceptions.ConnectionError:
#         return "🔌 Connection failed. Check your internet."
#     except Exception as e:
#         return f"⚠ System error: {str(e)}"

# # ---------------------------------------------------------
# # Professional Chat Bubble System
# # ---------------------------------------------------------
# class ChatBubble:
#     def _init_(self, parent, text, is_user=True, timestamp=None):
#         self.parent = parent
#         self.text = text
#         self.is_user = is_user
#         self.timestamp = timestamp or datetime.now().strftime("%I:%M %p")
        
#         self.create_bubble()
    
#     def create_bubble(self):
#         # Frame for bubble
#         bubble_frame = Frame(self.parent, bg="#f0f2f5")
#         bubble_frame.pack(fill=X, padx=10, pady=2)
        
#         # Timestamp (small, subtle)
#         time_label = Label(bubble_frame, text=self.timestamp, 
#                           font=("Segoe UI", 8), fg="#666666", bg="#f0f2f5")
#         time_label.pack(anchor="e" if self.is_user else "w")
        
#         # Main bubble container
#         container = Frame(bubble_frame, bg="#f0f2f5")
#         container.pack(fill=X)
        
#         if self.is_user:
#             # User bubble (Blue, aligned right)
#             bubble = Label(container, text=self.text, 
#                           font=("Segoe UI", 10),
#                           bg="#0084ff", fg="white",
#                           wraplength=350,
#                           justify=LEFT,
#                           padx=15, pady=8)
#             bubble.pack(anchor="e", padx=(100, 0))
            
#             # User avatar (simple circle)
#             avatar = Label(container, text="👤", font=("Arial", 14), 
#                           bg="#f0f2f5", fg="#0084ff")
#             avatar.pack(side=RIGHT, padx=(5, 0))
#         else:
#             # Bot bubble (Light gray, aligned left)
#             avatar = Label(container, text="🤖", font=("Arial", 14), 
#                           bg="#f0f2f5", fg="#25D366")
#             avatar.pack(side=LEFT, padx=(0, 5))
            
#             bubble = Label(container, text=self.text, 
#                           font=("Segoe UI", 10),
#                           bg="#ffffff", fg="#1c1e21",
#                           wraplength=350,
#                           justify=LEFT,
#                           padx=15, pady=8,
#                           relief="flat")
#             bubble.pack(anchor="w", padx=(0, 100))

# # ---------------------------------------------------------
# # Professional Chatbot Application
# # ---------------------------------------------------------
# class ProfessionalChatbot:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("CorpAI Assistant")
#         self.root.geometry("800x700")
#         self.root.configure(bg="#f0f2f5")
        
#         # Set professional colors
#         self.colors = {
#             "primary": "#1a73e8",  # Google Blue
#             "secondary": "#34a853",  # Google Green
#             "background": "#f0f2f5",
#             "card": "#ffffff",
#             "text": "#202124",
#             "text_light": "#5f6368"
#         }
        
#         self.setup_ui()
#         self.chat_history = []
        
#     def setup_ui(self):
#         # Header (Professional)
#         header_frame = Frame(self.root, bg=self.colors["primary"], height=60)
#         header_frame.pack(fill=X)
#         header_frame.pack_propagate(False)
        
#         # Logo and Title
#         logo_label = Label(header_frame, text="🤖", font=("Arial", 24), 
#                           bg=self.colors["primary"], fg="white")
#         logo_label.pack(side=LEFT, padx=(20, 10))
        
#         title_label = Label(header_frame, text="CorpAI Assistant", 
#                            font=("Segoe UI", 18, "bold"), 
#                            bg=self.colors["primary"], fg="white")
#         title_label.pack(side=LEFT, padx=5)
        
#         subtitle_label = Label(header_frame, text="Powered by OpenRouter AI", 
#                               font=("Segoe UI", 10), 
#                               bg=self.colors["primary"], fg="#e8f0fe")
#         subtitle_label.pack(side=LEFT, padx=5)
        
#         # Status indicator
#         self.status_label = Label(header_frame, text="● Online", 
#                                  font=("Segoe UI", 9), 
#                                  bg=self.colors["primary"], fg="#34a853")
#         self.status_label.pack(side=RIGHT, padx=20)
        
#         # Chat Container
#         chat_container = Frame(self.root, bg=self.colors["background"])
#         chat_container.pack(fill=BOTH, expand=True, padx=20, pady=10)
        
#         # Chat Display Area (Scrolled Text)
#         self.chat_display = Canvas(chat_container, bg=self.colors["background"], 
#                                   highlightthickness=0)
#         scrollbar = Scrollbar(chat_container, orient=VERTICAL, 
#                              command=self.chat_display.yview)
#         self.scrollable_frame = Frame(self.chat_display, bg=self.colors["background"])
        
#         self.scrollable_window = self.chat_display.create_window((0, 0), 
#                                                                  window=self.scrollable_frame, 
#                                                                  anchor="nw")
        
#         self.chat_display.configure(yscrollcommand=scrollbar.set)
#         self.chat_display.pack(side=LEFT, fill=BOTH, expand=True)
#         scrollbar.pack(side=RIGHT, fill=Y)
        
#         # Configure scrolling
#         self.scrollable_frame.bind("<Configure>", 
#             lambda e: self.chat_display.configure(
#                 scrollregion=self.chat_display.bbox("all")))
        
#         # Welcome message
#         self.add_welcome_message()
        
#         # Input Area
#         input_frame = Frame(self.root, bg=self.colors["card"], height=100)
#         input_frame.pack(fill=X, padx=20, pady=(0, 20))
        
#         # Input field with placeholder
#         self.input_var = StringVar()
#         self.input_entry = Entry(input_frame, 
#                                 textvariable=self.input_var,
#                                 font=("Segoe UI", 12),
#                                 bg="white",
#                                 fg=self.colors["text"],
#                                 relief="flat",
#                                 insertbackground=self.colors["primary"])
#         self.input_entry.pack(fill=X, padx=20, pady=15, ipady=8)
#         self.input_entry.bind("<Return>", lambda e: self.send_message())
#         self.input_entry.bind("<KeyRelease>", self.check_input)
        
#         # Placeholder text
#         self.placeholder_label = Label(input_frame, 
#                                       text="Type your message here...",
#                                       font=("Segoe UI", 12, "italic"),
#                                       bg="white",
#                                       fg="#9aa0a6")
#         self.placeholder_label.place(in_=self.input_entry, x=10, y=8)
        
#         # Button Container
#         button_frame = Frame(input_frame, bg=self.colors["card"])
#         button_frame.pack(fill=X, padx=20, pady=(0, 15))
        
#         # Send Button
#         self.send_btn = Button(button_frame, 
#                               text="Send Message →",
#                               command=self.send_message,
#                               font=("Segoe UI", 11, "bold"),
#                               bg=self.colors["primary"],
#                               fg="white",
#                               activebackground="#1557b0",
#                               activeforeground="white",
#                               relief="flat",
#                               padx=25,
#                               pady=8,
#                               cursor="hand2")
#         self.send_btn.pack(side=RIGHT)
#         self.send_btn.config(state=DISABLED)
        
#         # Clear Button
#         clear_btn = Button(button_frame,
#                           text="Clear Chat",
#                           command=self.clear_chat,
#                           font=("Segoe UI", 10),
#                           bg="#f1f3f4",
#                           fg=self.colors["text_light"],
#                           relief="flat",
#                           padx=15,
#                           pady=5,
#                           cursor="hand2")
#         clear_btn.pack(side=LEFT)
        
#         # Save Button
#         save_btn = Button(button_frame,
#                          text="Save Conversation",
#                          command=self.save_conversation,
#                          font=("Segoe UI", 10),
#                          bg="#f1f3f4",
#                          fg=self.colors["text_light"],
#                          relief="flat",
#                          padx=15,
#                          pady=5,
#                          cursor="hand2")
#         save_btn.pack(side=LEFT, padx=10)
        
#     def add_welcome_message(self):
#         """Add professional welcome message"""
#         welcome_frame = Frame(self.scrollable_frame, bg=self.colors["background"])
#         welcome_frame.pack(fill=X, pady=20)
        
#         welcome_card = Frame(welcome_frame, bg="white", relief="flat")
#         welcome_card.pack(padx=50)
        
#         Label(welcome_card, text="👋 Welcome to CorpAI Assistant", 
#               font=("Segoe UI", 14, "bold"), 
#               bg="white", fg=self.colors["text"]).pack(pady=(15, 5))
        
#         Label(welcome_card, 
#               text="I'm your professional AI assistant powered by Gemini 2.0 Flash.\nHow can I help you today?",
#               font=("Segoe UI", 11), 
#               bg="white", fg=self.colors["text_light"],
#               justify=CENTER).pack(pady=(0, 15))
        
#         # Quick tips
#         tips_frame = Frame(welcome_card, bg="#f8f9fa")
#         tips_frame.pack(fill=X, padx=15, pady=(0, 15))
        
#         tips = [
#             "💡 Ask about business strategies",
#             "📊 Request data analysis insights",
#             "✍ Get help with professional writing",
#             "🌐 Discuss market trends"
#         ]
        
#         for tip in tips:
#             Label(tips_frame, text=tip, 
#                   font=("Segoe UI", 9), 
#                   bg="#f8f9fa", fg=self.colors["text_light"]).pack(anchor="w", pady=2)
    
#     def check_input(self, event=None):
#         """Enable/disable send button based on input"""
#         text = self.input_var.get().strip()
#         if text:
#             self.send_btn.config(state=NORMAL)
#             self.placeholder_label.place_forget()
#         else:
#             self.send_btn.config(state=DISABLED)
#             self.placeholder_label.place(in_=self.input_entry, x=10, y=8)
    
#     def send_message(self):
#         """Send message to AI and display response"""
#         text = self.input_var.get().strip()
#         if not text:
#             return
        
#         # Clear input
#         self.input_var.set("")
#         self.check_input()
        
#         # Add user message bubble
#         ChatBubble(self.scrollable_frame, text, is_user=True)
#         self.chat_history.append(f"You: {text}")
        
#         # Update scroll
#         self.root.update_idletasks()
#         self.chat_display.yview_moveto(1)
        
#         # Disable send button during processing
#         self.send_btn.config(state=DISABLED, text="Thinking...")
#         self.status_label.config(text="● Processing", fg="#fbbc04")
        
#         # Process in thread
#         threading.Thread(target=self.process_response, args=(text,), daemon=True).start()
    
#     def process_response(self, user_text):
#         """Process AI response in background"""
#         try:
#             response = ask_openrouter(user_text)
            
#             # Add bot response bubble
#             self.root.after(0, self.add_bot_response, response)
            
#             # Update chat history
#             self.chat_history.append(f"Assistant: {response}")
            
#         except Exception as e:
#             error_msg = f"⚠ An error occurred: {str(e)}"
#             self.root.after(0, self.add_bot_response, error_msg)
    
#     def add_bot_response(self, response):
#         """Add bot response to chat (must be called from main thread)"""
#         ChatBubble(self.scrollable_frame, response, is_user=False)
        
#         # Reset UI
#         self.send_btn.config(state=NORMAL, text="Send Message →")
#         self.status_label.config(text="● Online", fg="#34a853")
        
#         # Scroll to bottom
#         self.root.update_idletasks()
#         self.chat_display.yview_moveto(1)
    
#     def clear_chat(self):
#         """Clear chat history"""
#         if messagebox.askyesno("Clear Chat", "Are you sure you want to clear the conversation?"):
#             # Destroy all chat bubbles
#             for widget in self.scrollable_frame.winfo_children():
#                 widget.destroy()
            
#             # Reset
#             self.chat_history = []
#             self.add_welcome_message()
    
#     def save_conversation(self):
#         """Save conversation to file"""
#         if not self.chat_history:
#             messagebox.showinfo("Save Conversation", "No conversation to save.")
#             return
        
#         timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
#         filename = f"chat_history_{timestamp}.txt"
        
#         try:
#             with open(filename, "w", encoding="utf-8") as f:
#                 f.write("=== CorpAI Assistant Conversation ===\n")
#                 f.write(f"Date: {datetime.now().strftime('%Y-%m-%d %I:%M %p')}\n")
#                 f.write("="*40 + "\n\n")
                
#                 for line in self.chat_history:
#                     f.write(line + "\n")
            
#             messagebox.showinfo("Success", f"Conversation saved to:\n{filename}")
#         except Exception as e:
#             messagebox.showerror("Error", f"Failed to save: {str(e)}")

# # ---------------------------------------------------------
# # Main Application
# # ---------------------------------------------------------
# if __name__ == "__main__":
#     root = Tk()
    
#     # Set professional icon (if available)
#     try:
#         root.iconbitmap(default='icon.ico')
#     except:
#         pass
    
#     app = ProfessionalChatbot(root)
#     root.mainloop()


# import requests
# import json
# from datetime import datetime
# from tkinter import *
# import threading
# import tkinter.messagebox as messagebox

# # ---------------------------------------------------------
# # 🔥 YOUR OPENROUTER API KEY
# # ---------------------------------------------------------
# API_KEY = "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"

# # ---------------------------------------------------------
# # DEBUG OpenRouter API Call
# # ---------------------------------------------------------
# def ask_openrouter(prompt):
#     """Debug API call to see what's happening"""
#     print(f"\n=== DEBUG: Sending request to OpenRouter ===")
#     print(f"Prompt: {prompt}")
    
#     url = "https://openrouter.ai/api/v1/chat/completions"
#     headers = {
#         "Authorization": f"Bearer {API_KEY}",
#         "HTTP-Referer": "https://localhost:3000",
#         "Content-Type": "application/json"
#     }

#     data = {
#         "model": "google/gemini-2.0-flash-exp:free",
#         "messages": [
#             {"role": "user", "content": prompt}
#         ],
#         "max_tokens": 300
#     }

#     try:
#         print(f"Sending request to: {url}")
#         print(f"Headers: {headers}")
#         print(f"Data: {json.dumps(data, indent=2)}")
        
#         response = requests.post(url, headers=headers, json=data, timeout=30)
        
#         print(f"\n=== DEBUG: Response received ===")
#         print(f"Status Code: {response.status_code}")
#         print(f"Response Headers: {dict(response.headers)}")
        
#         if response.status_code != 200:
#             print(f"Error response: {response.text}")
#             return f"❌ API Error {response.status_code}: {response.text}"
        
#         result = response.json()
#         print(f"Response JSON: {json.dumps(result, indent=2)}")
        
#         if "choices" in result and result["choices"]:
#             message = result["choices"][0]["message"]["content"]
#             print(f"Extracted message: {message[:100]}...")
#             return message
#         else:
#             print("No 'choices' in response")
#             return "⚠ No response from AI. Please try again."
            
#     except requests.exceptions.RequestException as e:
#         print(f"\n=== DEBUG: Request Exception ===")
#         print(f"Error: {str(e)}")
#         return f"🔌 Connection error: {str(e)}"
#     except Exception as e:
#         print(f"\n=== DEBUG: General Exception ===")
#         print(f"Error: {str(e)}")
#         return f"⚠ Error: {str(e)}"

# # ---------------------------------------------------------
# # SIMPLE Chatbot UI with Debug Info
# # ---------------------------------------------------------
# class SimpleChatbot:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Chatbot Debug")
#         self.root.geometry("700x600")
        
#         # Debug console
#         self.debug_text = Text(root, height=10, bg="black", fg="white", font=("Consolas", 9))
#         self.debug_text.pack(fill=X, padx=10, pady=5)
#         self.debug_text.insert(END, "=== Chatbot Debug Console ===\n")
        
#         # Chat display
#         self.chat_display = Text(root, height=20, font=("Arial", 11), wrap=WORD)
#         scrollbar = Scrollbar(root, command=self.chat_display.yview)
#         self.chat_display.config(yscrollcommand=scrollbar.set)
#         self.chat_display.pack(side=LEFT, fill=BOTH, expand=True, padx=(10, 0), pady=5)
#         scrollbar.pack(side=RIGHT, fill=Y, pady=5)
        
#         # Welcome message
#         self.chat_display.insert(END, "🤖 Welcome! Type a message and press Send.\n\n")
        
#         # Input area
#         input_frame = Frame(root)
#         input_frame.pack(fill=X, padx=10, pady=10)
        
#         self.input_entry = Entry(input_frame, font=("Arial", 12), width=50)
#         self.input_entry.pack(side=LEFT, padx=(0, 10))
#         self.input_entry.bind("<Return>", lambda e: self.send_message())
        
#         self.send_button = Button(input_frame, text="Send", command=self.send_message, 
#                                  font=("Arial", 11), bg="#4CAF50", fg="white")
#         self.send_button.pack(side=LEFT)
        
#         # Clear button
#         clear_button = Button(input_frame, text="Clear", command=self.clear_chat,
#                              font=("Arial", 11))
#         clear_button.pack(side=LEFT, padx=(10, 0))
        
#         # Test API button
#         test_button = Button(input_frame, text="Test API", command=self.test_api,
#                            font=("Arial", 11), bg="#2196F3", fg="white")
#         test_button.pack(side=LEFT, padx=(10, 0))
        
#     def log_debug(self, message):
#         """Add message to debug console"""
#         timestamp = datetime.now().strftime("%H:%M:%S")
#         self.debug_text.insert(END, f"[{timestamp}] {message}\n")
#         self.debug_text.see(END)
        
#     def send_message(self):
#         """Send message to AI"""
#         user_text = self.input_entry.get().strip()
#         if not user_text:
#             return
        
#         self.log_debug(f"User: {user_text}")
        
#         # Clear input
#         self.input_entry.delete(0, END)
        
#         # Display user message
#         self.chat_display.insert(END, f"👤 You: {user_text}\n")
#         self.chat_display.see(END)
        
#         # Show typing indicator
#         self.chat_display.insert(END, "🤖 Bot is thinking...\n")
#         self.chat_display.see(END)
        
#         # Disable send button
#         self.send_button.config(state=DISABLED, text="Processing...")
        
#         # Process in background
#         threading.Thread(target=self.get_response, args=(user_text,), daemon=True).start()
    
#     def get_response(self, user_text):
#         """Get response from API"""
#         try:
#             response = ask_openrouter(user_text)
            
#             # Update UI in main thread
#             self.root.after(0, self.display_response, response)
            
#         except Exception as e:
#             error_msg = f"Error in get_response: {str(e)}"
#             self.log_debug(error_msg)
#             self.root.after(0, self.display_response, f"⚠ {error_msg}")
    
#     def display_response(self, response):
#         """Display AI response"""
#         # Remove "thinking" message
#         self.chat_display.delete("end-2l", "end-1l")
        
#         # Display response
#         self.chat_display.insert(END, f"🤖 Bot: {response}\n\n")
#         self.chat_display.see(END)
        
#         # Re-enable send button
#         self.send_button.config(state=NORMAL, text="Send")
        
#         self.log_debug(f"Response displayed: {response[:50]}...")
    
#     def clear_chat(self):
#         """Clear chat display"""
#         self.chat_display.delete(1.0, END)
#         self.chat_display.insert(END, "🤖 Chat cleared. Type a new message.\n\n")
#         self.log_debug("Chat cleared")
    
#     def test_api(self):
#         """Test API connection"""
#         self.log_debug("Testing API connection...")
#         test_response = ask_openrouter("Hello, can you respond with 'API is working'?")
#         self.log_debug(f"Test result: {test_response}")

# # ---------------------------------------------------------
# # TEST API DIRECTLY First
# # ---------------------------------------------------------
# def test_api_directly():
#     """Test the API directly without GUI"""
#     print("=== Testing API directly ===")
#     print(f"API Key length: {len(API_KEY)}")
#     print(f"API Key first 10 chars: {API_KEY[:10]}...")
    
#     test_prompt = "Hello, are you working?"
    
#     try:
#         # Simple test
#         response = requests.post(
#             "https://openrouter.ai/api/v1/chat/completions",
#             headers={
#                 "Authorization": f"Bearer {API_KEY}",
#                 "HTTP-Referer": "https://localhost:3000"
#             },
#             json={
#                 "model": "google/gemini-2.0-flash-exp:free",
#                 "messages": [{"role": "user", "content": test_prompt}],
#                 "max_tokens": 100
#             },
#             timeout=10
#         )
        
#         print(f"Status Code: {response.status_code}")
#         print(f"Response: {response.text}")
        
#         if response.status_code == 200:
#             data = response.json()
#             if "choices" in data:
#                 print("✅ API is working!")
#                 print(f"Response: {data['choices'][0]['message']['content']}")
#                 return True
#             else:
#                 print("❌ Unexpected response format")
#                 return False
#         else:
#             print(f"❌ API Error: {response.status_code}")
#             return False
            
#     except Exception as e:
#         print(f"❌ Exception: {str(e)}")
#         return False

# # ---------------------------------------------------------
# # Main Application
# # ---------------------------------------------------------
# if __name__== "__main__":
#     print("=== Starting Chatbot ===")
    
#     # First test API directly
#     if not test_api_directly():
#         print("\n⚠ WARNING: API test failed. The chatbot may not work.")
#         print("Possible issues:")
#         print("1. API key is invalid or expired")
#         print("2. No internet connection")
#         print("3. OpenRouter service is down")
#         print("4. Rate limit exceeded")
    
#     input("\nPress Enter to continue to GUI...")
    
#     # Start GUI
#     root = Tk()
#     app = SimpleChatbot(root)
#     root.mainloop()

# import requests
# import threading
# from datetime import datetime
# from tkinter import *
# from tkinter import messagebox

# API_KEY = "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"

# def call_api(prompt):
#     try:
#         url = "https://openrouter.ai/api/v1/chat/completions"
#         headers = {
#             "Authorization": f"Bearer {API_KEY}",
#             "HTTP-Referer": "https://corporate-ai.tech",
#             "Content-Type": "application/json"
#         }
#         data = {
#             "model": "google/gemini-2.0-flash-exp:free",
#             "messages": [{"role": "user", "content": prompt}],
#             "max_tokens": 1000
#         }
#         response = requests.post(url, headers=headers, json=data, timeout=60)
#         if response.status_code == 200:
#             result = response.json()
#             return result["choices"][0]["message"]["content"]
#         return f"⚠ Error {response.status_code}"
#     except Exception as e:
#         return f"⚠ {str(e)}"

# class CorporateChatbot:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Corporate AI Assistant")
#         self.root.geometry("900x700")
        
#         self.dark_mode = False
#         self.themes = {
#             "light": {
#                 "bg": "#f8f9fa", "header_bg": "#1a73e8", "chat_bg": "#ffffff",
#                 "user_bg": "#0084ff", "bot_bg": "#f0f2f5", "input_bg": "white",
#                 "input_fg": "#202124", "button_bg": "#1a73e8", "sidebar_bg": "#ffffff",
#                 "border": "#dadce0", "bot_fg": "#1c1e21", "header_sub": "#e8f0fe"
#             },
#             "dark": {
#                 "bg": "#202124", "header_bg": "#0d47a1", "chat_bg": "#2d2e30",
#                 "user_bg": "#0084ff", "bot_bg": "#3c4043", "input_bg": "#3c4043",
#                 "input_fg": "#e8eaed", "button_bg": "#1a73e8", "sidebar_bg": "#2d2e30",
#                 "border": "#5f6368", "bot_fg": "#e8eaed", "header_sub": "#bbdefb"
#             }
#         }
#         self.current_theme = self.themes["light"]
#         self.conversation = []
#         self.setup_ui()
    
#     def setup_ui(self):
#         self.root.config(bg=self.current_theme["bg"])
#         self.create_header()
#         self.create_chat_area()
#         self.create_sidebar()
#         self.create_input()
#         self.create_emoji_panel()
#         self.setup_bindings()
    
#     def create_header(self):
#         header = Frame(self.root, bg=self.current_theme["header_bg"], height=60)
#         header.pack(fill=X)
#         logo = Frame(header, bg=self.current_theme["header_bg"])
#         logo.pack(side=LEFT, padx=20)
#         Label(logo, text="🤖", font=("Arial", 24), bg=self.current_theme["header_bg"], fg="white").pack(side=LEFT)
#         title = Frame(logo, bg=self.current_theme["header_bg"])
#         title.pack(side=LEFT, padx=10)
#         Label(title, text="Corporate AI Assistant", font=("Segoe UI", 16, "bold"), bg=self.current_theme["header_bg"], fg="white").pack()
#         Label(title, text="Powered by OpenRouter AI", font=("Segoe UI", 9), bg=self.current_theme["header_bg"], fg=self.current_theme["header_sub"]).pack()
#         status = Frame(header, bg=self.current_theme["header_bg"])
#         status.pack(side=RIGHT, padx=20)
#         self.status_label = Label(status, text="● Online", font=("Segoe UI", 10), bg=self.current_theme["header_bg"], fg="#34a853")
#         self.status_label.pack()
    
#     def create_chat_area(self):
#         main = Frame(self.root, bg=self.current_theme["bg"])
#         main.pack(fill=BOTH, expand=True, padx=20, pady=10)
#         container = Frame(main, bg=self.current_theme["border"])
#         container.pack(fill=BOTH, expand=True)
#         self.chat_display = Frame(container, bg=self.current_theme["chat_bg"])
#         self.chat_display.pack(fill=BOTH, expand=True, padx=1, pady=1)
#         self.chat_canvas = Canvas(self.chat_display, bg=self.current_theme["chat_bg"], highlightthickness=0)
#         self.scrollbar = Scrollbar(self.chat_display, orient="vertical", command=self.chat_canvas.yview)
#         self.chat_frame = Frame(self.chat_canvas, bg=self.current_theme["chat_bg"])
#         self.chat_window = self.chat_canvas.create_window((0, 0), window=self.chat_frame, anchor="nw")
#         self.chat_canvas.config(yscrollcommand=self.scrollbar.set)
#         self.chat_frame.bind("<Configure>", lambda e: self.chat_canvas.config(scrollregion=self.chat_canvas.bbox("all")))
#         self.scrollbar.pack(side=RIGHT, fill=Y)
#         self.chat_canvas.pack(side=LEFT, fill=BOTH, expand=True)
#         self.show_welcome()
    
#     def create_sidebar(self):
#         sidebar = Frame(self.root, bg=self.current_theme["sidebar_bg"], width=200)
#         sidebar.pack(side=RIGHT, fill=Y, padx=(0, 20), pady=10)
#         controls = Frame(sidebar, bg=self.current_theme["sidebar_bg"])
#         controls.pack(fill=BOTH, expand=True, padx=15, pady=15)
#         Label(controls, text="Controls", font=("Segoe UI", 14, "bold"), bg=self.current_theme["sidebar_bg"], fg=self.current_theme["input_fg"]).pack(pady=(0, 15))
#         self.theme_btn = Button(controls, text="🌙 Dark Mode", command=self.toggle_theme, font=("Segoe UI", 11), bg=self.current_theme["button_bg"], fg="white", relief="flat", padx=15, pady=8, cursor="hand2")
#         self.theme_btn.pack(fill=X, pady=5)
#         Button(controls, text="💾 Save Chat", command=self.save_chat, font=("Segoe UI", 11), bg=self.current_theme["button_bg"], fg="white", relief="flat", padx=15, pady=8, cursor="hand2").pack(fill=X, pady=5)
#         Button(controls, text="🗑 Clear Chat", command=self.clear_chat, font=("Segoe UI", 11), bg="#dc3545", fg="white", relief="flat", padx=15, pady=8, cursor="hand2").pack(fill=X, pady=5)
#         Button(controls, text="😊 Emoji", command=self.toggle_emoji, font=("Segoe UI", 11), bg=self.current_theme["button_bg"], fg="white", relief="flat", padx=15, pady=8, cursor="hand2").pack(fill=X, pady=5)
#         Frame(controls, height=1, bg=self.current_theme["border"]).pack(fill=X, pady=20)
#         self.stats_label = Label(controls, text="Messages: 0\nTokens: 0", font=("Segoe UI", 10), bg=self.current_theme["sidebar_bg"], fg=self.current_theme["input_fg"], justify=LEFT)
#         self.stats_label.pack(anchor="w")
    
#     def create_input(self):
#         input_frame = Frame(self.root, bg=self.current_theme["bg"], height=100)
#         input_frame.pack(fill=X, padx=20, pady=(0, 20))
#         container = Frame(input_frame, bg=self.current_theme["input_bg"], relief="solid", borderwidth=1)
#         container.pack(fill=BOTH, expand=True)
#         self.input_text = Text(container, font=("Segoe UI", 11), bg=self.current_theme["input_bg"], fg=self.current_theme["input_fg"], relief="flat", height=3, wrap=WORD)
#         self.input_text.pack(side=LEFT, fill=BOTH, expand=True, padx=10, pady=10)
#         self.input_text.bind("<Control-Return>", lambda e: self.send())
#         self.input_text.bind("<KeyRelease>", lambda e: self.update_send_button())
#         send_frame = Frame(container, bg=self.current_theme["input_bg"])
#         send_frame.pack(side=RIGHT, fill=Y, padx=(0, 10), pady=10)
#         self.send_btn = Button(send_frame, text="Send", command=self.send, font=("Segoe UI", 11, "bold"), bg=self.current_theme["button_bg"], fg="white", relief="flat", padx=20, pady=10, cursor="hand2", state=DISABLED)
#         self.send_btn.pack()
    
#     def create_emoji_panel(self):
#         self.emoji_panel = Frame(self.root, bg=self.current_theme["sidebar_bg"], relief="solid", borderwidth=1)
#         self.emoji_panel.place(x=20, y=600, width=350, height=120)
#         self.emoji_panel.place_forget()
#         emojis = ["😊","😂","🤔","👍","👎","🔥","🎉","❤","💡","📊","📈","📉","🔧","🚀","💼","💰","🌐","🔒","📝","🤖"]
#         for i in range(0, len(emojis), 5):
#             row = Frame(self.emoji_panel, bg=self.current_theme["sidebar_bg"])
#             row.pack(fill=X, pady=2)
#             for j in range(5):
#                 if i+j < len(emojis):
#                     emoji = emojis[i+j]
#                     Button(row, text=emoji, font=("Arial", 14), command=lambda e=emoji: self.add_emoji(e), bg=self.current_theme["sidebar_bg"], fg=self.current_theme["input_fg"], relief="flat", cursor="hand2").pack(side=LEFT, padx=2)
    
#     def setup_bindings(self):
#         self.root.bind("<Control-s>", lambda e: self.save_chat())
#         self.root.bind("<Control-l>", lambda e: self.toggle_theme())
#         self.root.bind("<Escape>", lambda e: self.hide_emoji())
    
#     def show_welcome(self):
#         welcome = Frame(self.chat_frame, bg=self.current_theme["chat_bg"])
#         welcome.pack(fill=X, pady=20)
#         card = Frame(welcome, bg=self.current_theme["bot_bg"], relief="flat", padx=20, pady=20)
#         card.pack(padx=40)
#         Label(card, text="🤖 Corporate AI Assistant", font=("Segoe UI", 14, "bold"), bg=self.current_theme["bot_bg"], fg=self.current_theme["bot_fg"]).pack()
#         Label(card, text="Professional AI for business needs", font=("Segoe UI", 11), bg=self.current_theme["bot_bg"], fg=self.current_theme["bot_fg"]).pack(pady=10)
    
#     def add_bubble(self, text, is_user):
#         frame = Frame(self.chat_frame, bg=self.current_theme["chat_bg"])
#         frame.pack(fill=X, padx=20, pady=5)
#         container = Frame(frame, bg=self.current_theme["chat_bg"])
#         container.pack(fill=X)
#         if is_user:
#             Label(container, text=text, font=("Segoe UI", 11), bg=self.current_theme["user_bg"], fg="white", wraplength=400, justify=LEFT, padx=15, pady=10).pack(side=RIGHT, padx=(50, 0))
#             Label(container, text="👤", font=("Arial", 14), bg=self.current_theme["chat_bg"], fg=self.current_theme["user_bg"]).pack(side=RIGHT, padx=5)
#         else:
#             Label(container, text="🤖", font=("Arial", 14), bg=self.current_theme["chat_bg"], fg=self.current_theme["button_bg"]).pack(side=LEFT, padx=5)
#             Label(container, text=text, font=("Segoe UI", 11), bg=self.current_theme["bot_bg"], fg=self.current_theme["bot_fg"], wraplength=400, justify=LEFT, padx=15, pady=10).pack(side=LEFT, padx=(0, 50))
    
#     def update_send_button(self):
#         text = self.input_text.get("1.0", "end-1c").strip()
#         self.send_btn.config(state=NORMAL if text else DISABLED)
    
#     def send(self):
#         msg = self.input_text.get("1.0", "end-1c").strip()
#         if not msg: return
#         self.input_text.delete("1.0", END)
#         self.update_send_button()
#         self.add_bubble(msg, True)
#         self.conversation.append(f"You: {msg}")
#         self.update_stats()
#         self.send_btn.config(state=DISABLED, text="Processing...")
#         self.status_label.config(text="● Processing", fg="#fbbc04")
#         typing = Frame(self.chat_frame, bg=self.current_theme["chat_bg"])
#         typing.pack(fill=X, padx=20, pady=5)
#         typing_label = Label(typing, text="🤖 AI is thinking...", font=("Segoe UI", 10, "italic"), bg=self.current_theme["chat_bg"], fg=self.current_theme["input_fg"])
#         typing_label.pack(anchor="w")
#         threading.Thread(target=self.get_response, args=(msg, typing_label), daemon=True).start()
    
#     def get_response(self, msg, typing_label):
#         try:
#             response = call_api(msg)
#             self.root.after(0, typing_label.destroy)
#             self.root.after(0, self.add_bubble, response, False)
#             self.conversation.append(f"Assistant: {response}")
#             self.root.after(0, self.update_stats)
#             self.root.after(0, self.after_response)
#         except Exception as e:
#             self.root.after(0, typing_label.destroy)
#             self.root.after(0, self.add_bubble, f"Error: {str(e)}", False)
#             self.root.after(0, self.after_response)
    
#     def after_response(self):
#         self.send_btn.config(state=NORMAL, text="Send")
#         self.status_label.config(text="● Online", fg="#34a853")
#         self.root.after(100, lambda: self.chat_canvas.yview_moveto(1.0))
    
#     def update_stats(self):
#         msgs = len(self.conversation)
#         tokens = sum(len(m)//4 for m in self.conversation)
#         self.stats_label.config(text=f"Messages: {msgs}\nTokens: {tokens}")
    
#     def add_emoji(self, emoji):
#         self.input_text.insert(INSERT, emoji)
#         self.input_text.focus()
    
#     def toggle_emoji(self):
#         if self.emoji_panel.winfo_ismapped():
#             self.hide_emoji()
#         else:
#             self.emoji_panel.place(x=20, y=600)
#             self.emoji_panel.lift()
    
#     def hide_emoji(self):
#         self.emoji_panel.place_forget()
    
#     def toggle_theme(self):
#         self.dark_mode = not self.dark_mode
#         self.current_theme = self.themes["dark" if self.dark_mode else "light"]
#         self.apply_theme()
    
#     def apply_theme(self):
#         self.root.config(bg=self.current_theme["bg"])
#         self.theme_btn.config(text="☀ Light Mode" if self.dark_mode else "🌙 Dark Mode")
#         self.chat_display.config(bg=self.current_theme["chat_bg"])
#         self.chat_canvas.config(bg=self.current_theme["chat_bg"])
#         self.chat_frame.config(bg=self.current_theme["chat_bg"])
#         self.input_text.config(bg=self.current_theme["input_bg"], fg=self.current_theme["input_fg"])
    
#     def clear_chat(self):
#         if not messagebox.askyesno("Clear Chat", "Clear conversation?"): return
#         for w in self.chat_frame.winfo_children(): w.destroy()
#         self.conversation.clear()
#         self.update_stats()
#         self.show_welcome()
    
#     def save_chat(self):
#         if not self.conversation:
#             messagebox.showinfo("Save", "No conversation to save.")
#             return
#         timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
#         filename = f"chat_{timestamp}.txt"
#         try:
#             with open(filename, "w", encoding="utf-8") as f:
#                 f.write("Corporate AI Assistant - Conversation\n")
#                 f.write(f"Date: {datetime.now().strftime('%Y-%m-%d %I:%M %p')}\n")
#                 f.write("="*50 + "\n\n")
#                 for msg in self.conversation: f.write(f"{msg}\n\n")
#             messagebox.showinfo("Success", f"Saved to:\n{filename}")
#         except Exception as e:
#             messagebox.showerror("Error", f"Save failed: {str(e)}")

# if __name__ == "__main__":
#     print("Starting Corporate AI Assistant...")
#     root = Tk()
#     CorporateChatbot(root)
#     root.mainloop()


# import requests
# import json
# import threading
# import os
# from datetime import datetime
# from tkinter import *
# from tkinter import messagebox

# # ==================== API FUNCTIONS ====================
# API_KEY = "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"

# def call_openrouter_api(prompt, system_prompt=None):
#     try:
#         url = "https://openrouter.ai/api/v1/chat/completions"

#         headers = {
#             "Authorization": f"Bearer {API_KEY}",
#             "Content-Type": "application/json",
#             "Referer": "https://corporate-ai.tech",
#             "X-Title": "Corporate AI Assistant"
#         }

#         messages = []
#         if system_prompt:
#             messages.append({"role": "system", "content": system_prompt})
#         messages.append({"role": "user", "content": prompt})

#         data = {
#             "model": "google/gemini-2.0-flash-exp",
#             "messages": messages,
#             "max_tokens": 1000,
#             "temperature": 0.7
#         }

#         response = requests.post(url, headers=headers, json=data, timeout=60)

#         if response.status_code == 200:
#             result = response.json()

#             try:
#                 return result["choices"][0]["message"]["content"]
#             except:
#                 return "⚠ Response format error."

#         elif response.status_code == 401:
#             return "🔒 Authentication error (Invalid API KEY)."

#         elif response.status_code == 429:
#             return "⏳ Rate limit exceeded. Try again later."

#         else:
#             return f"⚠ API Error {response.status_code}: {response.text}"

#     except requests.exceptions.Timeout:
#         return "⏱ Request timeout."

#     except requests.exceptions.ConnectionError:
#         return "🔌 Internet connection error."

#     except Exception as e:
#         return f"⚠ Error: {str(e)}"


# # ==================== CHAT BUBBLE CLASS ====================
# class ChatBubble:
#     def __init__(self, parent, message, is_user=True, theme=None):
#         self.parent = parent
#         self.message = message
#         self.is_user = is_user
#         self.theme = theme
#         self.create_bubble()

#     def create_bubble(self):
#         bubble_frame = Frame(self.parent, bg=self.theme["chat_bg"])
#         bubble_frame.pack(fill=X, padx=20, pady=5)

#         container = Frame(bubble_frame, bg=self.theme["chat_bg"])
#         container.pack(fill=X)

#         if self.is_user:
#             bubble = Label(
#                 container, text=self.message, font=("Segoe UI", 11),
#                 bg=self.theme["user_bubble_bg"], fg="white",
#                 wraplength=400, justify=LEFT, padx=15, pady=10
#             )
#             bubble.pack(side=RIGHT, padx=(50, 0))
#             Label(
#                 container, text="👤", font=("Arial", 14),
#                 bg=self.theme["chat_bg"], fg=self.theme["user_bubble_bg"]
#             ).pack(side=RIGHT, padx=5)

#         else:
#             Label(
#                 container, text="🤖", font=("Arial", 14),
#                 bg=self.theme["chat_bg"], fg=self.theme["button_bg"]
#             ).pack(side=LEFT, padx=5)

#             bubble = Label(
#                 container, text=self.message, font=("Segoe UI", 11),
#                 bg=self.theme["bot_bubble_bg"], fg=self.theme["bot_bubble_fg"],
#                 wraplength=400, justify=LEFT, padx=15, pady=10
#             )
#             bubble.pack(side=LEFT, padx=(0, 50))


# # ==================== MAIN CHATBOT CLASS ====================
# class CorporateChatbot:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Corporate AI Assistant")
#         self.root.geometry("900x700")

#         self.dark_mode = False
#         self.themes = self.setup_themes()
#         self.current_theme = self.themes["light"]

#         self.conversation_history = []
#         self.system_prompt = "You are a professional AI assistant for business environments."

#         self.setup_ui()

#     def setup_themes(self):
#         return {
#             "light": {
#                 "bg": "#f8f9fa",
#                 "header_bg": "#1a73e8",
#                 "header_fg": "white",
#                 "header_sub_fg": "#e8f0fe",
#                 "chat_bg": "#ffffff",
#                 "user_bubble_bg": "#0084ff",
#                 "user_bubble_fg": "white",
#                 "bot_bubble_bg": "#f0f2f5",
#                 "bot_bubble_fg": "#1c1e21",
#                 "input_bg": "white",
#                 "input_fg": "#202124",
#                 "button_bg": "#1a73e8",
#                 "button_fg": "white",
#                 "sidebar_bg": "#ffffff",
#                 "border": "#dadce0"
#             },
#             "dark": {
#                 "bg": "#202124",
#                 "header_bg": "#0d47a1",
#                 "header_fg": "white",
#                 "header_sub_fg": "#bbdefb",
#                 "chat_bg": "#2d2e30",
#                 "user_bubble_bg": "#0084ff",
#                 "user_bubble_fg": "white",
#                 "bot_bubble_bg": "#3c4043",
#                 "bot_bubble_fg": "#e8eaed",
#                 "input_bg": "#3c4043",
#                 "input_fg": "#e8eaed",
#                 "button_bg": "#1a73e8",
#                 "button_fg": "white",
#                 "sidebar_bg": "#2d2e30",
#                 "border": "#5f6368"
#             }
#         }

#     def setup_ui(self):
#         self.root.configure(bg=self.current_theme["bg"])
#         self.create_header()
#         self.create_main_content()
#         self.create_sidebar()
#         self.create_input_area()
#         self.create_emoji_panel()
#         self.setup_bindings()

#     def create_header(self):
#         header = Frame(self.root, bg=self.current_theme["header_bg"], height=60)
#         header.pack(fill=X)

#         logo_frame = Frame(header, bg=self.current_theme["header_bg"])
#         logo_frame.pack(side=LEFT, padx=20)

#         Label(
#             logo_frame, text="🤖", font=("Arial", 24),
#             bg=self.current_theme["header_bg"], fg="white"
#         ).pack(side=LEFT)

#         title_frame = Frame(logo_frame, bg=self.current_theme["header_bg"])
#         title_frame.pack(side=LEFT, padx=10)

#         Label(
#             title_frame, text="Corporate AI Assistant",
#             font=("Segoe UI", 16, "bold"),
#             bg=self.current_theme["header_bg"], fg="white"
#         ).pack()

#         Label(
#             title_frame, text="Powered by OpenRouter AI",
#             font=("Segoe UI", 9),
#             bg=self.current_theme["header_bg"], fg=self.current_theme["header_sub_fg"]
#         ).pack()

#         status_frame = Frame(header, bg=self.current_theme["header_bg"])
#         status_frame.pack(side=RIGHT, padx=20)

#         self.status_label = Label(
#             status_frame, text="● Online",
#             font=("Segoe UI", 10),
#             bg=self.current_theme["header_bg"], fg="#34a853"
#         )
#         self.status_label.pack()

#     def create_main_content(self):
#         main_frame = Frame(self.root, bg=self.current_theme["bg"])
#         main_frame.pack(fill=BOTH, expand=True, padx=20, pady=10)

#         chat_container = Frame(main_frame, bg=self.current_theme["border"])
#         chat_container.pack(fill=BOTH, expand=True)

#         self.chat_display_frame = Frame(chat_container, bg=self.current_theme["chat_bg"])
#         self.chat_display_frame.pack(fill=BOTH, expand=True, padx=1, pady=1)

#         self.chat_canvas = Canvas(
#             self.chat_display_frame, bg=self.current_theme["chat_bg"], highlightthickness=0
#         )
#         self.chat_scrollbar = Scrollbar(
#             self.chat_display_frame, orient="vertical", command=self.chat_canvas.yview
#         )

#         self.chat_inner_frame = Frame(self.chat_canvas, bg=self.current_theme["chat_bg"])
#         self.chat_window = self.chat_canvas.create_window(
#             (0, 0), window=self.chat_inner_frame, anchor="nw"
#         )

#         self.chat_canvas.configure(yscrollcommand=self.chat_scrollbar.set)
#         self.chat_inner_frame.bind("<Configure>", self.on_frame_configure)

#         self.chat_scrollbar.pack(side=RIGHT, fill=Y)
#         self.chat_canvas.pack(side=LEFT, fill=BOTH, expand=True)

#         self.show_welcome_message()

#     def create_sidebar(self):
#         sidebar = Frame(self.root, bg=self.current_theme["sidebar_bg"], width=200)
#         sidebar.pack(side=RIGHT, fill=Y, padx=(0, 20), pady=10)

#         control_frame = Frame(sidebar, bg=self.current_theme["sidebar_bg"])
#         control_frame.pack(fill=BOTH, expand=True, padx=15, pady=15)

#         Label(
#             control_frame, text="Controls", font=("Segoe UI", 14, "bold"),
#             bg=self.current_theme["sidebar_bg"], fg=self.current_theme["input_fg"]
#         ).pack(pady=(0, 15))

#         self.theme_btn = Button(
#             control_frame, text="🌙 Dark Mode",
#             command=self.toggle_theme,
#             font=("Segoe UI", 11),
#             bg=self.current_theme["button_bg"], fg="white",
#             relief="flat", padx=15, pady=8, cursor="hand2"
#         )
#         self.theme_btn.pack(fill=X, pady=5)

#         Button(
#             control_frame, text="💾 Save Chat",
#             command=self.save_conversation,
#             font=("Segoe UI", 11),
#             bg=self.current_theme["button_bg"], fg="white",
#             relief="flat", padx=15, pady=8, cursor="hand2"
#         ).pack(fill=X, pady=5)

#         Button(
#             control_frame, text="🗑 Clear Chat",
#             command=self.clear_chat,
#             font=("Segoe UI", 11),
#             bg="#dc3545", fg="white",
#             relief="flat", padx=15, pady=8, cursor="hand2"
#         ).pack(fill=X, pady=5)

#         Button(
#             control_frame, text="😊 Emoji",
#             command=self.toggle_emoji_panel,
#             font=("Segoe UI", 11),
#             bg=self.current_theme["button_bg"], fg="white",
#             relief="flat", padx=15, pady=8, cursor="hand2"
#         ).pack(fill=X, pady=5)

#         Frame(
#             control_frame, height=1, bg=self.current_theme["border"]
#         ).pack(fill=X, pady=20)

#         self.stats_label = Label(
#             control_frame, text="Messages: 0\nTokens: 0",
#             font=("Segoe UI", 10),
#             bg=self.current_theme["sidebar_bg"],
#             fg=self.current_theme["input_fg"],
#             justify=LEFT
#         )
#         self.stats_label.pack(anchor="w")

#     def create_input_area(self):
#         input_frame = Frame(self.root, bg=self.current_theme["bg"], height=100)
#         input_frame.pack(fill=X, padx=20, pady=(0, 20))

#         input_container = Frame(
#             input_frame, bg=self.current_theme["input_bg"], relief="solid", borderwidth=1
#         )
#         input_container.pack(fill=BOTH, expand=True)

#         self.input_text = Text(
#             input_container, font=("Segoe UI", 11),
#             bg=self.current_theme["input_bg"], fg=self.current_theme["input_fg"],
#             relief="flat", height=3, wrap=WORD
#         )
#         self.input_text.pack(side=LEFT, fill=BOTH, expand=True, padx=10, pady=10)
#         self.input_text.bind("<Control-Return>", lambda e: self.send_message())
#         self.input_text.bind("<KeyRelease>", self.on_input_change)

#         send_frame = Frame(input_container, bg=self.current_theme["input_bg"])
#         send_frame.pack(side=RIGHT, fill=Y, padx=(0, 10), pady=10)

#         self.send_btn = Button(
#             send_frame, text="Send", command=self.send_message,
#             font=("Segoe UI", 11, "bold"),
#             bg=self.current_theme["button_bg"], fg="white",
#             relief="flat", padx=20, pady=10, cursor="hand2",
#             state=DISABLED
#         )
#         self.send_btn.pack()

#     def create_emoji_panel(self):
#         self.emoji_panel = Frame(
#             self.root, bg=self.current_theme["sidebar_bg"],
#             relief="solid", borderwidth=1
#         )
#         self.emoji_panel.place(x=20, y=600, width=350, height=120)
#         self.emoji_panel.place_forget()

#         emojis = [
#             "😊", "😂", "🤔", "👍", "👎",
#             "🔥", "🎉", "❤", "💡", "📊",
#             "📈", "📉", "🔧", "🚀", "💼",
#             "💰", "🌐", "🔒", "📝", "🤖"
#         ]

#         for i in range(0, len(emojis), 5):
#             row_frame = Frame(self.emoji_panel, bg=self.current_theme["sidebar_bg"])
#             row_frame.pack(fill=X, pady=2)

#             for j in range(5):
#                 if i + j < len(emojis):
#                     emoji_char = emojis[i + j]
#                     Button(
#                         row_frame, text=emoji_char, font=("Arial", 14),
#                         command=lambda e=emoji_char: self.insert_emoji(e),
#                         bg=self.current_theme["sidebar_bg"],
#                         fg=self.current_theme["input_fg"],
#                         relief="flat", cursor="hand2"
#                     ).pack(side=LEFT, padx=2)

#     def setup_bindings(self):
#         self.root.bind("<Control-s>", lambda e: self.save_conversation())
#         self.root.bind("<Control-l>", lambda e: self.toggle_theme())
#         self.root.bind("<Escape>", lambda e: self.hide_emoji_panel())

#     def show_welcome_message(self):
#         welcome_frame = Frame(self.chat_inner_frame, bg=self.current_theme["chat_bg"])
#         welcome_frame.pack(fill=X, pady=20)

#         card = Frame(
#             welcome_frame, bg=self.current_theme["bot_bubble_bg"],
#             relief="flat", padx=20, pady=20
#         )
#         card.pack(padx=40)

#         Label(
#             card, text="🤖 Corporate AI Assistant",
#             font=("Segoe UI", 14, "bold"),
#             bg=self.current_theme["bot_bubble_bg"],
#             fg=self.current_theme["bot_bubble_fg"]
#         ).pack()

#         Label(
#             card, text="Professional AI for business needs",
#             font=("Segoe UI", 11),
#             bg=self.current_theme["bot_bubble_bg"],
#             fg=self.current_theme["bot_bubble_fg"]
#         ).pack(pady=10)

#     def on_frame_configure(self, event=None):
#         self.chat_canvas.configure(scrollregion=self.chat_canvas.bbox("all"))
#         self.chat_canvas.yview_moveto(1.0)

#     def on_input_change(self, event=None):
#         text = self.input_text.get("1.0", "end-1c").strip()
#         self.send_btn.config(state=NORMAL if text else DISABLED)

#     def send_message(self):
#         message = self.input_text.get("1.0", "end-1c").strip()
#         if not message:
#             return

#         self.input_text.delete("1.0", END)
#         self.on_input_change()

#         ChatBubble(self.chat_inner_frame, message, is_user=True, theme=self.current_theme)
#         self.conversation_history.append(f"You: {message}")
#         self.update_stats()

#         self.send_btn.config(state=DISABLED, text="Processing...")
#         self.status_label.config(text="● Processing", fg="#fbbc04")

#         typing_frame = Frame(self.chat_inner_frame, bg=self.current_theme["chat_bg"])
#         typing_frame.pack(fill=X, padx=20, pady=5)
#         typing_label = Label(
#             typing_frame, text="🤖 AI is thinking...",
#             font=("Segoe UI", 10, "italic"),
#             bg=self.current_theme["chat_bg"],
#             fg=self.current_theme["input_fg"]
#         )
#         typing_label.pack(anchor="w")

#         threading.Thread(
#             target=self.process_ai_response, args=(message, typing_label), daemon=True
#         ).start()

#     def process_ai_response(self, user_message, typing_label):
#         try:
#             response = call_openrouter_api(user_message, self.system_prompt)

#             self.root.after(0, typing_label.destroy)
#             self.root.after(0, ChatBubble, self.chat_inner_frame, response, False, self.current_theme)

#             self.conversation_history.append(f"Assistant: {response}")
#             self.root.after(0, self.update_stats)
#             self.root.after(0, self.enable_ui_after_response)

#         except Exception as e:
#             self.root.after(0, typing_label.destroy)
#             self.root.after(0, ChatBubble, self.chat_inner_frame, f"Error: {str(e)}", False, self.current_theme)
#             self.root.after(0, self.enable_ui_after_response)

#     def enable_ui_after_response(self):
#         self.send_btn.config(state=NORMAL, text="Send")
#         self.status_label.config(text="● Online", fg="#34a853")
#         self.root.after(100, self.scroll_to_bottom)

#     def scroll_to_bottom(self):
#         self.chat_canvas.yview_moveto(1.0)

#     def update_stats(self):
#         messages = len(self.conversation_history)
#         tokens = sum(len(msg) // 4 for msg in self.conversation_history)
#         self.stats_label.config(text=f"Messages: {messages}\nTokens: {tokens}")

#     def insert_emoji(self, emoji_char):
#         self.input_text.insert(INSERT, emoji_char)
#         self.input_text.focus()

#     def toggle_emoji_panel(self):
#         if self.emoji_panel.winfo_ismapped():
#             self.hide_emoji_panel()
#         else:
#             self.show_emoji_panel()

#     def show_emoji_panel(self):
#         self.emoji_panel.place(x=20, y=600)
#         self.emoji_panel.lift()

#     def hide_emoji_panel(self):
#         self.emoji_panel.place_forget()

#     def toggle_theme(self):
#         self.dark_mode = not self.dark_mode
#         self.current_theme = self.themes["dark" if self.dark_mode else "light"]
#         self.apply_theme()

#     def apply_theme(self):
#         self.root.config(bg=self.current_theme["bg"])
#         self.theme_btn.config(text="☀ Light Mode" if self.dark_mode else "🌙 Dark Mode")
#         self.chat_display_frame.config(bg=self.current_theme["chat_bg"])
#         self.chat_canvas.config(bg=self.current_theme["chat_bg"])
#         self.chat_inner_frame.config(bg=self.current_theme["chat_bg"])
#         self.input_text.config(bg=self.current_theme["input_bg"], fg=self.current_theme["input_fg"])

#     def clear_chat(self):
#         if not messagebox.askyesno("Clear Chat", "Clear conversation?"):
#             return

#         for widget in self.chat_inner_frame.winfo_children():
#             widget.destroy()

#         self.conversation_history.clear()
#         self.update_stats()
#         self.show_welcome_message()

#     def save_conversation(self):
#         if not self.conversation_history:
#             messagebox.showinfo("Save", "No conversation to save.")
#             return

#         timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
#         filename = f"chat_{timestamp}.txt"

#         try:
#             with open(filename, "w", encoding="utf-8") as f:
#                 f.write("Corporate AI Assistant - Conversation\n")
#                 f.write(f"Date: {datetime.now().strftime('%Y-%m-%d %I:%M %p')}\n")
#                 f.write("="*50 + "\n\n")

#                 for message in self.conversation_history:
#                     f.write(f"{message}\n\n")

#             messagebox.showinfo("Success", f"Saved to:\n{filename}")

#         except Exception as e:
#             messagebox.showerror("Error", f"Save failed: {str(e)}")


# # ==================== MAIN EXECUTION ====================
# if __name__ == "__main__":
#     print("Starting Corporate AI Assistant...")
#     root = Tk()
#     app = CorporateChatbot(root)
#     root.mainloop()



# import requests
# import threading
# from datetime import datetime
# from tkinter import *
# from tkinter import messagebox

# API_KEY = "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"

# def call_api(prompt):
#     """Call OpenRouter API with fallback models"""
#     try:
#         url = "https://openrouter.ai/api/v1/chat/completions"
#         headers = {
#             "Authorization": f"Bearer {API_KEY}",
#             "HTTP-Referer": "https://localhost:3000",
#             "Content-Type": "application/json"
#         }
        
#         # List of available models to try (most reliable first)
#         available_models = [
#             "openai/gpt-3.5-turbo",  # Most reliable
#             "meta-llama/llama-3.2-3b-instruct:free",  # Free
#             "google/gemini-2.0-flash",  # Try without :free
#             "google/gemini-flash",
#             "anthropic/claude-3-haiku"
#         ]
        
#         for model in available_models:
#             try:
#                 print(f"Trying model: {model}")
#                 data = {
#                     "model": model,
#                     "messages": [{"role": "user", "content": prompt}],
#                     "max_tokens": 300
#                 }
                
#                 response = requests.post(url, headers=headers, json=data, timeout=30)
                
#                 if response.status_code == 200:
#                     result = response.json()
#                     if "choices" in result and result["choices"]:
#                         print(f"✅ Success with model: {model}")
#                         return result["choices"][0]["message"]["content"]
#                     else:
#                         print(f"❌ No choices in response for {model}")
#                 else:
#                     print(f"❌ Model {model} failed with status {response.status_code}")
#                     if response.status_code == 429:
#                         print("Rate limited, trying next model...")
                    
#             except Exception as e:
#                 print(f"❌ Error with model {model}: {str(e)[:50]}")
#                 continue
        
#         return "⚠ All models failed. Please check your API key or try again later."
            
#     except Exception as e:
#         print(f"❌ Connection error: {str(e)}")
#         return f"⚠ Error: {str(e)}"

# class WorkingChatbot:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("AI Assistant")
#         self.root.geometry("850x650")
        
#         # Test API first
#         print("Testing API connection...")
#         test_response = call_api("Hello")
#         print(f"Test result: {test_response[:50]}...")
        
#         # Colors
#         self.colors = {
#             "bg": "#f0f2f5",
#             "header_bg": "#1a73e8",
#             "user_bubble": "#0084ff",
#             "bot_bubble": "#ffffff",
#             "input_bg": "white",
#             "button_bg": "#1a73e8"
#         }
        
#         self.conversation = []
#         self.setup_ui()
    
#     def setup_ui(self):
#         # Configure window
#         self.root.config(bg=self.colors["bg"])
        
#         # Create header
#         self.create_header()
        
#         # Create chat area
#         self.create_chat_area()
        
#         # Create input area
#         self.create_input_area()
        
#         # Add welcome message
#         self.add_message("🤖 Hello! I'm your AI assistant. How can I help you?", False)
    
#     def create_header(self):
#         header = Frame(self.root, bg=self.colors["header_bg"], height=60)
#         header.pack(fill=X)
        
#         # Logo and title
#         Label(header, text="🤖", font=("Arial", 24), 
#               bg=self.colors["header_bg"], fg="white").pack(side=LEFT, padx=20)
        
#         title_frame = Frame(header, bg=self.colors["header_bg"])
#         title_frame.pack(side=LEFT)
        
#         Label(title_frame, text="AI Assistant", 
#               font=("Segoe UI", 18, "bold"), 
#               bg=self.colors["header_bg"], fg="white").pack()
        
#         Label(title_frame, text="Powered by OpenRouter", 
#               font=("Segoe UI", 9), 
#               bg=self.colors["header_bg"], fg="#e8f0fe").pack()
        
#         # Status
#         status_frame = Frame(header, bg=self.colors["header_bg"])
#         status_frame.pack(side=RIGHT, padx=20)
        
#         self.status_label = Label(status_frame, text="● Online", 
#                                  font=("Segoe UI", 10), 
#                                  bg=self.colors["header_bg"], fg="#34a853")
#         self.status_label.pack()
    
#     def create_chat_area(self):
#         # Main container
#         main_frame = Frame(self.root, bg=self.colors["bg"])
#         main_frame.pack(fill=BOTH, expand=True, padx=20, pady=10)
        
#         # Chat container
#         chat_container = Frame(main_frame, bg="#dadce0")
#         chat_container.pack(fill=BOTH, expand=True)
        
#         # Chat display
#         self.chat_display = Frame(chat_container, bg="white")
#         self.chat_display.pack(fill=BOTH, expand=True, padx=1, pady=1)
        
#         # Canvas for scrolling
#         self.canvas = Canvas(self.chat_display, bg="white", highlightthickness=0)
#         scrollbar = Scrollbar(self.chat_display, orient="vertical", command=self.canvas.yview)
        
#         self.scrollable_frame = Frame(self.canvas, bg="white")
        
#         self.scrollable_frame.bind(
#             "<Configure>",
#             lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
#         )
        
#         self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
#         self.canvas.configure(yscrollcommand=scrollbar.set)
        
#         scrollbar.pack(side=RIGHT, fill=Y)
#         self.canvas.pack(side=LEFT, fill=BOTH, expand=True)
    
#     def create_input_area(self):
#         input_frame = Frame(self.root, bg=self.colors["bg"], height=80)
#         input_frame.pack(fill=X, padx=20, pady=(0, 20))
        
#         # Input container
#         input_container = Frame(input_frame, bg="white", relief="solid", borderwidth=1)
#         input_container.pack(fill=BOTH, expand=True)
        
#         # Text input
#         self.input_field = Entry(input_container, 
#                                 font=("Segoe UI", 12),
#                                 bg="white",
#                                 relief="flat")
#         self.input_field.pack(side=LEFT, fill=BOTH, expand=True, padx=15, pady=15)
#         self.input_field.bind("<Return>", lambda e: self.send_message())
        
#         # Send button
#         send_frame = Frame(input_container, bg="white")
#         send_frame.pack(side=RIGHT, fill=Y, padx=(0, 15), pady=15)
        
#         self.send_btn = Button(send_frame, 
#                               text="Send",
#                               command=self.send_message,
#                               font=("Segoe UI", 11, "bold"),
#                               bg=self.colors["button_bg"],
#                               fg="white",
#                               relief="flat",
#                               padx=25,
#                               pady=10,
#                               cursor="hand2")
#         self.send_btn.pack()
    
#     def add_message(self, text, is_user):
#         """Add a message bubble to chat"""
#         bubble_frame = Frame(self.scrollable_frame, bg="white")
#         bubble_frame.pack(fill=X, padx=20, pady=5)
        
#         container = Frame(bubble_frame, bg="white")
#         container.pack(fill=X)
        
#         if is_user:
#             # User message (right side)
#             bubble = Label(container, text=text, 
#                           font=("Segoe UI", 11),
#                           bg=self.colors["user_bubble"],
#                           fg="white",
#                           wraplength=350,
#                           justify=LEFT,
#                           padx=15, pady=10)
#             bubble.pack(side=RIGHT, padx=(50, 0))
            
#             Label(container, text="👤", font=("Arial", 14), 
#                   bg="white", fg=self.colors["user_bubble"]).pack(side=RIGHT, padx=5)
#         else:
#             # Bot message (left side)
#             Label(container, text="🤖", font=("Arial", 14), 
#                   bg="white", fg=self.colors["button_bg"]).pack(side=LEFT, padx=5)
            
#             bubble = Label(container, text=text, 
#                           font=("Segoe UI", 11),
#                           bg=self.colors["bot_bubble"],
#                           fg="black",
#                           wraplength=350,
#                           justify=LEFT,
#                           padx=15, pady=10)
#             bubble.pack(side=LEFT, padx=(0, 50))
        
#         # Auto scroll to bottom
#         self.canvas.yview_moveto(1.0)
    
#     def send_message(self):
#         """Send user message and get AI response"""
#         msg = self.input_field.get().strip()
#         if not msg:
#             return
        
#         # Clear input
#         self.input_field.delete(0, END)
        
#         # Add user message
#         self.add_message(msg, True)
#         self.conversation.append(f"You: {msg}")
        
#         # Show typing indicator
#         typing_frame = Frame(self.scrollable_frame, bg="white")
#         typing_frame.pack(fill=X, padx=20, pady=5)
#         typing_label = Label(typing_frame, text="🤖 Thinking...", 
#                            font=("Segoe UI", 10, "italic"),
#                            bg="white", fg="gray")
#         typing_label.pack(anchor="w")
        
#         # Update UI state
#         self.send_btn.config(state=DISABLED, text="Processing...")
#         self.status_label.config(text="● Processing", fg="#fbbc04")
        
#         # Get response in background thread
#         threading.Thread(target=self.get_ai_response, 
#                         args=(msg, typing_label), 
#                         daemon=True).start()
    
#     def get_ai_response(self, user_message, typing_label):
#         """Get response from AI in background thread"""
#         try:
#             response = call_api(user_message)
            
#             # Update UI in main thread
#             self.root.after(0, typing_label.destroy)
#             self.root.after(0, self.add_message, response, False)
#             self.conversation.append(f"AI: {response}")
#             self.root.after(0, self.restore_ui_state)
            
#         except Exception as e:
#             error_msg = f"Error: {str(e)}"
#             self.root.after(0, typing_label.destroy)
#             self.root.after(0, self.add_message, error_msg, False)
#             self.root.after(0, self.restore_ui_state)
    
#     def restore_ui_state(self):
#         """Restore UI after response"""
#         self.send_btn.config(state=NORMAL, text="Send")
#         self.status_label.config(text="● Online", fg="#34a853")

# if __name__ == "__main__":
#     print("="*60)
#     print("Starting AI Assistant...")
#     print("="*60)
    
#     root = Tk()
#     app = WorkingChatbot(root)
#     root.mainloop()


import requests, threading, os
from datetime import datetime
from tkinter import *
from tkinter import messagebox

# API_KEY = "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"

def api_call(prompt):
    try:
        url = "https://openrouter.ai/api/v1/chat/completions"
        headers = {
            "Authorization": f"Bearer {API_KEY}",
            "HTTP-Referer": "https://localhost:3000",
            "Content-Type": "application/json"
        }
        data = {
            "model": "openai/gpt-3.5-turbo",
            "messages": [{"role": "user", "content": prompt}],
            "max_tokens": 500
        }
        response = requests.post(url, headers=headers, json=data, timeout=30)
        if response.status_code == 200:
            return response.json()["choices"][0]["message"]["content"]
        return f"⚠ Error {response.status_code}"
    except:
        return "⚠ Connection failed"

class ChatBot:
    def __init__(self, root):
        self.root = root
        self.root.title("AI Assistant")
        self.root.geometry("900x700")
        self.dark = False
        self.chat = []
        
        # Themes
        self.light_theme = {
            "bg": "#f0f2f5", "header": "#1a73e8", "chat": "white",
            "user": "#0084ff", "bot": "#ffffff", "bot_text": "#1c1e21",
            "input": "white", "input_fg": "#202124", "btn": "#1a73e8",
            "sidebar": "white", "border": "#dadce0", "sub": "#e8f0fe"
        }
        self.dark_theme = {
            "bg": "#0d1117", "header": "#0d47a1", "chat": "#161b22",
            "user": "#0084ff", "bot": "#21262d", "bot_text": "#f0f6fc",
            "input": "#21262d", "input_fg": "#f0f6fc", "btn": "#1a73e8",
            "sidebar": "#161b22", "border": "#30363d", "sub": "#8b949e"
        }
        self.colors = self.light_theme
        
        self.build_ui()
        self.test_connection()
    
    def build_ui(self):
        self.root.config(bg=self.colors["bg"])
        self.make_header()
        self.make_chat()
        self.make_sidebar()
        self.make_input()
        self.make_emoji()
        self.setup_keys()
        self.show_welcome()
    
    def make_header(self):
        h = Frame(self.root, bg=self.colors["header"], height=70)
        h.pack(fill=X)
        
        left = Frame(h, bg=self.colors["header"])
        left.pack(side=LEFT, padx=20)
        Label(left, text="🤖", font=("Arial", 28), bg=self.colors["header"], fg="white").pack(side=LEFT)
        
        title = Frame(left, bg=self.colors["header"])
        title.pack(side=LEFT, padx=10)
        Label(title, text="AI Assistant", font=("Segoe UI", 18, "bold"), bg=self.colors["header"], fg="white").pack()
        Label(title, text="Powered by OpenRouter", font=("Segoe UI", 10), bg=self.colors["header"], fg=self.colors["sub"]).pack()
        
        right = Frame(h, bg=self.colors["header"])
        right.pack(side=RIGHT, padx=20)
        self.status = Label(right, text="● Online", font=("Segoe UI", 10), bg=self.colors["header"], fg="#34a853")
        self.status.pack()
    
    def make_chat(self):
        main = Frame(self.root, bg=self.colors["bg"])
        main.pack(fill=BOTH, expand=True, padx=20, pady=10)
        
        container = Frame(main, bg=self.colors["border"])
        container.pack(fill=BOTH, expand=True)
        
        self.chat_display = Frame(container, bg=self.colors["chat"])
        self.chat_display.pack(fill=BOTH, expand=True, padx=1, pady=1)
        
        self.canvas = Canvas(self.chat_display, bg=self.colors["chat"], highlightthickness=0)
        self.scroll = Scrollbar(self.chat_display, command=self.canvas.yview)
        
        self.chat_area = Frame(self.canvas, bg=self.colors["chat"])
        self.window = self.canvas.create_window((0, 0), window=self.chat_area, anchor="nw")
        
        self.canvas.config(yscrollcommand=self.scroll.set)
        self.chat_area.bind("<Configure>", lambda e: self.canvas.config(scrollregion=self.canvas.bbox("all")))
        
        self.scroll.pack(side=RIGHT, fill=Y)
        self.canvas.pack(side=LEFT, fill=BOTH, expand=True)
    
    def make_sidebar(self):
        sidebar = Frame(self.root, bg=self.colors["sidebar"], width=180)
        sidebar.pack(side=RIGHT, fill=Y, padx=(0, 20), pady=10)
        
        ctrl = Frame(sidebar, bg=self.colors["sidebar"])
        ctrl.pack(fill=BOTH, expand=True, padx=15, pady=15)
        
        Label(ctrl, text="Controls", font=("Segoe UI", 14, "bold"), bg=self.colors["sidebar"], fg=self.colors["input_fg"]).pack(pady=(0, 15))
        
        self.theme_btn = Button(ctrl, text="🌙 Dark Mode", command=self.switch_theme, font=("Segoe UI", 11), bg=self.colors["btn"], fg="white", relief="flat", cursor="hand2")
        self.theme_btn.pack(fill=X, pady=5)
        
        Button(ctrl, text="💾 Save Chat", command=self.save, font=("Segoe UI", 11), bg=self.colors["btn"], fg="white", relief="flat", cursor="hand2").pack(fill=X, pady=5)
        
        Button(ctrl, text="🗑 Clear Chat", command=self.clear, font=("Segoe UI", 11), bg="#dc3545", fg="white", relief="flat", cursor="hand2").pack(fill=X, pady=5)
        
        Button(ctrl, text="😊 Emoji", command=self.toggle_emoji, font=("Segoe UI", 11), bg=self.colors["btn"], fg="white", relief="flat", cursor="hand2").pack(fill=X, pady=5)
        
        Frame(ctrl, height=1, bg=self.colors["border"]).pack(fill=X, pady=20)
        
        self.stats = Label(ctrl, text="Messages: 0", font=("Segoe UI", 10), bg=self.colors["sidebar"], fg=self.colors["input_fg"], justify=LEFT)
        self.stats.pack(anchor="w")
    
    def make_input(self):
        inp = Frame(self.root, bg=self.colors["bg"], height=90)
        inp.pack(fill=X, padx=20, pady=(0, 20))
        
        box = Frame(inp, bg=self.colors["input"], relief="solid", borderwidth=1)
        box.pack(fill=BOTH, expand=True)
        
        self.entry = Entry(box, font=("Segoe UI", 12), bg=self.colors["input"], fg=self.colors["input_fg"], relief="flat")
        self.entry.pack(side=LEFT, fill=BOTH, expand=True, padx=15, pady=15)
        
        btn_frame = Frame(box, bg=self.colors["input"])
        btn_frame.pack(side=RIGHT, fill=Y, padx=(0, 15), pady=15)
        
        self.send_btn = Button(btn_frame, text="Send", command=self.send, font=("Segoe UI", 11, "bold"), bg=self.colors["btn"], fg="white", relief="flat", padx=25, pady=10, cursor="hand2")
        self.send_btn.pack()
    
    def make_emoji(self):
        self.emoji_box = Frame(self.root, bg=self.colors["sidebar"], relief="solid", borderwidth=1)
        self.emoji_box.place(x=20, y=600, width=350, height=120)
        self.emoji_box.place_forget()
        
        emojis = ["😊", "😂", "🤔", "👍", "👎", "🔥", "🎉", "❤", "💡", "📊", "📈", "📉", "🔧", "🚀", "💼", "💰", "🌐", "🔒", "📝", "🤖"]
        
        for i in range(0, len(emojis), 5):
            row = Frame(self.emoji_box, bg=self.colors["sidebar"])
            row.pack(fill=X, pady=2)
            for j in range(5):
                if i+j < len(emojis):
                    e = emojis[i+j]
                    Button(row, text=e, font=("Arial", 16), command=lambda x=e: self.add_emoji(x), bg=self.colors["sidebar"], fg=self.colors["input_fg"], relief="flat", cursor="hand2").pack(side=LEFT, padx=2)
    
    def setup_keys(self):
        self.root.bind("<Return>", lambda e: self.send())
        self.root.bind("<Control-s>", lambda e: self.save())
        self.root.bind("<Control-l>", lambda e: self.switch_theme())
        self.root.bind("<Escape>", lambda e: self.emoji_box.place_forget())
        self.entry.focus()
    
    def show_welcome(self):
        w = Frame(self.chat_area, bg=self.colors["chat"])
        w.pack(fill=X, pady=30)
        card = Frame(w, bg=self.colors["bot"], relief="flat", padx=20, pady=20)
        card.pack(padx=40)
        Label(card, text="🤖 AI Assistant", font=("Segoe UI", 14, "bold"), bg=self.colors["bot"], fg=self.colors["bot_text"]).pack()
        Label(card, text="Type a message and press Enter", font=("Segoe UI", 11), bg=self.colors["bot"], fg=self.colors["bot_text"]).pack(pady=10)
    
    def add_bubble(self, text, user=True):
        f = Frame(self.chat_area, bg=self.colors["chat"])
        f.pack(fill=X, padx=20, pady=5)
        c = Frame(f, bg=self.colors["chat"])
        c.pack(fill=X)
        
        if user:
            Label(c, text=text, font=("Segoe UI", 11), bg=self.colors["user"], fg="white", wraplength=350, justify=LEFT, padx=15, pady=10).pack(side=RIGHT, padx=(50, 0))
            Label(c, text="👤", font=("Arial", 14), bg=self.colors["chat"], fg=self.colors["user"]).pack(side=RIGHT, padx=5)
        else:
            Label(c, text="🤖", font=("Arial", 14), bg=self.colors["chat"], fg=self.colors["btn"]).pack(side=LEFT, padx=5)
            Label(c, text=text, font=("Segoe UI", 11), bg=self.colors["bot"], fg=self.colors["bot_text"], wraplength=350, justify=LEFT, padx=15, pady=10).pack(side=LEFT, padx=(0, 50))
        
        self.canvas.yview_moveto(1.0)
    
    def send(self):
        msg = self.entry.get().strip()
        if not msg: return
        
        self.entry.delete(0, END)
        self.add_bubble(msg, True)
        self.chat.append(f"You: {msg}")
        self.update_stats()
        
        self.send_btn.config(state=DISABLED, text="...")
        self.status.config(text="● Thinking", fg="#fbbc04")
        
        t = Frame(self.chat_area, bg=self.colors["chat"])
        t.pack(fill=X, padx=20, pady=5)
        tl = Label(t, text="🤖 Thinking...", font=("Segoe UI", 10, "italic"), bg=self.colors["chat"], fg="gray")
        tl.pack(anchor="w")
        
        threading.Thread(target=self.get_response, args=(msg, tl), daemon=True).start()
    
    def get_response(self, msg, tl):
        try:
            r = api_call(msg)
            self.root.after(0, tl.destroy)
            self.root.after(0, self.add_bubble, r, False)
            self.chat.append(f"AI: {r}")
            self.root.after(0, self.update_stats)
            self.root.after(0, self.reset_ui)
        except:
            self.root.after(0, tl.destroy)
            self.root.after(0, self.add_bubble, "⚠ Error", False)
            self.root.after(0, self.reset_ui)
    
    def reset_ui(self):
        self.send_btn.config(state=NORMAL, text="Send")
        self.status.config(text="● Online", fg="#34a853")
    
    def update_stats(self):
        self.stats.config(text=f"Messages: {len(self.chat)}")
    
    def add_emoji(self, e):
        self.entry.insert(END, e)
        self.entry.focus()
    
    def toggle_emoji(self):
        if self.emoji_box.winfo_ismapped():
            self.emoji_box.place_forget()
        else:
            self.emoji_box.place(x=20, y=600)
            self.emoji_box.lift()
    
    def switch_theme(self):
        self.dark = not self.dark
        self.colors = self.dark_theme if self.dark else self.light_theme
        self.apply_theme()
    
    def apply_theme(self):
        self.root.config(bg=self.colors["bg"])
        self.theme_btn.config(text="☀ Light" if self.dark else "🌙 Dark")
        self.chat_display.config(bg=self.colors["chat"])
        self.canvas.config(bg=self.colors["chat"])
        self.chat_area.config(bg=self.colors["chat"])
        self.entry.config(bg=self.colors["input"], fg=self.colors["input_fg"])
    
    def clear(self):
        if not messagebox.askyesno("Clear", "Clear chat?"): return
        for w in self.chat_area.winfo_children(): w.destroy()
        self.chat.clear()
        self.update_stats()
        self.show_welcome()
    
    def save(self):
        if not self.chat:
            messagebox.showinfo("Save", "No chat to save")
            return
        name = f"chat_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        try:
            with open(name, "w", encoding="utf-8") as f:
                f.write(f"Chat Log - {datetime.now()}\n")
                f.write("="*40 + "\n")
                for m in self.chat: f.write(m + "\n\n")
            messagebox.showinfo("Saved", f"Saved to {name}")
        except:
            messagebox.showerror("Error", "Save failed")
    
    def test_connection(self):
        print("Testing API...")
        r = api_call("Hello")
        print(f"Result: {r[:30]}...")

if __name__ == "__main__":
    print("Starting chatbot...")
    root = Tk()
    ChatBot(root)
    root.mainloop()