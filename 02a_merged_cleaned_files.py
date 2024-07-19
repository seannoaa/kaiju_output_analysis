import pandas as pd
import argparse

# python ./02a_merged_cleaned_files.py MIA_merged_output_clean.csv NP_merged_output_clean.csv MIA-NP_merged_output_clean.csv

def merge_files(file1_path, file2_path, output_path):
    # Load the first file
    file1 = pd.read_csv(file1_path)
    
    # Load the second file
    file2 = pd.read_csv(file2_path)
    
    # Merge the two files based on the 'taxon_id' column
    merged_file = pd.merge(file1, file2, on='taxon_id')

    # Remove the 'taxon_name_y' column
    if 'taxon_name_y' in merged_file.columns:
        merged_file = merged_file.drop(columns=['taxon_name_y'])
    
    # Rename 'taxon_name_x' to 'taxon_name'
    if 'taxon_name_x' in merged_file.columns:
        merged_file = merged_file.rename(columns={'taxon_name_x': 'taxon_name'})
    
    # Save the merged file to a new CSV file
    merged_file.to_csv(output_path, index=False)
    
    print(f"Files have been merged successfully! Output saved to {output_path}")

def main():
    parser = argparse.ArgumentParser(description="Merge two CSV files based on the 'taxon_id' column.")
    parser.add_argument('file1', help="Path to the first CSV file")
    parser.add_argument('file2', help="Path to the second CSV file")
    parser.add_argument('output', help="Path to save the merged CSV file")
    
    args = parser.parse_args()
    
    merge_files(args.file1, args.file2, args.output)

if __name__ == '__main__':
    main()
