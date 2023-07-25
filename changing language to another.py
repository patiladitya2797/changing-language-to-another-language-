#changing english language to marathi language
#for that selected the googletrans API
#"mr"code is for the marathi language


from googletrans import Translator
translator=Translator()
output=translator.translate("I LOVE MY COUNTRY",dest="mr")
print(output)