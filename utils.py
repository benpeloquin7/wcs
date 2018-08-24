# chip.txt
chip_url = 'http://www1.icsi.berkeley.edu/wcs/data/20021219/txt/chip.txt'
chip_names = ['chip_num', 'grid_row', 'grid_col', 'chip_coord']
chip_dtypes = [int, str, str, str]
# dict.txt
dict_url = 'http://www1.icsi.berkeley.edu/wcs/data/20041016/txt/dict.txt'
dict_names = ['lang_num', 'term_num', 'term', 'term_abbr']
dict_dtypes= [int, int, str, str]
# foc_exp.txt
foci_exp_url = 'http://www1.icsi.berkeley.edu/wcs/data/20030414/txt/foci-exp.txt'
foc_exp_names = ['lang_num', 'speaker_num', 'response', 'term_abbr', 'chip_coord']
foc_exp_dtypes= [int, int, str, str, str]
# term.txt
term_url = 'http://www1.icsi.berkeley.edu/wcs/data/20021219/txt/term.txt'
term_names = ['lang_num', 'speaker_num', 'chip_num', 'term_abbr']
term_dtypes = [int, int, int, str]
# cnum-vhcm-lab-new.txt
colors_url = 'https://www1.icsi.berkeley.edu/wcs/data/cnum-maps/cnum-vhcm-lab-new.txt'
color_names = ['chip_num', 'V', 'H', 'C', 'MunH', 'MunV', 'L', 'A', 'B']
color_dtypes = [int, str, int, int, str, float, float, float, float]

# collections
data_files = ['foci_exp', 'dict', 'chip', 'term']
urls = [foci_exp_url, dict_url, chip_url, term_url]
col_names = [foc_exp_names, dict_names, chip_names, term_names]
dtypes = [foc_exp_dtypes, dict_dtypes, chip_dtypes, term_dtypes]