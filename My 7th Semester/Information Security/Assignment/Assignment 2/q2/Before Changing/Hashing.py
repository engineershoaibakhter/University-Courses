import hashlib
import os
import pandas as pd

def calculate_sha256(file_path):
    """Calculate the SHA256 hash of a file."""
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as file:
        for chunk in iter(lambda: file.read(4096), b""):
            sha256_hash.update(chunk)
    return sha256_hash.hexdigest()

def generate_initial_hashes(word_files, excel_file):
    """Generate SHA256 hashes for the given Word files and save to Excel."""
    data = {"File Name": [], "SHA256 Hash": []}
    
    for file in word_files:
        if not os.path.isfile(file):
            print(f"Warning: {file} does not exist and will be skipped.")
            continue
        file_path = os.path.abspath(file)
        sha256_hash = calculate_sha256(file_path)
        data["File Name"].append(file)
        data["SHA256 Hash"].append(sha256_hash)
        print(f"Processed {file}: {sha256_hash}")
    
    df = pd.DataFrame(data)
    df.to_excel(excel_file, index=False)
    print(f"\nInitial hash values saved to {excel_file}")

if __name__ == "__main__":
    # List of Word files
    word_files = [
        "File_1.docx",
        "File_2.docx",
        "File_3.docx",
        "File_4.docx",
        "File_5.docx",
        "File_6.docx",
        "File_7.docx",
        "File_8.docx",
        "File_9.docx",
        "File_10.docx"
    ]
    
    # Define the initial Excel file to store hash values
    initial_excel_file = "hash_values_initial.xlsx"
    
    # Generate and save initial hash values
    generate_initial_hashes(word_files, initial_excel_file)
