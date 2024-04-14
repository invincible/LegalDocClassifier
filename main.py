import datetime
import sqlite3 as sql
import os

from langchain.document_loaders import UnstructuredFileLoader

import re
#import pymorphy3
#morph = pymorphy3.MorphAnalyzer()

with open ("russian", "r") as f:
    stop_words = f.read().splitlines()
stop_words.append('г')

def extract_text(file_path):
    text = ""
    try:
        loader = UnstructuredFileLoader(file_path)
        docs = loader.load()
        text = docs[0].page_content
    except Exception as e:
        print("Error in text extractor: ", e)

    return text

def clear_text(text):
    
    text = " ".join((re.sub(r'[^-а-яА-ЯёЁ]', ' ', text).split())).lower()    
    
    out = []
    for token in text.split():
        #token = morph.normal_forms(token)[0]
        out.append(token)
    
    text = " ".join(out)
    text = " ".join([word for word in text.split() if word not in stop_words])
    
    return text

def save_metainfo(file_path, doc_type):
    con = sql.connect("documents.db")
    cur = con.cursor()
    if not cur.execute("SELECT name FROM sqlite_master").fetchone():
        cur.execute("CREATE TABLE documents (doc_name, doc_type, date, size)")
    cur.execute("INSERT INTO documents VALUES (?, ?, ?, ?)", (file_path.split("/")[1], doc_type, datetime.datetime.now(), os.path.getsize(file_path)))
    con.commit()
    con.close()
    
def get_metainfo():
    con = sql.connect("documents.db")
    cur = con.cursor()
    if not cur.execute("SELECT name FROM sqlite_master;").fetchone():
        cur.execute("CREATE TABLE documents (doc_name, doc_type, date, size);")
    result = cur.execute("SELECT * FROM documents;").fetchall()
    con.close()

    return result
    
def prediction(text):
    preprocessed_text = clear_text(text)
    model_predict = "Dogovor"

    return model_predict

def check_type(file_path):
    extracted_text = extract_text(file_path)
    return prediction(extracted_text)

def upload_files(file_path):
    extracted_text = extract_text(file_path)
    model_prediction = prediction(extracted_text)
    save_metainfo(file_path, model_prediction)
    return model_prediction

def get_files():
    files = get_metainfo()

    result_dict = {"data": []}
    if files:
        for i in files:
            result_dict["data"].append({"filename": i[0], "document_type": i[1], "date": i[2], "size": i[3]})

    return result_dict