from header import *
a = []
class file_ext(object):
    def input_file(in_file):
        f  = open (in_file , 'r')
        temp = [f.read()]
        x = "".join(temp)
        x = x.replace('\n',' ').replace(',','').replace('.','').split(' ')
        f.close()
        return x
    def output_file(out_file , x):
        f  = open (out_file , 'w')
        f.write(x)
        f.close()

class translation(file_ext) :
    def translate_words (x):
            translator = Translator()
            for i in x :
               translator = Translator()
               translations = translator.translate(str(i) ,dest = 'ar')
               a.append(str(translations.text))
               print( '  [' + str(i)+ ']  Have Been --------> Seccussfully Transated !')
            return a
    def Remove(duplicate): 
        final_list = [] 
        for num in duplicate: 
            if num not in final_list: 
                final_list.append(num) 
        return final_list 
            