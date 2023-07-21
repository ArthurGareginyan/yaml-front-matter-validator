import os
import yaml
import argparse

# Create the parser
parser = argparse.ArgumentParser(description='Process a directory path.')
# Add the argument
parser.add_argument('dirpath', type=str, help='The directory path to search')
# Parse the arguments
args = parser.parse_args()

# Define the root directory to search from
root_dir = args.dirpath

# Iterate through root directory and subdirectories
for dirpath, dirnames, filenames in os.walk(root_dir):
    for filename in filenames:
        # Check if the file is a .md file
        if filename.endswith('.md'):
            # Construct the full file path
            filepath = os.path.join(dirpath, filename)
            with open(filepath, 'r') as f:
                lines = f.readlines()

            front_matter = []
            if lines:
                # Assuming front matter is at the start of the file
                # and is delimited by '---'
                if lines[0].strip() == '---':
                    for i in range(1, len(lines)):
                        if lines[i].strip() == '---':
                            break
                        front_matter.append(lines[i])
            
            # Convert list of lines to a single string
            front_matter_str = ''.join(front_matter)
            try:
                # Try to parse the front matter
                parsed = yaml.safe_load(front_matter_str)
            except yaml.YAMLError as e:
                print(f"Error in file: {filepath}")
                print(f"Error details: {e}")
