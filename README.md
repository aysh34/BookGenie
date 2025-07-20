# BookGenie

[![Python](https://img.shields.io/badge/Python-3.9-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.3-lightgrey)](https://flask.palletsprojects.com/)
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-1.3-yellowgreen)](https://scikit-learn.org/)
[![License](https://img.shields.io/badge/License-MIT-informational)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Active-success)]()

## Overview

BookGenie is a robust, machine learning-powered application that delivers personalized book recommendations based on user preferences and reading history. By leveraging advanced recommendation algorithms, BookGenie analyzes user interactions and book metadata to suggest titles tailored to individual interests, streamlining the discovery of new books.

## Features

- Personalized recommendations using collaborative and content-based filtering
- Advanced search by title, author, or genre
- Interactive dashboard for exploring recommendations and insights
- Scalable and modular codebase for easy extension

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/aysh34/BookGenie.git
   cd BookGenie
   ```

2. **Create and activate a virtual environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Configure environment variables:**

   - Create a `.env` file in the root directory.
   - Add required API keys and configuration settings as described in `.env.example`.

2. **Run the application:**

   ```bash
   python app.py
   ```

3. **Access the dashboard:**
   - Open your browser and navigate to `http://localhost:5000`.

## Deployment

### Deploy on Vercel

1. **Prerequisites:**

   - Ensure your code is pushed to a GitHub repository
   - Sign up for a free account at [vercel.com](https://vercel.com)

2. **Deploy:**

   - Import your GitHub repository on Vercel
   - Select "Other" as framework preset
   - Deploy with default settings
   - Vercel will automatically detect the configuration from `vercel.json`

3. **Environment Variables (Optional):**
   - Set `SECRET_KEY` in Vercel's environment variables for enhanced security

### Deploy on Heroku

1. **Install Heroku CLI and login:**

   ```bash
   heroku login
   ```

2. **Create and deploy:**
   ```bash
   heroku create your-app-name
   git push heroku main
   ```

The `Procfile` is already configured for Heroku deployment.

## Project Structure

```
BookGenie/
│
├── data/                # Datasets and data processing scripts
├── models/              # Machine learning models
├── app.py               # Main application entry point
├── requirements.txt     # Python dependencies
├── README.md            # Project documentation
└── ...
```

## Recommendation Logic

BookGenie employs a hybrid recommendation system combining collaborative filtering and popularity-based filtering.

### 1. Popularity-Based Filtering

- Aggregates books with highest ratings and number of readers

### 2. Collaborative Filtering

- Uses cosine similarity on a pivot table of users × books
- Recommends books that are similar in reading patterns

## Contributing

Contributions are encouraged and appreciated. Please open an issue or submit a pull request for enhancements or bug fixes. For detailed contribution guidelines, refer to [CONTRIBUTING.md](CONTRIBUTING.md).

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For questions, support, or feedback, please open an issue on the [GitHub repository](https://github.com/aysh34/BookGenie/issues).
