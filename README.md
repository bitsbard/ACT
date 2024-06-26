# ACT (Automated Conversion Tasks)

ACT automates the process of converting task data into images, extracting information from those images, and updating tasks based on the extracted information. This tool is designed to fit into a larger project aimed at automating the replacement of tasks on an existing UI, leveraging computer vision to detect characters and perform automated replacements.

## Setup Instructions

### Prerequisites

- Python 3.6+
- pip

### Setting Up

1. **Clone the Repository**

   ```bash
   git clone https://github.com/bitsbard/ACT.git
   cd ACT
   ```

2. **Create and Activate Virtual Environment**

   - **Windows:**

     ```bash
     python -m venv myenv
     myenv\Scripts\activate
     ```

   - **macOS and Linux:**

     ```bash
     python3 -m venv myenv
     source myenv/bin/activate
     ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

### Running the Code

```bash
python main.py
```
