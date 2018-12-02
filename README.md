# LinkedIn-Post-Visualization
LinkedIn Post Visualization Tool

PURPOSE : <br>

LinkedIn Post Data Analytics Visualization tool <br>
Generates Horizontal Bar graph/chart for Company and Title Analytics <br>
Generates Pie chart for Company and Title Analytics <br>

Requirements: <br>
Windows 10 OS <br>
Python == 2.7.x <br>
Python modules (libraries) & Dependencies can be installed using pip <br>
Install tesseract v-4 in C:\Program Files (x86)\Tesseract-OCR from https://github.com/UB-Mannheim/tesseract/wiki  (set enviroment variable for it if required) <br>
Install Imagemagick from Sourceforge.net in C:\Program Files (set enviroment variable for it if required) <br>
chromedriver.exe based on your chrome browser <br> stored in a folder called drivers

Scripts to be updates and excuted : <br>

1]<br>
Open get_post.py and update the LinkedIn userid and path URL of your post till 'activity:' example :<br>
https://www.linkedin.com/in/ritesh-sharma29/detail/recent-activity/shares/ca/share-analytics/urn:li:activity: <br>
Post ID need to be passed as argument <br>
python get_post.py <postid> <br>
Example python get_post.py 6468885395999424512 <br>

screenshot.png will be genertaed <br>

2] <br>
Run crop.py <br>
python crop.py <br>
screenshot.png gets sliced in CROP folder into 3 <br>
Text files for company - 1.txt, Title - 2.txt and Location - 3.txt gets generated using tesseract <br>
Check Manually in all txt files Comapny,Title and Location starts with number on 5th line if not edit and save txt files

3] <br>
Update ext_txt.py https://www.linkedin.com/in/ritesh-sharma29/detail/recent with your LinkedIn URL till word recent <br>
Run ext_txt.py <br>
python ext_txt.py <postid> <br>
Example python ext_txt.py 6468885395999424512 <br>
Visualization charts will be generated 
 










