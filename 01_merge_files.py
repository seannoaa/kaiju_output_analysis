import argparse
import pandas as pd

# python ./01_merge_files.py MIA/kaiju_summaries/Meth3_MIA_B-1-genus-longtail.kaijuReport MIA/kaiju_summaries/Meth4_MIA_B-1-genus-longtail.kaijuReport MIA/kaiju_summaries/Meth1_MIA_A-1-genus-longtail.kaijuReport MIA/kaiju_summaries/Meth2_MIA_B-1-genus-longtail.kaijuReport MIA/kaiju_summaries/Meth5_MIA_B-1-genus-longtail.kaijuReport MIA/kaiju_summaries/Meth3_MIA_C-1-genus-longtail.kaijuReport MIA/kaiju_summaries/Meth4_MIA_C-1-genus-longtail.kaijuReport MIA/kaiju_summaries/Meth2_MIA_C-1-genus-longtail.kaijuReport MIA/kaiju_summaries/Meth5_MIA_C-1-genus-longtail.kaijuReport MIA/kaiju_summaries/Meth1_MIA_C-1-genus-longtail.kaijuReport MIA/kaiju_summaries/Meth4_MIA_A-1-genus-longtail.kaijuReport MIA/kaiju_summaries/Meth3_MIA_A-1-genus-longtail.kaijuReport MIA/kaiju_summaries/Meth5_MIA_A-1-genus-longtail.kaijuReport MIA/kaiju_summaries/Meth2_MIA_A-1-genus-longtail.kaijuReport MIA/kaiju_summaries/Meth1_MIA_B-1-genus-longtail.kaijuReport MIA_merged_output.csv
# python ./01_merge_files.py NP/kaiju_summaries/Meth3_NP_B-1-genus-longtail.kaijuReport NP/kaiju_summaries/Meth4_NP_B-1-genus-longtail.kaijuReport NP/kaiju_summaries/Meth1_NP_A-1-genus-longtail.kaijuReport NP/kaiju_summaries/Meth2_NP_B-1-genus-longtail.kaijuReport NP/kaiju_summaries/Meth5_NP_B-1-genus-longtail.kaijuReport NP/kaiju_summaries/Meth3_NP_C-1-genus-longtail.kaijuReport NP/kaiju_summaries/Meth4_NP_C-1-genus-longtail.kaijuReport NP/kaiju_summaries/Meth2_NP_C-1-genus-longtail.kaijuReport NP/kaiju_summaries/Meth5_NP_C-1-genus-longtail.kaijuReport NP/kaiju_summaries/Meth1_NP_C-1-genus-longtail.kaijuReport NP/kaiju_summaries/Meth4_NP_A-1-genus-longtail.kaijuReport NP/kaiju_summaries/Meth3_NP_A-1-genus-longtail.kaijuReport NP/kaiju_summaries/Meth5_NP_A-1-genus-longtail.kaijuReport NP/kaiju_summaries/Meth2_NP_A-1-genus-longtail.kaijuReport NP/kaiju_summaries/Meth1_NP_B-1-genus-longtail.kaijuReport NP_merged_output.csv

# python ./01_merge_files.py MIA/kaiju_summaries/Meth3_MIA_B-1-phylum-longtail.kaijuReport MIA/kaiju_summaries/Meth4_MIA_B-1-phylum-longtail.kaijuReport MIA/kaiju_summaries/Meth1_MIA_A-1-phylum-longtail.kaijuReport MIA/kaiju_summaries/Meth2_MIA_B-1-phylum-longtail.kaijuReport MIA/kaiju_summaries/Meth5_MIA_B-1-phylum-longtail.kaijuReport MIA/kaiju_summaries/Meth3_MIA_C-1-phylum-longtail.kaijuReport MIA/kaiju_summaries/Meth4_MIA_C-1-phylum-longtail.kaijuReport MIA/kaiju_summaries/Meth2_MIA_C-1-phylum-longtail.kaijuReport MIA/kaiju_summaries/Meth5_MIA_C-1-phylum-longtail.kaijuReport MIA/kaiju_summaries/Meth1_MIA_C-1-phylum-longtail.kaijuReport MIA/kaiju_summaries/Meth4_MIA_A-1-phylum-longtail.kaijuReport MIA/kaiju_summaries/Meth3_MIA_A-1-phylum-longtail.kaijuReport MIA/kaiju_summaries/Meth5_MIA_A-1-phylum-longtail.kaijuReport MIA/kaiju_summaries/Meth2_MIA_A-1-phylum-longtail.kaijuReport MIA/kaiju_summaries/Meth1_MIA_B-1-phylum-longtail.kaijuReport MIA_merged_output.csv
# python ./01_merge_files.py NP/kaiju_summaries/Meth3_NP_B-1-phylum-longtail.kaijuReport NP/kaiju_summaries/Meth4_NP_B-1-phylum-longtail.kaijuReport NP/kaiju_summaries/Meth1_NP_A-1-phylum-longtail.kaijuReport NP/kaiju_summaries/Meth2_NP_B-1-phylum-longtail.kaijuReport NP/kaiju_summaries/Meth5_NP_B-1-phylum-longtail.kaijuReport NP/kaiju_summaries/Meth3_NP_C-1-phylum-longtail.kaijuReport NP/kaiju_summaries/Meth4_NP_C-1-phylum-longtail.kaijuReport NP/kaiju_summaries/Meth2_NP_C-1-phylum-longtail.kaijuReport NP/kaiju_summaries/Meth5_NP_C-1-phylum-longtail.kaijuReport NP/kaiju_summaries/Meth1_NP_C-1-phylum-longtail.kaijuReport NP/kaiju_summaries/Meth4_NP_A-1-phylum-longtail.kaijuReport NP/kaiju_summaries/Meth3_NP_A-1-phylum-longtail.kaijuReport NP/kaiju_summaries/Meth5_NP_A-1-phylum-longtail.kaijuReport NP/kaiju_summaries/Meth2_NP_A-1-phylum-longtail.kaijuReport NP/kaiju_summaries/Meth1_NP_B-1-phylum-longtail.kaijuReport NP_merged_output.csv

