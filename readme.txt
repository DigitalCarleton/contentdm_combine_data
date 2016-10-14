readme.txt

This script, cdm_combine_data.py, was created to combine exported ContentDM
metadata into one csv file. The user chooses which data headings of each
exported file to include, delete, or add to a "Misc" column. Contained in
this zip file should be two CSV files starting with "data_". One shows what
it would look like if all the columns from each file were added and the 
other has gone through a selection process where a few columns have been
deleted with the script or added to the Misc column.

The script requires having Python 2.7 installed and set up for command line
use. 

From the directory that this file is in, run it from the command line/unix
prompt:
python <filepath-if-applicable>cdm_combine_data.py <cdm_export_directory>

example:
python "C:\Users\me\cdm_combine_data.py" "C:\Users\me\cdm_item_export"
Note that Windows uses '\' for filepaths and Mac/Unix uses '/'.


For more information, view the comments in cdm_combine_data.py and (if
desired) in rm_special_chars.py.

-------------
Detailed contents:

Contents:

- folder "cdm_item_export":  contains a few sample files for running the script on

- cdm_combine_data.py:  the heart of the code

- (optional) chars_to_replace.csv:  sometimes text files come with special characters that mess up the output, and this file in conjunction with rm_special_chars.py and rm_special_chars.pyc help clean it up. Usage of this is not necessary or required. (I included it because it's an adaption of a different work project)
- readme.txt:  great info eh

- (optional) rm_special_chars.py:  see chars_to_replace.csv above

- (optional) rm_special_chars.pyc:  see chars_to_replace.csv above. This is the compiled version of rm_special_chars.py (which happens when you run one Python program from another; in this case, cdm_combine_data.py has the option to run with rm_special_chars.py). 

-------------
Carleton College DHA - Spring 2015
originally written by Sahree Kasper (sahreek@gmail.com)