import argparse
import pandas as pd

# python ./02_clean_files.py MIA_merged_output.csv MIA_merged_output_clean.csv
# python ./02_clean_files.py NP_merged_output.csv NP_merged_output_clean.csv

def clean_csv(input_file, output_file):
    # Read the input CSV file
    df = pd.read_csv(input_file)
    
    # Remove columns that start with "file_", "taxon_name_", and "_reads"
    columns_to_keep = [col for col in df.columns if not (col.startswith('file_') or col.startswith('taxon_name_') or col.startswith('reads_'))]
    df = df[columns_to_keep]
    
    # Rename columns to remove "percent_" and "-species"
    df.columns = [col.replace('percent_', '').replace('-phylum', '').replace('-species', '').replace('-genus', '') for col in df.columns]

    # Replace missing values with zero
    df = df.fillna(0)

    # Filter out rows where the "taxon_id" column value is equal to "0.0"
    df = df[df['taxon_id'] != 0.0]

    # Convert all "0" values in the "taxon_name" column to "NA"
    df['taxon_name'] = df['taxon_name'].replace(0, 'NA')
            
    # Output the cleaned DataFrame to a new CSV file
    df.to_csv(output_file, index=False)
    print(f"Cleaned data has been saved to {output_file}")

def main():
    parser = argparse.ArgumentParser(description="Clean a CSV file by removing specific columns and renaming others.")
    parser.add_argument('input_file', type=str, help="Path to the input CSV file")
    parser.add_argument('output_file', type=str, help="Path to the output CSV file")
    
    args = parser.parse_args()
    
    clean_csv(args.input_file, args.output_file)

if __name__ == "__main__":
    main()