def merge_files(input_files, output_file, sample_set, taxa_level):
    # Initialize an empty dataframe to hold the merged data
    merged_df = None
    
    # Loop through each file in the input list
    for file in input_files:
        # Read the file into a dataframe
        df = pd.read_csv(file, sep='\t')
        
        # Merge the current dataframe with the accumulated merged_df
        if merged_df is None:
            merged_df = df
        else:
            merged_df = pd.merge(merged_df, df, on='taxon_id', how='outer', suffixes=('', '_'+file))
    
    # Rename specific columns as specified
    if sample_set == "MIA":
        renamed_columns = {
            'file': 'file_Meth3_MIA_B-1-{}'.format(taxa_level),
            'percent': 'percent_Meth3_MIA_B-1-{}'.format(taxa_level),
            'reads': 'reads_Meth3_MIA_B-1-{}'.format(taxa_level)
        }

    if sample_set == "NP":
        renamed_columns = {
            'file': 'file_Meth3_NP_B-1-{}'.format(taxa_level),
            'percent': 'percent_Meth3_NP_B-1-{}'.format(taxa_level),
            'reads': 'reads_Meth3_NP_B-1-{}'.format(taxa_level)
        }

    merged_df.rename(columns=renamed_columns, inplace=True)
    
    # Rearrange columns to place "taxon_id" as the first column and "taxon_name" as the second column
    columns = list(merged_df.columns)
    columns.insert(0, columns.pop(columns.index('taxon_id')))
    columns.insert(1, columns.pop(columns.index('taxon_name')))
    merged_df = merged_df[columns]
    
    # Remove the specified string from the entire dataframe
    merged_df.replace('/kb/module/work/tmp/output_1712422967823/kaiju_output/', '', regex=True, inplace=True)
    merged_df.replace('/kb/module/work/tmp/output_1712422974401/kaiju_output/', '', regex=True, inplace=True)

    # Remove decimal point and trailing zero from all values in the "taxon_id" column
    merged_df['taxon_id'] = merged_df['taxon_id'].apply(lambda x: str(x).split('.')[0])
    
    # Rename all column names to remove the specified suffix and string
    merged_df.columns = [col.replace('-longtail.kaijuReport', '').replace('MIA/kaiju_summaries/', '') for col in merged_df.columns]
    merged_df.columns = [col.replace('-longtail.kaijuReport', '').replace('NP/kaiju_summaries/', '') for col in merged_df.columns]

    # Save the merged dataframe to a CSV file
    merged_df.to_csv(output_file, index=False)
    print(f"Merged file saved as {output_file}")

if __name__ == "__main__":
    # Create the parser
    parser = argparse.ArgumentParser(description="Merge multiple files into a master file based on the taxon_id column with specified processing steps")
    
    # Add the arguments
    parser.add_argument('input_files', nargs='+', help="List of input files to merge")
    parser.add_argument('output_file', help="Output file to save the merged result")
    
    # Parse the arguments
    args = parser.parse_args()
    
    # Define a sample set specific variable for special handling (i.e "MIA" or "NP")
    sample_set = args.input_files[0].split('/')[0]

    # Define a sample set specific variable for special handling (i.e "genus" or "phylym")
    taxa_level = args.input_files[0].split('/')[2].split('-')[-2]

    # Call the merge_files function with the provided arguments
    merge_files(args.input_files, args.output_file, sample_set, taxa_level)