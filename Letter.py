Letter ='''Dear <|Name|>,

        You are selected!

         <|Date|>'''

Name=input("Entr Your Name: ")
Date= input("Enter Date: ")
Letter=Letter.replace("<|Name|>",Name)
Letter=Letter.replace("<|Date|>",Date)
print(Letter)