import os

# Get all txt files in current directory
txt_files = [f for f in os.listdir('.') if f.endswith('.txt')]

# Create/open output file
with open('AIO.txt', 'w', encoding='utf-8') as outfile:
    # Process each txt file
    for txt_file in txt_files:
        outfile.write(f'# {txt_file}\n')  # Write filename as comment
        
        # Read and write content of current file
        with open(txt_file, 'r', encoding='utf-8') as infile:
            outfile.write(infile.read())
        
        # Add a newline between files
        outfile.write('\n\n')

print(f'Combined {len(txt_files)} files into AIO.txt')