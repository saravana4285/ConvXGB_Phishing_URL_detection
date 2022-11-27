# ConvXGB_Phishing_URL_detection
Hello, This repository contains the step by step implementation of ConvXGB model in detecting Phishing URL on mendeley datasets.
The datasets can be freely downloaded at https://data.mendeley.com/datasets/n96ncsr5g4
<br>
<H2> 1.Data Gathering </H2>
you can just download all the files provided in mendeley dataset and extract them to single folder, then use the "1.txt2image_transformation.py" python script which requires only rec_id and url as input from mendeley phishing-url datasets to re-visit the url and crawl the webpage in PNG format.
This script uses python selenium libraries to re-visit the given webpage and crawl the webpage as PNG format to local storage.</br>
<H2> 2.EDA </H2>
Exploratory data analysis techniques are applied on the mendeley phishing url datasets.
<H2> 3.Data Pre-processing </H2>
Several tasks are performed in this data pre-processing section, which includes but not limit to screen each image for complete white-background and purging, data similarity check, test-train split, etc
<H2> 4.Data Validation </H2>
validation for quality of data, missing data, etc are done.
<H2> 5.Hypertuning experiments </H2>
several hyperparameters are tuned to build the final_model. each folder has jupyter notebook of experiment with outputs.
<H2> 6.Final_model </H2>
Final model provides the best outstanding performace.
