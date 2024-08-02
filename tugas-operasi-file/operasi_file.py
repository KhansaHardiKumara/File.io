def membaca(nama_file):
    with open(nama_file, "r") as file_txt:
        file_content = file_txt.read()
        print(file_content)

def menulis(nama_file):
    
    membaca("file.txt")

    nama_kartun = input("Nama Kartun: ")
    text = "\n {}".format(nama_kartun)


    with open(nama_file, "a") as file_kartun:
        file_kartun.write(text)

menulis("file.txt")