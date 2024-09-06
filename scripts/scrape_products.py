from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
import time

# Path to Edge WebDriver
driver_path = 'drivers/msedgedriver.exe'
service = webdriver.edge.service.Service(executable_path=driver_path)
driver = webdriver.Edge(service=service)

# Open the webpage for the data to scrape
driver.get('https://example.com/products')

wait = WebDriverWait(driver, 10)

wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'product')))

# Find all products on the page
products = driver.find_elements(By.CLASS_NAME, 'product')

# Opens a CSV file to save the data
with open('data/products.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Title', 'Description', 'Price'])  # Write header row

    # Loop through all products and extract the data
    for product in products:
        title = product.find_element(By.CLASS_NAME, 'product-title').text
        description = product.find_element(By.CLASS_NAME, 'product-description').text
        price = product.find_element(By.CLASS_NAME, 'product-price').text

        writer.writerow([title, description, price])

# Close the browser
driver.quit()

print("Data has been scraped and saved to products.csv")
