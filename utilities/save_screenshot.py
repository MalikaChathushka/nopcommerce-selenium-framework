import os
import time

def take_screenshot(driver, name="screenshot"):

    # Create the screenshots directory if it doesn't exist
    screenshots_dir = os.path.join(os.getcwd(), "screenshots")
    os.makedirs(screenshots_dir, exist_ok=True)

    # Generate file name with timestamp
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    file_path = os.path.join(screenshots_dir, f"{name}_{timestamp}.png")

    # Take the screenshot and save
    driver.save_screenshot(file_path)

    return file_path