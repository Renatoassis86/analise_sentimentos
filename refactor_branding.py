import os
import re

def replace_in_files():
    root_dir = "."
    patterns = {
        r"Marketing Intelligence": "Marketing Intelligence",
        r"Marketing Intelligence": "Marketing Intelligence",
        r"marketing-intelligence": "marketing-intelligence",
        # Adicionar padrões para o token se encontrarmos outros ghp_
        r"ghp_[A-Za-z0-9]{36}": "REDACTED_API_TOKEN" 
    }
    
    exclude_dirs = {".git", "venv", ".ipynb_checkpoints"}
    
    for root, dirs, files in os.walk(root_dir):
        dirs[:] = [d for d in dirs if d not in exclude_dirs]
        for name in files:
            file_path = os.path.join(root, name)
            # Skip binary
            if name.endswith(('.png', '.jpg', '.jpeg', '.gif', '.pdf', '.docx', '.xlsx')):
                continue
            
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                new_content = content
                for pattern, repl in patterns.items():
                    new_content = re.sub(pattern, repl, new_content)
                
                if new_content != content:
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    print(f"✅ Refatorado: {file_path}")
            except Exception as e:
                # Silenciosamente pular arquivos que não puderam ser lidos (provavelmente binários)
                pass

if __name__ == "__main__":
    replace_in_files()
