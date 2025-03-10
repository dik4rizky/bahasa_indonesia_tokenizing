import PyPDF2
import re

# Buka file PDF
temp_term =[]
term=[]
halaman=0

with open("Kamus-Besar-Bahasa-Indonesia.pdf", "rb") as file:
    reader = PyPDF2.PdfReader(file)
    for page in reader.pages:
        teks=page.extract_text()  # Ekstrak teks dari setiap halaman
        halaman+=1
        print(halaman)
        hasil = re.sub(r"[^a-zA-Z\s\-]", "", teks) ## hapus simbol kecuali spasi dan -
        for kata in hasil.split():## pisah berdasarkan spasi
            temp_term.append(kata)
            #print(kata)
    
term=sorted([re.sub(r"^[-]+", "", s)for s in list(set(temp_term)) ])   



with open("output.txt", "w", encoding="utf-8", errors="ignore") as file:
    for item in term:
        file.write(item + "\n")

        