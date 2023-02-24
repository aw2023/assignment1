import pandas as pd


def clean(contact_info_file, other_info_file):
    df1 = pd.read_csv(contact_info_file)
    df2 = pd.read_csv(other_info_file)
    # 1 merge the two input data files based on the ID of each respondent.
    df_merge = df1.merge(df2, left_on='respondent_id', right_on='id', how='outer')
    df_merge = df_merge.drop(labels='id', axis=1)

    # 2 drop any rows with missing values.
    df_drop_na = df_merge.dropna()

    # 3 drop rows if the job value contains ‘insurance’ or ‘Insurance’.
    df_drop_insurance = df_drop_na[~df_drop_na['job'].str.contains('insurance|Insurance')]

    # 4 write the cleaned data to the file specified by the output_file argument
    return df_drop_insurance


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('contact_info_file', help='Data file 1(CSV)')
    parser.add_argument('other_info_file', help='Data file 2(CSV)')
    parser.add_argument('output_file', help='Cleaned data file (CSV)')
    args = parser.parse_args()
    cleaned = clean(args.contact_info_file, args.other_info_file)
    cleaned.to_csv(args.output_file, index=False)



