import time
import requests
from bs4 import BeautifulSoup
import csv

def my_code():

    # Function to scrape data from a webpage
    def scrape_data(url):
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            data = []
    #         print(soup)
            # Replace the following code with the appropriate HTML elements and classes for the data you want to scrape
            for item in soup.find_all('div', id='qlook'):
    #             print(item)
                 Temperature = item.find('div', class_="h2").text.strip()
                 print(Temperature)
                 weather_status= item.find('p').text.strip()
                 print(weather_status)

            data.append({"Temperature": Temperature, "weather_status": weather_status})

            return data
        else:
            print(f"Failed to fetch data from {url}. Status Code: {response.status_code}")
            return []

    # # Replace 'YOUR_URL_HERE' with the URL of the webpage you want to scrape
    url = 'https://www.timeanddate.com/weather/india/bengaluru'
    scraped_data = scrape_data(url)

    # Define the path where you want to save the CSV file
    csv_file_path = "C:/Users/Dell/Desktop/scraped_data.csv"

    # # Save the scraped data to a CSV file
    # with open(csv_file_path, 'w', newline='') as csvfile:
    #     fieldnames = ["Temperature", "weather_status"]
    #     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    #     writer.writeheader()
    #     writer.writerows(scraped_data)



    existing_data = []
    try:
        with open(csv_file_path, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            existing_data = [row for row in reader]
    except FileNotFoundError:
        print("No existing data found. A new CSV file will be created.")

    # Combine existing data with the newly scraped data
    all_data = existing_data + scraped_data

    # Save the combined data to a CSV file
    with open(csv_file_path, 'w', newline='') as csvfile:
        fieldnames = ["Temperature", "weather_status"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(all_data)


    print("Data has been scraped and saved successfully to scraped_data.csv.")
    print("Executing my code!")
    
while True:
    my_code()
    time.sleep(10)    
    
