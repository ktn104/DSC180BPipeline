import os
import ftplib
import zipfile
import gzip


def ftp_server_authen():
    """
    a function call to connect and authenticate a ftp server
    """
    
    #connect to the FTP server
    ftp = ftplib.FTP("ftp.ebi.ac.uk")
    #login anonymously
    ftp.login()
    #change the parent dir
    parent_dir = '/pub/databases/gwas/summary_statistics'
    ftp.cwd(parent_dir)
    #ftp.retrlines("LIST")
    return ftp

#grab the authenticated server
ftp = ftp_server_authen()

def ftp_server(ftp, study = None):
    """
    a function call to change to a specific study subdir
    """
    assert isinstance(study, str)

    #changing to one specific study
    ftp.cwd('/%s' % study)
    ftp.retrlines("LIST")

def get_t2d_file_names(server):
    """
    a function call to save all the useful T2D files into a list within the current directory
    """
    directory_listing = []
    file_listing = []
    #get the list of sub-directories at the current dir and append them to a list
    server.retrlines("LIST", directory_listing.append)
    #only grab the bam files from the list 
    file_listing = [i.split()[-1] for i in directory_listing if 'txt' == i.split()[-1][-3:]]
    return file_listing

def download_bam_file(filetype, outdir, study):
    """
    Function call to download bam files
    """

    #redirect the ftp server
    #go to one specific T2D Study with Summary Statistics
    ftp_server(ftp, study = 'MahajanA_29632382_GCST007517')

    #dir where the downloaded data will be saved at
    T2Ddir = "/Users/fernieqin/Desktop/DSC180B/T2D_data"

    try:
        #change to the data dir
        os.chdir(T2Ddir)      
    except OSError:
        #make a new dir if not existing
        os.mkdir(T2Ddir)
        print ("Successfully created the T2D data directory")
    else:
        print ("T2D data directory already exists")

    #dir where the downloaded person data will be saved at
    t2d_one_sub_dir = T2Ddir + "/" + study

    try:
        #change to the data dir
        os.chdir(t2d_one_sub_dir)      
    except OSError:
        #make a new dir if not existing
        os.mkdir(t2d_one_sub_dir)
        print ("Successfully created the sub directory %s" % t2d_one_sub_dir)
    else:
        print ("Sub directory %s already exists" % t2d_one_sub_dir)

    #change to the data dir
    os.chdir(t2d_one_sub_dir)

    for fn in t2d_file_listing:
        #check if the file already exists in the dir
        if os.path.exists(t2d_one_sub_dir + '/' + fn):
            print("File %s already exists" % fn)
        #download the file otherwise
        else:
            one_file = open(fn, "wb")
            ftp.retrbinary("RETR " + fn, one_file.write) 
            one_file.close()
            print("successfully downloaded the file: " + str(fn))
    
    #return to the parent dir ready for next call
    ftp.cwd('../')
    print(ftp.nlst())