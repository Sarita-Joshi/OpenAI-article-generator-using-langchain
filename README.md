# Article Generator Web App

## Overview

This Article Generator Web App allows users to generate articles based on specific parameters using OpenAI's GPT-3.5. The app provides an intuitive interface for users to input various parameters such as topic, keywords, length, tone, audience, and purpose. The generated article is displayed in a responsive layout, allowing users to easily interact with and review their content.

## Features

- **Dynamic Form**: Allows users to input and configure article parameters including topic, keywords, outline, length, tone, audience, and purpose.
- **Article Generation**: Uses OpenAI's GPT-3.5 to generate articles based on the provided parameters.
- **Responsive Layout**: The interface is designed to adapt and display the form and generated article side by side after submission.
- **Text Justification**: The generated article text is justified for better readability.

## Requirements

- Python 3.8+
- Streamlit
- OpenAI Python package

## Installation

1. **Clone the Repository**

   ```
   git clone https://github.com/your-username/article-generator-webapp.git
   cd article-generator-webapp
   ```

2. **Create and Activate a Virtual Environment**

   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**

   ```
   pip install -r requirements.txt
   ```

4. **Set Up OpenAI API Key**

   Replace `'your-openai-api-key'` in the code with your actual OpenAI API key. You can obtain an API key by signing up at [OpenAI](https://www.openai.com/).

## Usage

1. **Run the Streamlit App**

   ```
   streamlit run app.py
   ```

2. **Access the App**

   Open your web browser and go to `http://localhost:8501` to interact with the app.

3. **Input Parameters**

   - **Topic**: Enter the main topic of the article.
   - **Keywords**: Add relevant keywords.
   - **Outline**: Provide a comma-separated outline of the article.
   - **Length**: Specify the desired length of the article in words.
   - **Tone**: Choose the tone of the article.
   - **Audience**: Select the target audience.
   - **Purpose**: Define the purpose of the article.

4. **Generate Article**

   Click the "Generate Article" button to create the article. The form will shift to one side, and the generated article will be displayed on the other.
