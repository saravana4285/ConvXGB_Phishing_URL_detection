# ConvXGB_Phishing_URL_detection
This repo stores implementation code of ConvXGB model to detect phishing URL
<H2> 1.Data Gathering </H2>
"1.txt2image_transformation.py" requires rec_id and url as input from mendeley phishing-url datasets.
This script has python selenium libraries to visit the given webpage and crawl the webpage as PNG format to local storage.
<H2> 2.EDA </H2>
Exploratory data analysis techniques are applied on the mendeley phishing url datasets.
<H2> 3.Data Pre-processing </H2>
Several tasks are performed in this data pre-processing section, includes but not limit to screen each image for complete white-background and purging,etc
<H2> 4.Data Validation </H2>
validation for quality of data, missing data, etc are done.
<H2> 5.Hypertuning experiments </H2>
several hyperparameters are tuned to build the final_model.
<H2> 6.Final_model </H2>
Final model provides the best outstanding performace.
