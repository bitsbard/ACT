import cv2
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pytesseract

# Create a mock dataframe
data = {
    'Task ID': [1, 2, 3, 4, 5],
    'Current Task': ['Inspect chip', 'Replace capacitor', 'Test voltage', 'Calibrate sensor', '¥'],
    'New Task': ['Test chip', 'Replace resistor', 'Check current', 'Align sensor', '$']
}

# Convert the dictionary into a pandas dataframe
df = pd.DataFrame(data)
df.to_excel('mock_tasks.xlsx', index=False)

# Load the mock tasks spreadsheet
df = pd.read_excel('mock_tasks.xlsx')

# Function to convert dataframe to image
def dataframe_to_image(df, path):
    fig, ax = plt.subplots()
    ax.axis('tight')
    ax.axis('off')
    table = ax.table(cellText=df.values, colLabels=df.columns, cellLoc='center', loc='center')
    fig.savefig(path, bbox_inches='tight')

# Convert dataframe to image
image_path = 'mock_tasks.png'
dataframe_to_image(df, image_path)

# Function to extract text from image using pytesseract
def extract_text_from_image(image_path):
    img = cv2.imread(image_path)
    if img is None:
        return None
    text = pytesseract.image_to_string(img)
    return text

# Function to update the tasks in the dataframe based on detected text
def update_tasks_with_detected_text(task_data, detected_text):
    updated_tasks = task_data.copy()
    for index, row in task_data.iterrows():
        current_task = row['Current Task']
        new_task = row['New Task']
        if current_task in detected_text:
            updated_tasks.at[index, 'Current Task'] = new_task
            updated_tasks.at[index, 'New Task'] = ''
    return updated_tasks

# Extract text from the image
detected_text = extract_text_from_image(image_path)

# Update tasks based on detected text
if detected_text:
    updated_tasks = update_tasks_with_detected_text(df, detected_text)
    updated_tasks.to_excel('updated_tasks.xlsx', index=False)
