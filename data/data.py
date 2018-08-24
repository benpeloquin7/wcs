"""Preprocess WCS data.


"""
import pandas as pd
import logging
from utils import *

logging.getLogger().setLevel(logging.INFO)


def input_data(url, col_names=None, dtypes=None, skiprows=[]):
    """Bespoke WCS data ingest functionality.

    See http://www1.icsi.berkeley.edu/wcs/data.html.
    """
    if col_names:
        if dtypes is not None:
            assert (len(col_names) == len(dtypes))
            dtypes_ = {k: v for k, v in zip(col_names, dtypes)}
            df = pd.read_table(url, names=col_names, dtype=dtypes_,
                               keep_default_na=False, na_values=[''],
                               skiprows=skiprows)
        else:
            df = pd.read_table(url, names=col_names,
                               keep_default_na=False, na_values=[''],
                               skiprows=skiprows)
    else:
        df = pd.read_table(url, keep_default_na=False, na_values=[''],
                           skiprows=skiprows)

    return df


def merge_datasets():
    """Primary WCS data merge."""
    df_chips = input_data(chip_url, chip_names, chip_dtypes)
    df_dict = input_data(dict_url, dict_names, dict_dtypes, [0])
    df_terms = input_data(term_url, term_names, term_dtypes)
    df_foc_exp = input_data(foci_exp_url, foc_exp_names, foc_exp_dtypes)
    df_colors = input_data(colors_url, color_names, color_dtypes, [0])

    # foc_exp -> term
    joiner = ['lang_num', 'speaker_num', 'term_abbr']
    df_join_1 = pd.merge(df_foc_exp, df_terms, on=joiner) \
        .reset_index(drop=True)

    # foc_exp -> term -> dict
    joiner = ['lang_num', 'term_abbr']
    df_join_2 = pd.merge(df_join_1, df_dict, on=joiner) \
        .reset_index(drop=True)

    # terms -> chips -> foc-exp -> dict
    joiner = ['chip_num', 'chip_coord']
    df_join_3 = pd.merge(df_join_2, df_chips, on=joiner) \
        .reset_index(drop=True)

    # terms -> chips -> foc-exp -> dict -> colors
    joiner = ['chip_num']
    df_join_4 = pd.merge(df_join_3, df_colors, on=joiner) \
        .reset_index(drop=True)

    return df_join_4


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--do-write", action='store_true', default=True,
                        help='Write to output file flag [default: True]')
    parser.add_argument("--out-file", type=str,
                        default='./data/merged_wcs_data.csv',
                        help='Output file [default: merged_wcs_data.csv]')

    args = parser.parse_args()

    df_merged = merge_datasets()
    if args.do_write:
        logging.info('Writing data to:\t{}'.format(args.out_file))
        df_merged.to_csv(args.out_file)
