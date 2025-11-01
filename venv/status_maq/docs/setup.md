# Setup Instructions for Status das Máquinas Project

## Prerequisites

Before you begin, ensure you have the following installed on your machine:

- Python 3.7 or higher
- pip (Python package installer)

## Installation Steps

1. **Clone the Repository**

   Open your terminal and run the following command to clone the repository:

   ```
   git clone https://github.com/yourusername/status_maq.git
   ```

   Replace `yourusername` with your GitHub username.

2. **Navigate to the Project Directory**

   Change into the project directory:

   ```
   cd status_maq
   ```

3. **Create a Virtual Environment (Optional but Recommended)**

   It is recommended to create a virtual environment to manage dependencies. You can create one using the following command:

   ```
   python -m venv venv
   ```

   Activate the virtual environment:

   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```
     source venv/bin/activate
     ```

4. **Install Dependencies**

   Install the required Python packages using pip:

   ```
   pip install -r requirements.txt
   ```

5. **Run the Application**

   You can start the application by running:

   ```
   streamlit run app.py
   ```

   This will open the application in your default web browser.

## Usage

Once the application is running, you can input the status of machines by sector and view visualizations of the data.

## Additional Information

For more details on how to use the application, refer to the `README.md` file in the project directory.