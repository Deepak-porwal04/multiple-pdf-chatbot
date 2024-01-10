# Multi-language PDF Chatbot using Gemini Pro

## Overview

This project is a multi-language PDF chatbot powered by Gemini Pro. It allows users to upload PDF documents, process them, and ask questions about their content. The chatbot utilizes Google Generative AI for text embeddings, Faiss for creating and searching vector stores, and Streamlit for the user interface.

## Table of Contents

- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Environment Setup](#environment-setup)
  - [API Key](#api-key)
  - [Running the Application](#running-the-application)

- [Contributing](#contributing)
  - [Bug Reports and Feature Requests](#bug-reports-and-feature-requests)
  - [Code Contributions](#code-contributions)

## Project Structure

The project is organized into several directories:

- **`configuration`**
  - **`config.py`**: Handles the loading of the API key from the .env file.

- **`constants`**
  - **`constant.py`**: Contains constant values used throughout the project.

- **`src`**
  - **`embeddings.py`**: Initializes Google Generative AI Embeddings and creates/saves a vector store.
  - **`pdf_processing.py`**: Extracts text from PDFs and splits it into overlapping chunks using a recursive character-based approach.
  - **`pipeline.py`**: Orchestrates the processing of PDFs, including text extraction, chunk creation, and vector store generation.
  - **`question_answering.py`**: Manages the question-answering pipeline, including processing PDFs, loading vector stores, and generating answers.
  - **`vectorstore.py`**: Handles the loading and searching of vector stores using Faiss.
  - **`views.py`**: Defines the Streamlit user interface for interacting with the chatbot.

- **`app.py`**: The main script to run the application.

- **`.env`**: Contains sensitive information such as the API key. This file should not be shared.

## Getting Started

### Prerequisites

- Python (>=3.9)
- Other prerequisites are mentioned in requirements.txt

### Environment Setup

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/multi-language-pdf-chatbot.git
   cd multi-language-pdf-chatbot

2. **Create a virtual environment:**
    ```bash
    conda create -p venv python==3.9
    ```
    ```bash
    conda activate venv/
    ```

3. **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
4. **create a .env file in project root, and write:**
```bash
GOOGLE_API_KEY = 'your_api_key_here'
```

### API Key

- visit https://makersuite.google.com/

- Click on *Get API key*

- Now click on *Create API key in new project*

- Copy the API Key and keep it secure


### Running the Application

- After having the [Environment Setup](#environment-setup). Run the following command:
```bash
streamlit run app.py
```

## Contributing

Contributions are most welcomed. If you're interested in improving this project, here's how you can get involved:

### Bug Reports and Feature Requests

If you come across any issues or have ideas for new features, please let me know by [opening an issue](https://github.com/Deepak-porwal04/multiple-pdf-chatbot/issues). Provide detailed information about the problem or your feature request, and we'll do our best to address it.

### Code Contributions

If you'd like to contribute code to this project, follow these simple steps:

1. **Fork the Repository:**
   - Click on the "Fork" button at the top right of the [project repository](https://github.com/Deepak-porwal04/multiple-pdf-chatbot) page.

2. **Clone Your Fork:**
   - Clone your forked repository to your local machine.
     ```bash
     git clone https://github.com/Deepak-porwal04/multiple-pdf-chatbot.git
     cd multiple-pdf-chatbot
     ```

3. **Create a Branch:**
   - Create a new branch for your changes.
     ```bash
     git checkout -b feature-or-fix-branch
     ```

4. **Make Changes:**
   - Make your code changes and improvements.

5. **Commit Changes:**
   - Commit your changes with a descriptive commit message.
     ```bash
     git add .
     git commit -m "Your descriptive commit message"
     ```

6. **Push Changes:**
   - Push your changes to your fork on GitHub.
     ```bash
     git push origin feature-or-fix-branch
     ```

7. **Submit a Pull Request:**
   - Open a pull request (PR) against the main repository.
   - Provide a clear title and description for your PR.

I'll review your contributions and work with you to integrate them into the project.