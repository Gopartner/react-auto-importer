import sys
import os
import re

def find_src_dir(filepath):
    """
    Mencari folder 'src' di direktori proyek berdasarkan lokasi file yang sedang diedit.
    """
    current_dir = os.path.dirname(filepath)
    while current_dir != '/':
        if 'src' in os.listdir(current_dir):
            return os.path.join(current_dir, 'src')
        current_dir = os.path.dirname(current_dir)
    return None

def find_component_path(component_name, src_dir, filepath):
    """
    Mencari path komponen di dalam direktori 'src' dan subdirektorinya.
    Menghasilkan path relatif berdasarkan lokasi file yang sedang diedit.
    """
    for root, _, files in os.walk(src_dir):
        for file in files:
            if file == f"{component_name}.jsx" or file == f"{component_name}.js":
                absolute_path = os.path.join(root, file)
                relative_path = os.path.relpath(absolute_path, os.path.dirname(filepath))
                # Memastikan path menggunakan forward slash dan memperbaiki path relatif
                return relative_path.replace(os.sep, '/').replace('.jsx', '')
    return None

def get_existing_imports_and_comments(filepath):
    """
    Mengambil daftar impor dan komentar komponen yang tidak ditemukan dari file.
    """
    imports = set()
    missing_components = set()
    with open(filepath, 'r') as file:
        for line in file:
            # Ambil impor yang sudah ada
            import_match = re.match(r'import\s+([a-zA-Z0-9_]+)\s+from\s+[\'"](.+?)[\'"]', line)
            if import_match:
                imports.add(import_match.group(1))
            
            # Ambil komentar untuk komponen yang tidak ditemukan
            missing_match = re.match(r'// import\s+([a-zA-Z0-9_]+)\s+from\s+[\'"]path/to/\1[\'"]', line)
            if missing_match:
                missing_components.add(missing_match.group(1))
    return imports, missing_components

def add_imports(filepath, imports_to_add, missing_components):
    """
    Menambahkan impor dan komentar jika ada komponen yang tidak ditemukan,
    tanpa menambah komentar yang sudah ada sebelumnya.
    """
    with open(filepath, 'r+') as file:
        lines = file.readlines()
        file.seek(0)
        
        # Tambahkan impor baru
        if imports_to_add:
            file.write("\n".join(imports_to_add) + "\n\n")
        
        # Tambahkan komentar untuk komponen yang tidak ditemukan
        if missing_components:
            file.write("// Komponen berikut tidak ditemukan:\n")
            for component in missing_components:
                file.write(f"// import {component} from 'path/to/{component}';\n")
            file.write("\n")

        file.writelines(lines)

def main():
    if len(sys.argv) < 2:
        print("Usage: python auto_import_react.py <file_path>")
        return

    filepath = sys.argv[1]
    print(f"Processing file: {filepath}")

    if not os.path.isfile(filepath):
        print(f"Error: File '{filepath}' does not exist.")
        return

    src_dir = find_src_dir(filepath)
    if not src_dir:
        print("Error: Folder 'src' tidak ditemukan dalam proyek.")
        return

    print(f"Src directory: {src_dir}")

    existing_imports, existing_missing_components = get_existing_imports_and_comments(filepath)

    with open(filepath, 'r') as file:
        content = file.read()

    # Mencari komponen JSX yang belum diimpor
    components = set(re.findall(r'<([A-Z][a-zA-Z0-9_]*)', content))
    imports_to_add = []
    missing_components = []

    for component in components:
        if component not in existing_imports and component not in existing_missing_components:
            component_path = find_component_path(component, src_dir, filepath)
            if component_path:
                # Menyesuaikan path relatif
                imports_to_add.append(f"import {component} from '{component_path}';")
            else:
                missing_components.append(component)

    # Tambahkan impor dan komentar
    if imports_to_add or missing_components:
        add_imports(filepath, imports_to_add, missing_components)
        if imports_to_add:
            print("Impor komponen telah ditambahkan:")
            for imp in imports_to_add:
                print(f"  {imp}")
        if missing_components:
            print("Komponen berikut tidak ditemukan dan ditambahkan sebagai komentar:")
            for component in missing_components:
                print(f"  // import {component} from 'path/to/{component}';")
    else:
        print("Semua komponen sudah diimpor atau tidak ada komponen yang perlu diimpor.")

if __name__ == "__main__":
    main()
