"""
    cdm_combine_data.py
    Created to combine exported ContentDM metadata in one csv file. The
    user chooses which data headings of each exported file to include,
    delete, or add to a "Misc" column.
    
    Usage: python cdm_combine_data.py <cdm_export_directory>
    
    Input: <cdm_export_directory> containing the exported metadata files.
    Output: data_MM-DD-YYYY_HHMMSS.csv saved in <cdm_export_directory>. It
    combines select metadata from the given export files in the directory.
    
    Possible future suggestions:
     - make sure that no data lines end with strange punctuation such as a
     semicolon
     - provide a renaming option for columns (as the code is written, the 
     old names would probably need to be saved somehow)
     - executable file to avoid using command line/unix prompt
     - gather a list of field names and give the option to group similar
     ones
     - user interface
"""

import rm_special_chars # optional: uncomment line ~110 and read rm_special_chars.py
import csv, datetime, glob, os, sys

columns = []
deleted = []
misc = []

def line_parser(line):
    """ Returns a list of length 2. The first item is the category name
        and the second is its corresponding data. 
    """
    # split the line on the first occurence of a colon
    line = line.strip().split(':',1)
    
    # strip extra whitespace from each word in the line
    line = [w.strip() for w in line]

    return line


def prompt(col):
    """ Returns column name or None. User chooses whether the given column
        name will be kept as a column header, added to the misc section,
        or deleted. 
    """
    if col in columns or col in deleted or col in misc:
        return None
    
    print '\n\nCurrent column:', col, '\n--------------------------------'
    keep_col = raw_input('Add this column to the spreadsheet? y/n\n')
    if check_input(keep_col):
        # to implement renaming columns, must keep track of orig names
        #rename_col = raw_input('Rename this column? y/n\n')
        #if check_input(rename_col):
        #    rename_name = raw_input('Enter the new column name: ')
        #    return rename_name
        #elif check_input(rename_col) == False:
        return col
    elif check_input(keep_col) == False:
        delete_col = raw_input('Delete this column or add it to a miscellaneous field? d/m\n')
        if check_input(delete_col, 'd', 'm'):
            # remove column header completely
            deleted.append(col)
            return None
        elif check_input(delete_col, 'd', 'm') == False:
            # add column to misc section
            misc.append(col)
            return None
    else: # bad input
        prompt(col)

        
def check_input(p, y='y', n='n'):
    """ Returns True or False if the given input matches with 'y' or 'n'.
        'q' can be used at any time to quit (except during renaming--not
        yet implemented). Instead of 'y' and 'n', the user can define
        their own versions of yes and no (for example, see the line that
        prompts if the column should be deleted or modified).
    """
    if p.lower() == y: 
        return True
    elif p.lower() == n:
        return False
    elif p.lower() == 'q':
        sys.exit()
    else:
        return None


def main():
    cdm_download_folder = sys.argv[1]
    
    # join path with a slash (dependent on operating system)
    os.chdir(os.path.join(cdm_download_folder,""))

    # create unique output filename related to date and time
    now = datetime.datetime.now()
    output_file_name = "data_%02d-%02d-%02d_%02d%02d%02d.csv" % (now.month, now.day, now.year, now.hour, now.minute, now.second)
    output = csv.writer(open(output_file_name,"wb"))
    
    
    # decide on columns to add
    all_cols = raw_input('Add all columns to the spreadsheet? y/n\n')
    
    # cycles through all possible column names in all txt files
    for fname in glob.glob("*.txt"):
        #rm_special_chars.rm(fname) # use this file to remove unwanted chars
        with open(fname) as f:
            for line in f:
                l = line_parser(line)
                if check_input(all_cols):
                    columns.append(l[0])
                elif not l[0] in columns or not l[0] in misc or not l[0] in deleted:
                    col = prompt(l[0])
                    if col: # aka: don't append it if prompt() gave None
                        columns.append(col)
    columns.append("Misc")
    
    # write the header row
    output.writerow(columns)

    # write any corresponding data from each txt file to the csv file
    for fname in glob.glob("*.txt"):
        # set correct number of columns for the row
        row = [None] * len(columns)
        with open(fname) as f:
            for line in f:
                l = line_parser(line)
                if l[0] in columns:
                    row[columns.index(l[0])] = l[1]
                if l[0] in misc:
                    # must add both the heading and text
                    if row[-1] == None:
                        row[-1] = ": ".join(l)
                    else:
                        row[-1] = "; ".join([row[-1],": ".join(l)])
        output.writerow(row)
            
main()