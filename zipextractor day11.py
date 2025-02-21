import zipfile
from pyfiglet import figlet_format
print(figlet_format("ZIP EXTRACTOR"))
filee = input("Zip file path/name: ")
where = input("Where to extract path (leave blank for default): ")

# Use "extracted_folder" if no path is provided
extract_path = where if where else "extracted_folder"

with zipfile.ZipFile(filee, "r") as zipf:
    zipf.extractall(extract_path)

print(f"Files extracted to: {extract_path}")
