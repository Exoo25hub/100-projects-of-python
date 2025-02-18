import zipfile
filee = input("file: ")
zipfilen = input("zip file name: ")
with zipfile.ZipFile(zipfilen, "w") as zipf:
    zipf.write(filee)  # Replace with your file name
