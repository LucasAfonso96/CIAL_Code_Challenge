# CIAL/Pasquali Code Challange

## Technical Overview

This repository contains Python scripts for a RESTful API web application  designed to fetch stock data from an external financial API and scrape data from the MarketWatch financial website.The application comprises two main routes:

1. **GET Route**: This route retrieves stock data for a given symbol from the external financial API. It saves the data into a database and outputs the results in JSON format.
   
2. **POST Route**: Responsible for updating the stock entity with the purchased amount. 


### Features
- **FastAPI Framework**: Utilizes FastAPI for creating robust and high-performance API endpoints.
- **Data Retrieval**: Fetches stock data from an external financial API and scrapes relevant information from MarketWatch.
- **RESTful API**: Offers a clean and structured interface for accessing stock data and managing stock entities.
- **JSON Output**: Outputs data in JSON format, ensuring compatibility and ease of integration with other systems.

- **Observation**: I mock MarketWatch scraping function response due to the issue mentioned in the previous email.


## Instalation and Run Project

### Windows

1. **Install Docker Desktop:**
   - Download and install [Docker Desktop](https://www.docker.com/products/docker-desktop) for Windows.

2. **Open PowerShell or Command Prompt:**
   - Open PowerShell or Command Prompt on your computer.

3. **Build Docker Image:**
   - Navigate to the directory containing the Dockerfile.
   - Run the following command to build the Docker image:
     ```
     docker build -t stock_api .
     ```

4. **Run Docker Container:**
   - Run the following command to execute the Docker container and provide input via stdin:
     ```
        docker run -p 8000:8000 stock_api
     
     ```

### Linux & macOS

1. **Install Docker:**
   - Install Docker Engine by following the instructions for [Linux](https://docs.docker.com/engine/install/) or [macOS](https://docs.docker.com/docker-for-mac/install/).

2. **Open Terminal:**
   - Open Terminal on your computer.

3. **Build Docker Image:**
   - Navigate to the directory containing your Dockerfile.
   - Run the following command to build the Docker image:
     ```
     docker build -t stock_api
     ```

4. **Run Docker Container:**
   - Run the following command to execute the Docker container and provide input via stdin:
     ```
     docker run -p 8000:8000 stock_api
     ```


## Environment Variables

This project utilizes environment variables for configuration. A `.env_example` file is provided with the necessary keys. To configure your environment, follow these steps:

1. **Create a .env File**: Create a new file named `.env` in the root directory of the project.

2. **Copy Environment Variables**: Open the `.env_example` file and copy the environment variables listed there.

3. **Paste into .env File**: Paste the copied environment variables into the newly created `.env` file.

4. **Set Values**: Replace the placeholder values with your actual API keys, credentials, or other sensitive information.

### Observation
    I pass the values in the .env_example because this is a test environment and to provide ease of use for running this project. In a professional way, I would never do this



## Running Unit Tests with Pytest

To run the unit tests with Pytest, navigate to the `tests` folder and run Pytest:

1. Change directory to the `tests` folder:
    ```
    cd tests
    ```

2. Run Pytest:

    ```
    pytest
    ```

This will execute all the unit tests in the `tests` directory.


## Notes

- In the function to fetch polygon data i have to change the date to the day before today, because was giving me a error : "Attempted to request today's data before end of day. Please upgrade your plan at https://polygon.io/pricing"

