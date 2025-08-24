# BookGenie

[![Python](https://img.shields.io/badge/Python-3.9-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.3-lightgrey)](https://flask.palletsprojects.com/)
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-1.3-yellowgreen)](https://scikit-learn.org/)
[![License](https://img.shields.io/badge/License-MIT-informational)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Active-success)]()

![](https://github.com/aysh34/BookGenie/blob/main/BookGenie.png)
## Overview

BookGenie is an intelligent book recommendation platform that helps readers discover their next favorite book through advanced machine learning algorithms. The application combines collaborative filtering and popularity-based recommendation systems to provide personalized book suggestions based on user preferences and reading patterns.

Built with Python and Flask, BookGenie analyzes large datasets of book ratings and user interactions to deliver accurate and relevant recommendations. Whether you're looking for your next great read or exploring new genres, BookGenie simplifies book discovery by understanding your unique reading taste.

## Features

- **Personalized Recommendations**: Advanced machine learning algorithms analyze reading patterns to suggest books tailored to individual preferences
- **Trending Books Discovery**: Explore the most popular and highly-rated books across different genres and time periods
- **Intuitive Web Interface**: Clean, responsive design that works seamlessly across desktop and mobile devices
- **Hybrid Recommendation System**: Combines collaborative filtering and popularity-based algorithms for accurate suggestions
- **Real-time Processing**: Fast recommendation generation with optimized data processing and caching
- **Scalable Architecture**: Modular design built for easy maintenance and future enhancements

## Installation

### Prerequisites

- Python 3.9 or higher
- pip package manager
- Virtual environment (recommended)

### Setup Instructions

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

### Running the Application

1. **Start the Flask server:**

   ```bash
   python app.py
   ```

2. **Access the application:**
   
   Open your web browser and navigate to `http://localhost:5000`

### Getting Recommendations

1. Navigate to the "Get Recommendations" page
2. Enter the title of a book you enjoyed
3. Click "Recommend" to receive personalized suggestions
4. Explore the recommended books with detailed information and ratings

### Exploring Trending Books

Visit the "Top Trending Books" page to discover currently popular books based on community ratings and engagement.

## Project Structure

```
BookGenie/
│
├── Data/                 # Book datasets and processed data files
├── Models/              # Trained machine learning models (pickle files)
├── static/              # CSS, JavaScript, and image assets
│   └── css/            # Custom stylesheets
├── templates/           # HTML templates for the web interface
│   ├── includes/       # Reusable template components
│   ├── index.html      # Homepage
│   ├── recommend.html  # Recommendation page
│   └── trending.html   # Trending books page
├── app.py              # Main Flask application
├── requirements.txt    # Python dependencies
└── README.md          # Project documentation
```

## Recommendation System

BookGenie employs a sophisticated hybrid recommendation system that combines multiple approaches to deliver accurate and personalized book suggestions.

### Popularity-Based Filtering

The system identifies trending and highly-rated books by analyzing:
- Overall book ratings and review scores
- Number of readers and engagement metrics
- Recent popularity trends and community feedback

### Collaborative Filtering

Advanced collaborative filtering uses machine learning to:
- Analyze user reading patterns and preferences
- Calculate similarity between users based on book ratings
- Generate recommendations using cosine similarity algorithms
- Identify books that similar readers have enjoyed

This hybrid approach ensures that users receive both popular, well-regarded books and personalized recommendations based on their unique reading history and preferences.

## Technology Stack

- **Backend**: Python, Flask
- **Machine Learning**: Scikit-learn, NumPy, Pandas
- **Frontend**: HTML5, CSS3, Bootstrap 5
- **Data Processing**: Pickle for model serialization
- **Deployment**: Vercel, Heroku support included

## Contributing

We welcome contributions to improve BookGenie. To contribute:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/improvement`)
3. Make your changes and test thoroughly
4. Commit your changes (`git commit -am 'Add new feature'`)
5. Push to the branch (`git push origin feature/improvement`)
6. Open a Pull Request with a clear description of your changes

Please ensure your code follows the existing style and includes appropriate documentation.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for complete details.

## Support

For questions, bug reports, or feature requests, please open an issue on the [GitHub repository](https://github.com/aysh34/BookGenie/issues). I appreciate your feedback and will respond as soon as possible.
