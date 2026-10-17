# Bluesky-bot-code

### ⚠️ Note: This Markov chain bot template is strictly for Bluesky! It cannot be used on X (Twitter).

**Prerequisites before using these bot files:**

First, retrieve these two keys from Bluesky:
* **`BSKY_HANDLE`** (Your username)
* **`BSKY_PASSWORD`** (Your App Password)

> **How to get an App Password:**
> Go to the menu (three lines) → **Settings** → **Privacy and security** → **App passwords**.

Make sure to copy and save both keys in a notepad app.

---

### Setup Instructions

1. Create a new repository on GitHub.
   Go to **Settings** → **Secrets and variables** → **Actions**.
   Add the two secrets you saved earlier:
   * **`BSKY_HANDLE`**
   * **`BSKY_PASSWORD`**
   *(Please make sure the names/keys are typed exactly as shown, without any mistakes!)*

2. Download or copy the following files and add them to your newly created GitHub repository:
   * **`ng_words.txt`**
   * **`bot.py`**
   * **`expand_ng.py`**
   * **`requirements.txt`**
   * **`processed_posts.txt`**  
   *(Make sure the file names match exactly!)*

   *Words such as major incidents and accidents have already been written in some languages in ng_wards.txt. If there are other words that are at risk of account freezing in Bluesky's terms of use, please add them each time.*
   
   **In addition, we recommend that words that may freeze accounts correspond not only to the native language, but also to all languages supported by Bluesky.**
     
   * For **`bot/.github/workflows/main.yml.txt`**, rename it to **`main.yml`** (place it under `.github/workflows/main.yml`).

***Feel free to change the hashtags in the hashtag-repost section to whatever you like!***  

In addition, ng_wards.txt supports  
**Japanese**  
**English**  
**Chinese (Simplified)**  
**Chinese (Traditional)**  
**Korean**  
**Spanish**  
**French**  
**German**  
**Italian**  
**Portuguese**  
**Russian**  
**Swedish**  
**Polish**  
**Romanian**  
**Dutch**  
**Finnish**  
**Greek**  
**Czech**  
**Danish**  
**Hungarian**  
**Cambodian**  
**Hindi**  
**Nepali**  

*We plan to adapt it to Bluesky's corresponding language in order.*  

---

### About the files in this repository

* You are free to use these files for personal use without giving credit or mentioning me. Please use them responsibly and lawfully.
* **Do NOT make `ng_words.txt` public.** Sharing it publicly may put your account at risk of being suspended.
