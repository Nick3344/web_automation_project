'''from selenium import webdriver
from selenium.webdriver.edge.service import Service  # Import Service class
from selenium.webdriver.common.by import By
import time

# Path to your Edge WebDriver
driver_path = '../drivers/msedgedriver.exe'

# Initialize the Edge WebDriver with the Service class
service = Service(executable_path=driver_path)
driver = webdriver.Edge(service=service)

# Open a webpage (for example, google.com)
driver.get('https://www.google.com')

# Wait for 5 seconds to see the browser action
time.sleep(5)

# Close the browser
driver.quit()'''

"""from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Path to your Edge WebDriver
driver_path = 'drivers/msedgedriver.exe'
service = webdriver.edge.service.Service(executable_path=driver_path)
driver = webdriver.Edge(service=service)

# Open the webpage (replace with the target URL)
driver.get('https://www.theforage.com/login')

# Wait for the page to load
time.sleep(5)

# Find and fill out form fields (use actual IDs, names, or XPaths of elements)
# Example: Filling out a username field
username_field = driver.find_element(By.ID, 'name')
username_field.send_keys('durby731@gmail.com')

# Example: Filling out a password field
password_field = driver.find_element(By.ID, 'Password')
password_field.send_keys('2paq_fMZDdRD5Ef')

# Example: Submitting the form
submit_button = driver.find_element(By.ID, 'Login')
submit_button.click()

# Wait to observe the result
time.sleep(5)

# Close the browser
driver.quit()"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Path to Edge WebDriver
driver_path = 'drivers/msedgedriver.exe'
service = webdriver.edge.service.Service(executable_path=driver_path)
driver = webdriver.Edge(service=service)

# Open the webpage with credentials
driver.get('https://www.theforage.com/login')
username = 'example@gmail.com'
password = 'example-password'

wait = WebDriverWait(driver, 10)

# Fill out login form
username_field = wait.until(EC.presence_of_element_located((By.NAME, 'email')))
username_field.send_keys(username)

password_field = wait.until(EC.presence_of_element_located((By.NAME, 'password')))
password_field.send_keys(password)

# Click the login button using XPath
#submit_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit' and contains(text(), 'Login')]")))
#submit_button.click()

submit_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input:where([type=\'submit\']')))
submit_button.click()

# Wait for the next page to load
time.sleep(5)

# Close the browser
driver.quit()


""""# Wait for the dashboard to load
dashboard_element = wait.until(EC.presence_of_element_located((By.ID, 'dashboard')))

# Navigate to the profile page
profile_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'Profile')))
profile_link.click()

# Extract user info
user_name = driver.find_element(By.ID, 'user_name').text
print("Logged in as:", user_name)

# Optional: Log out
logout_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Logout']")))
logout_button.click()

# Close the browser
driver.quit()"""




