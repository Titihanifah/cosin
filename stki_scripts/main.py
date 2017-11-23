"""
author rochanaph
October 23 2017"""

import w3,w4,w5, os

def main():
    path = './text files'
    this_path = os.path.split(__file__)[0]
    path = os.path.join(this_path, path)

    # membaca sekaligus pre-processing semua artikel simpan ke dictionary
    articles = {}
    for item in os.listdir(path):
        if item.endswith(".txt"):
            with open(path + "/" + item, 'r') as file:
                articles[item] = w3.prepro_base(file.read())

    # representasi bow
    list_of_bow = [] # membuat list kosong
    for key, value in articles.items(): # iterasi pasangan key, value
        # print key, value
        list_token = value.split() # cari kata2 dengan men-split
        dic = w4.bow(list_token)   # membuat bow
        list_of_bow.append(dic)    # append bow ke list kosong yg di atas

    # membuat matrix
    matrix_akhir = w4.matrix(list_of_bow) # jalankan fungsi matrix ke list_of_bow

    # mencari jarak
    jarak = {}
    for key, vektor in zip(articles.keys(), matrix_akhir):
        jarak[key] = w5.euclidean(matrix_akhir[0], vektor) # simpan nama file sbg key, jarak sbg value
    return jarak

# print main()


ef findSim(keyword, path):

    # membuat dictionary articles
    # membaca semua file .txt yang berada di direktori path(text files)
    # kemudian dimasukan kedalam dictionary articles dengan nama item/index(nama dokumen)
    articles = {}
    for item in os.listdir(path):
        if item.endswith(".txt"):
            with open(path + item, 'r') as file:
                articles[item] = w3.prepro_base(file.read())

    # memasukan kata kunci kedalam dictionary dengan nama item/index(keyword_index)
    # kemudian dimasukan ke dictionary articles dengan value keyword yang dimasukan
    kata_kunci = 'keyword_index'
    articles[kata_kunci] = w3.prepro_base(keyword)

    #menyimpan baris pertama dari dokumen dan menyimpannya dalam dictionary
    isi_doc = {}
    for isi in os.listdir(path):
     if isi.endswith(".txt"):
         with open(path + isi,'r') as file:
             isi_doc[isi] = file.read()

    # membuat list list_of_bow
    # yang kemudian dimasukan token-token unik di setiap dokumennya
    list_of_bow = []
    for key, value in articles.items():
        list_token = value.split()
        dic = w4.bow(list_token)
        list_of_bow.append(dic)

    # membuat matrix tiap-tiap dokumen dengan token unik dari semua dokumen
    matrix_akhir = w4.matrix(list_of_bow)

    # mencari id/urutan keyword_index
    # membuat dictionary presentase untuk semua dokumen
    id_keyword = articles.keys().index(kata_kunci)
    presentase = {}
    for key, vektor in zip(articles.keys(), matrix_akhir):
        if key != kata_kunci:
            presentase[key] = round(w5.cosine(matrix_akhir[id_keyword], vektor),2)

    #mencari baris dalam suati dokumen yang relevan dengan keyword
    baris = {}
    token_key = w3.prepro_base(keyword).split()
    for item in os.listdir(path):
        if item.endswith(".txt"):
            # baris[item] = ""
            tmp = [] 
            doc = open(path + item, 'r').readlines()
            for word in token_key:
                for line in doc:
                    if word in w3.tokenize(w3.prepro_base(line)) and line not in(value for index,value in enumerate(tmp)):
                        tmp.append(line)      
            if tmp != [] :
                #line of keyword
                lok = ''.join(tmp)
                baris[item] = lok
            else :
                baris[item] = 'kosong'

    return w4.sortdic(presentase, isi_doc, baris, descending=True)

# print findSim('./text files/ot_2.txt','./text files')
