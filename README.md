# Friends-TV-show-Analysis

## INPUT folder
The input folder contain a csv obtained from kaggle. That csv is a dataset with all the episodes, seasons, characters and script lines. 

## SRC folder
Include different files:

#### cleaningdataaset 
It is a file with the code needed to filter the data of the original dataset. 

#### web_scraping
In order to complete the dataset web scraping was performed. The rating of each episode obtained from https://www.imdb.com/search/title/ web was introduce in the data.

#### functions 
It is a file which includes all the functions needed to complete the code and make it work.

#### graphs
This file includes the operations performed to the dataset in order to obtain conclusions and final results. All the result were plotted in different graphs.

#### ImageAndQuotesScraping
Again web scraping was performed to obtain the main quotes of each characters and their images. 

#### sendEmail 
There is an option in which you can send and email to a desired person. This file includes the code to accomplish this task.

#### main 
It is the principal code of the program. 

## OUTPUT folder
Include the filtered CSV, the obtained graphs, main character's images and the PDF. 

The program can recibe different arguments. Depending on the character name it receives, it generates a PDF with the quote, image and graph corresponding with the selected character. If nothing is selected, the PDF include all the report. 
Finally there is an option which allows to send an email with the PDF. 
