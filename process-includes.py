#!/usr/bin/env python3
import os
import re
from pathlib import Path

def process_includes(file_path, root_dir):
    """Verarbeitet {% include %}-Tags in einer HTML-Datei."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Finde alle {% include ... %}-Tags
    pattern = r'{%\s*include\s+([^\s}]+)\s*%}'
    
    def replace_include(match):
        include_file = match.group(1)
        # Suche immer im root _includes directory
        include_path = Path(root_dir) / '_includes' / include_file
        
        if include_path.exists():
            with open(include_path, 'r', encoding='utf-8') as f:
                return f.read()
        else:
            print(f"Warning: {include_file} not found at {include_path}")
            return match.group(0)
    
    # Ersetze alle includes
    processed = re.sub(pattern, replace_include, content)
    
    # Schreibe zurück
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(processed)
    
    print(f"Processed: {file_path}")

# Root directory (aktuelles Verzeichnis)
root = os.getcwd()

# Verarbeite nur HTML-Dateien im aktuellen Verzeichnis und Unterordnern
# Ignoriere _includes
for root_dir, dirs, files in os.walk(root):
    # Entferne _includes aus der Liste, damit os.walk nicht in den Ordner geht
    if '_includes' in dirs:
        dirs.remove('_includes')
    
    for file in files:
        if file.endswith('.html'):
            file_path = os.path.join(root_dir, file)
            process_includes(file_path, root)

print("✓ Alle includes verarbeitet")
