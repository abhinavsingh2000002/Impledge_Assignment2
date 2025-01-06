from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


driver = webdriver.Chrome() 


driver.get("https://ecspro-qa.kloudship.com") 


username_field = driver.find_element(By.ID, "login-email")  
password_field = driver.find_element(By.ID, "login-password") 


username_field.send_keys("kloudship.qa.automation@mailinator.com") 
password_field.send_keys("Password1") 


password_field.send_keys(Keys.RETURN)


login_button = driver.find_element(By.ID, "login-btn")
login_button.click()

try:
    element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//*[@id='kloudShip-ecs-web']/app-root/app-sidenav/mat-sidenav-container/mat-sidenav-content/perfect-scrollbar/div/div[1]/div/app-home/div/div[2]/mat-card[8]/p[2]/span"))
    )

    element.click()
    print("Element clicked successfully!")
except Exception as e:
    print("Error finding or clicking the element:", e)


try:
    container_element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/app-sidenav/mat-sidenav-container/mat-sidenav-content/perfect-scrollbar/div/div[1]/div/app-dashboard/div/div[1]/app-package-type-list/perfect-scrollbar/div/div[1]/mat-card[1]/div[1]"))
    )
    container_element.click()
    print("Container Element clicked successfully!")
except Exception as e:
    print("Error finding or clicking the element:", e)


try:
    delete_element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/app-sidenav/mat-sidenav-container/mat-sidenav-content/perfect-scrollbar/div/div[1]/div/app-dashboard/div/div[1]/app-package-type-list/perfect-scrollbar/div/div[1]/mat-card[1]/div[2]/mat-icon"))
    )
    delete_element.click()
    print("Delete Element clicked successfully!")
except Exception as e:
    print("Error finding or clicking the element:", e)

try:
    confirm_delete_element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div[5]/div[2]/div/mat-dialog-container/app-alert-dialog/mat-card/div/button/span[1]"))
    )
    confirm_delete_element.click()
    print("Confirm Delete Element clicked successfully!")
except Exception as e:
    print("Error finding or clicking the element:", e)

try:
    three_dot_element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/app-sidenav/mat-sidenav-container/mat-sidenav-content/app-header/mat-toolbar/button[9]"))
    )
    three_dot_element.click()
    print(" Three Dot Icon Element clicked successfully!")
except Exception as e:
    print("Error finding or clicking the element:", e)


try:
    logout_element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div[5]/div[2]/div/div/div/button[6]"))
    )
    logout_element.click()
    print("Logout Element clicked successfully!")
except Exception as e:
    print("Error finding or clicking the element:", e)

time.sleep(5)

driver.quit()