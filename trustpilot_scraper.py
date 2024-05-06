"""Python Module to scrap public customers reviews data from Trustpilot"""

# import packages and libraries
import time
from datetime import datetime, timedelta
import requests
import pandas as pd
from loguru import logger


# Get the specific date; change the number based on how many days are required
SPECIFIC_DATE = datetime.now().date() - timedelta(days=2)

HEADERS = {"apikey": "xxx"} # Add the API access key here

# create global variables
REVIEWS_PER_PAGE = 100
BUSINESS_UNIT_ID = "xxx" # Add the business unit id here


def truspilot_scraping(
    business_unit_id: str,
    reviews_per_page: int,
    headers: dict,
    specific_date: pd.to_datetime,
) -> list:
    """
    This function paginates through pages to extract the data of public reviews on trustpilot
    """
    base_url = "https://api.trustpilot.com/v1/business-units/"
    results = []
    # Form the URL by combining the base URL, business unit ID, and reviews per page parameter
    url = f"{base_url}{business_unit_id}/reviews?perPage={reviews_per_page}"
    # Loop to fetch reviews from the URL until all pages have been retrieved
    while True:
        # Send a GET request to the specified URL with the provided headers
        response = requests.request("GET", url, headers=headers)
        # Convert data to json format
        json = response.json()
        reviews = json["reviews"]
        # Filter relevant reviews based on creation date
        relevant_reviews = [
            review
            for review in reviews
            if pd.to_datetime(review.get("createdAt")).date() >= specific_date
        ]
        # If no relevant reviews are found or list empty, exit the loop
        if not relevant_reviews:
            break
        else:
            results.extend(relevant_reviews)
            # Extract the pagination links from the JSON data
            links = json["links"]
            # Find the link for the next page, if it exists
            next_page = [l for l in links if l["rel"] == "next-page"]
            if next_page:
                [next_page] = next_page
                url = next_page["href"]
            else:
                # If no next page link is found, exit the loop
                break
            # Add a delay to prevent overwhelming the server with requests
            time.sleep(0.2)
    return results


def json_to_pandas(business_unit_id: str, results: list) -> pd.DataFrame:
    """
    This function converts a nested JSON structure obtained from an API response into a DataFrame.
    """
    # load the json results to pandas
    df_reviews = pd.json_normalize(results)
    logger.info(f"Available Data Attributes : {df_reviews.columns}")
    logger.info(
        f"Total number of reviews for company with id '{business_unit_id}' is : {len(df_reviews)}"
    )
    return df_reviews


def main():
    """Combines the functions"""
    results = truspilot_scraping(
        BUSINESS_UNIT_ID, REVIEWS_PER_PAGE, HEADERS, SPECIFIC_DATE
    )
    df_reviews = json_to_pandas(BUSINESS_UNIT_ID, results)
    return df_reviews


if __name__ == "__main__":
    main()
