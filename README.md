# Web-Scraping
Web scraping VTU results website to obtain the results pertaining to a semester.<br>
This project scrapes results for 5th Semester CBCS Scheme, to scrape results for any other semester changes the subject codes in the Results.py file accordingly

## Pre-requisites
  - Python3 with the following packages
    * requests
    * bs4(Beautiful Soup)
    * pandas
  - Working Internet Connection
  
 ## Running the project
 Clone the repository
 ```
  git clone git@github.com:harshasridhar/Web-Scraping.git
  ```
  ```sh
  cd Web_scraping
  ```
  In case you don't have the packages install, run the following command
  ```
  pip3 install -r dependencies.txt
  ```
  Run the file to scrape the results
  #### Note: Before running the Rsults.py file, include the USNs for which the results have to be obtained (Line 40)
  ```
  python3 Results.py
  ```
