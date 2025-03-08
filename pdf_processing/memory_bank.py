import os

MEMORY_BANK_DIR = '../memory-bank'

def get_memory_bank_file(content):
    # Simple categorization based on content
    if 'technology' in content.lower() or 'software' in content.lower():
        return 'techContext.md'
    elif 'project' in content.lower() or 'goal' in content.lower():
        return 'projectbrief.md'
    else:
        return 'activeContext.md'

def update_memory_bank(content):
    file_to_update = get_memory_bank_file(content)
    file_path = os.path.join(MEMORY_BANK_DIR, file_to_update)
    
    # Create the file if it doesn't exist
    if not os.path.exists(file_path):
        with open(file_path, 'w') as f:
            f.write(f"# {file_to_update[:-3]}\n\n")
    
    # Append the new content
    with open(file_path, 'a') as f:
        f.write(f"\n## New PDF Content\n\n{content}\n")
    
    print(f"Updated {file_to_update} in Memory Bank")

def read_memory_bank_file(file_name):
    file_path = os.path.join(MEMORY_BANK_DIR, file_name)
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            return f.read()
    else:
        return f"File {file_name} not found in Memory Bank"
