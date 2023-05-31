from translate import Translator
# Installed using pip install translate

trans_lang = ['fr', 'ja', 'ar']

def TranslatePhrase():

    text = input("What text would you like to translate: ")

    with open('translate.txt', 'w', encoding='utf-8') as file:
        for i in trans_lang:
            translator = Translator(from_lang='en', to_lang=i)
            translation = translator.translate(text)
            file.write(f"{i}: {translation}\n")

TranslatePhrase()
