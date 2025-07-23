import os  # Import os module to handle directory and file paths
import time  # Import time module to generate timestamps for screenshot filenames

def take_screenshot(driver, name="screenshot"):
    # Create the screenshots directory if it doesn't exist
    screenshots_dir = os.path.join(os.getcwd(), "screenshots")  # Set the path for the screenshots directory in the current working directory
    os.makedirs(screenshots_dir, exist_ok=True)  # Create the directory if it doesn't already exist

    # Generate file name with timestamp
    timestamp = time.strftime("%Y%m%d-%H%M%S")  # Get the current time in a specific format for uniqueness
    file_path = os.path.join(screenshots_dir, f"{name}_{timestamp}.png")  # Create the full file path for the screenshot

    # Take the screenshot and save
    driver.save_screenshot(file_path)  # Use Selenium WebDriver's save_screenshot method to capture and save the screenshot

    return file_path  # Return the file path of the saved screenshot for reference