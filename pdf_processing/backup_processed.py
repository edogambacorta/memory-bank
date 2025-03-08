import os
import shutil
from datetime import datetime

def backup_processed():
    # Define directories
    script_dir = os.path.dirname(__file__)
    processed_dir = os.path.join(script_dir, 'processed')
    backup_dir = os.path.join(script_dir, 'backup')

    # Ensure backup directory exists
    os.makedirs(backup_dir, exist_ok=True)

    # Create a timestamped backup folder
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_folder = os.path.join(backup_dir, f"backup_{timestamp}")

    # Copy the processed folder to the backup folder
    shutil.copytree(processed_dir, backup_folder)

    print(f"Backup created: {backup_folder}")

if __name__ == "__main__":
    backup_processed()
