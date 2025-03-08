import os
import shutil
import json
from datetime import datetime

def process_pdf(input_file):
    # Ensure input and processed directories exist
    input_dir = os.path.join(os.path.dirname(__file__), 'input')
    processed_dir = os.path.join(os.path.dirname(__file__), 'processed')
    os.makedirs(input_dir, exist_ok=True)
    os.makedirs(processed_dir, exist_ok=True)

    input_path = os.path.join(input_dir, input_file)
    if not os.path.exists(input_path):
        print(f"Error: {input_file} not found in the input directory.")
        return

    # Generate output filename with versioning
    base_name, ext = os.path.splitext(input_file)
    output_file = input_file
    version = 1
    while os.path.exists(os.path.join(processed_dir, output_file)):
        output_file = f"{base_name}_v{version}{ext}"
        version += 1

    output_path = os.path.join(processed_dir, output_file)

    # Move the file
    shutil.move(input_path, output_path)

    # Log the action
    log_file = os.path.join(os.path.dirname(__file__), 'processing_log.txt')
    with open(log_file, 'a') as log:
        log.write(f"{datetime.now()}: Processed {input_file} to {output_file}\n")

    # Generate summary
    summary = {
        "original_filename": input_file,
        "processed_filename": output_file,
        "processing_date": datetime.now().isoformat(),
        "file_size": os.path.getsize(output_path)
    }

    summary_file = os.path.join(processed_dir, f"{os.path.splitext(output_file)[0]}_summary.json")
    with open(summary_file, 'w') as f:
        json.dump(summary, f, indent=2)

    print(f"Processed {input_file} to {output_file}")
    print(f"Summary saved to {summary_file}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python process_pdf.py <input_file>")
    else:
        process_pdf(sys.argv[1])
