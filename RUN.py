import sys
import shutil
import os

sys.path.insert(0, 'src') # add library code to path

from ETL import ftp_server_authen, download_file #add download functions

from process import process_data #add process test data func

from Clean_EDA import read_gz, clean_df, create_histogram, manhattan_plot 

#load json config files
config = 'config/data-param.json'

def load_params(config_file):
    """
    Load the parameters from json files
    """
    with open(config_file) as fh:
        param = json.load(fh)
    return param

def main(targets):
    """
    The main function where we run the src code.
    """

    # make the fastq target
    if 'test' in targets:
        cfg = load_params(config)
        #recursively downloading all the test files
        for study in cfg['study']:
            #grab the authenticated server
            ftp = ftp_server_authen()
            #download the data accordingly
            download_file(ftp, cfg['outpath'], study)
    if 'clean' in targets:
        data = read_gz(T2D_data)
        clean_data = clean_df(data)
        histogram = create_histograms(clean_data,10)
        manhattan = manhattan_plot(clean_data, 10)
        
        
    return

if __name__ == '__main__':
    targets = sys.argv[1:]
    main(targets)
