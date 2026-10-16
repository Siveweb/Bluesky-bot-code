import time
from deep_translator import GoogleTranslator

TARGET_LANGS = [
    "en", "zh-CN", "zh-TW", "ko", "es", "fr", "de", "it", "pt", "ru", 
    "id", "th", "vi", "uk", "tr", "sv", "pl", "ro", "nl", "fi", 
    "el", "cs", "da", "hu", "km", "hi", "ne", "ca", "gl", "eu", 
    "ast", "ga", "an", "ia", "cy", "gd", "eo", "fy"
]

def expand_ng_list():
    
    try:
        with open("ng_words.txt", "r", encoding="utf-8") as f:
            base_words = [line.strip() for line in f if line.strip() and not line.strip().startswith("#")]
    except FileNotFoundError:
        print("エラー: ng_words.txt が見つかりません。")
        return

    print(f"元データ: {len(base_words)} 件の日本語NGワードを読み込みました。")
    
    all_ng_words = set(base_words)

    for lang in TARGET_LANGS:
        print(f"[{lang}] への自動翻訳を開始中...")
        translator = GoogleTranslator(source='ja', target=lang)
        count = 0
        
        for word in base_words:
          
            if len(word) <= 1 or word.isdigit():
                continue
                
            try:
                translated = translator.translate(word)
                if translated:
                    clean_word = translated.strip().lower()
                    all_ng_words.add(clean_word)
                    count += 1
            except Exception as e:
              
                pass

        print(f"  -> [{lang}] で {count} 件のNGワードを追加しました。")

  
    with open("ng_words.txt", "w", encoding="utf-8") as f:
        f.write("# --- 自動拡張された多言語NGワードリスト ---\n")
        for item in sorted(list(all_ng_words)):
            f.write(item + "\n")

    print("--------------------------------------------------")
    print(f"【完了】合計 {len(all_ng_words)} 件の多言語NGワードが ng_words.txt に登録されました！")

if __name__ == "__main__":
    expand_ng_list()
