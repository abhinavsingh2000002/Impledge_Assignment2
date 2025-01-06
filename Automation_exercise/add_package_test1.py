from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random


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
    Add_element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//*[@id='kloudShip-ecs-web']/app-root/app-sidenav/mat-sidenav-container/mat-sidenav-content/app-header/mat-toolbar/button[2]/span[1]/mat-icon"))
    )

    Add_element.click()
    print("Add_Element clicked successfully!")
except Exception as e:
    print("Error finding or clicking the element:", e)


try:
    name_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/app-root/app-sidenav/mat-sidenav-container/mat-sidenav-content/perfect-scrollbar/div/div[1]/div/app-dashboard/div/div[2]/app-package-type-manage/perfect-scrollbar/div/div[1]/mat-card/form/div/div[1]/section[1]/div/mat-form-field/div/div[1]/div/input"))
    )

    name_field.clear()
    name_field.send_keys("Abhinav_Singh")
    print("Name entered successfully!")
except Exception as e:
    print("Error finding or interacting with the input field:", e)


length_value = random.randint(1, 20)
width_value = random.randint(1, 20)
height_value = random.randint(1, 20)

try:
    length_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/app-root/app-sidenav/mat-sidenav-container/mat-sidenav-content/perfect-scrollbar/div/div[1]/div/app-dashboard/div/div[2]/app-package-type-manage/perfect-scrollbar/div/div[1]/mat-card/form/div/div[2]/section[1]/div/mat-form-field/div/div[1]/div/input"))
    )

    if length_value < 20:
        length_field.clear()
        length_field.send_keys(str(length_value))
        print(f"Value '{length_value}' entered successfully!")
    else:
        print(f"Value '{length_value}' is not less than 20. Input skipped.")
except Exception as e:
    print("Error finding or interacting with the input field:", e)


try:
    width_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/app-root/app-sidenav/mat-sidenav-container/mat-sidenav-content/perfect-scrollbar/div/div[1]/div/app-dashboard/div/div[2]/app-package-type-manage/perfect-scrollbar/div/div[1]/mat-card/form/div/div[2]/section[2]/div/mat-form-field/div/div[1]/div/input"))
    )
    if width_value < 20:
        width_field.clear()
        width_field.send_keys(str(width_value))
        print(f"Value '{width_value}' entered successfully!")
    else:
        print(f"Value '{width_value}' is not less than 20. Input skipped.")
except Exception as e:
    print("Error finding or interacting with the input field:", e)


try:
    height_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/app-root/app-sidenav/mat-sidenav-container/mat-sidenav-content/perfect-scrollbar/div/div[1]/div/app-dashboard/div/div[2]/app-package-type-manage/perfect-scrollbar/div/div[1]/mat-card/form/div/div[2]/section[3]/div/mat-form-field/div/div[1]/div/input"))
    )
    if height_value < 20:
        height_field.clear()
        height_field.send_keys(str(height_value))
        print(f"Value '{height_value}' entered successfully!")
    else:
        print(f"Value '{height_value}' is not less than 20. Input skipped.")
except Exception as e:
    print("Error finding or interacting with the input field:", e)


try:
    submit_element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//*[@id='kloudShip-ecs-web']/app-root/app-sidenav/mat-sidenav-container/mat-sidenav-content/perfect-scrollbar/div/div[1]/div/app-dashboard/div/div[2]/app-package-type-manage/mat-toolbar/button"))
    )

    submit_element.click()
    print("Element clicked successfully!")
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
