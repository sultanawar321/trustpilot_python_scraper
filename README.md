# trustpilot_python_scraper
This repository includes a Python Module to scrap the public customers reviews data from [Trust-pilot](https://documentation-apidocumentation.trustpilot.com/business-units-api#get-a-business-unit's-reviews) using API keys. 
- To complete this scraping excercise; you need:
  - 1) Trustpilot API keys can be generated from your account, follow this [documentation](https://support.trustpilot.com/hc/en-us/articles/207309867-How-to-use-Trustpilot-APIs)
    2) Business Unit ID: follow this [documentation](https://documentation-apidocumentation.trustpilot.com/business-units-api-(public)#find-a-business-unit)
    3) 
# The project structure includes:
- trustpilot_scraper.py:
  - truspilot_scraping function: It paginates through pages to extract the data of public reviews on trustpilot of a given business
  - json_to_pandas function: It converts a nested JSON structure data obtained from an API response into a DataFrame.
    
# Python Packaging:
- requests=2.27.1
- pandas=1.1.5
- loguro=0.7.2
  
# Code Execution:
- To run the program file: python trustpilot_python_scraper.py

