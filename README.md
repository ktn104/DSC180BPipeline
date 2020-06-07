# DSC180BPipeline
Our pipeline runs on a small data set but the images it produces is not very significant because the data is to small. When we run the data on the actual data we are using the images are much better and meaningful to analyze. 
Our pipleine allows you to download data from the GWAS Catalog, Clean the data, Merge the data, and then create plots such as Q-Q plots, P-value Histograms, and Manhattan Plots. These plots allow you to analyze the GWAS data and to determine which SNPs are significant.
To run the pipepline on the sample data in the direction run this command in the terminal:
  python run.py test-project
To run the data downloading portion run this command:
  python run.py test
To run the cleaning and plot making portion run this command:
  python run.py clean
You can modify the code to work for you specific trait you are analyzing from the GWAS Catalog in the data collection portion and the whole pipeline should work
