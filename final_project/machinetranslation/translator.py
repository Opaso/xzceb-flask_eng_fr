import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey= os.environ['apikey']
url= os.environ['url']
VERSION= '2018-05-01'
authenticator= IAMAuthenticator(apikey)
language_translator= LanguageTranslatorV3(version=VERSION, authenticator=authenticator)

language_translator.set_service_url(url)

def englishToFrench(english_text):
    french_translation= language_translator.translate(text= english_text, model_id= 'en-fr')
    result= french_translation.get_result()
    french_text= result['translations'][0]['translation']
    return french_text

def frenchToEnglish(french_text):
    english_translation= language_translator.translate(text= french_text, model_id= 'fr-en')
    result= english_translation.get_result()
    english_text= result['translations'][0]['translation']
    return english_text
