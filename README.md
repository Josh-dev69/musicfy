# Musicify - Personalized Music Recommendation System

Musicify is a web application that provides personalized music recommendations based on user preferences and listening history. Powered by Django, Bootstrap, and the Spotify API, Musicify offers a seamless experience for discovering new music tailored to individual tastes.

## Features

- **User Authentication**: Secure user registration and login system to personalize recommendations for each user.
- **Music Recommendations**: Utilizes Spotify's extensive music catalog and recommendation algorithms to suggest songs and playlists based on user preferences.
- **Liked Songs**: Allows users to save and manage their favorite songs for future reference.
- **Search Functionality**: Enables users to search for specific artists, albums, or tracks within the Spotify database.
- **Responsive Design**: Fully responsive user interface optimized for desktop, tablet, and mobile devices.

## Technologies Used

- **Django**: Python web framework for building the backend logic and handling user authentication.
- **Bootstrap**: Frontend framework for creating responsive and visually appealing user interfaces.
- **Spotify API**: Integration with the Spotify API to fetch music data and recommendations.
- **HTML/CSS**: Markup and styling languages for structuring and designing the web pages.
- **JavaScript**: Client-side scripting language for dynamic interactivity and asynchronous requests.

## Setup Instructions

1. Clone the repository: `git clone https://github.com/Josh-dev69/musicify.git`
2. Navigate to the project directory: `cd musicify`
3. Install dependencies: `pip install -r requirements.txt`
4. Configure Spotify API credentials in `settings.py`.
5. Run migrations: `python manage.py migrate`
6. Start the development server: `python manage.py runserver`
7. Access the application in your browser at `http://localhost:8000`

## Project Structure

- **music_recommender_project**: Django app directory containing views, models, templates, and static files.
- **templates**: HTML templates for rendering frontend pages.
- **static**: Contains CSS, JavaScript, and image files for styling and interactivity.
- **requirements.txt**: List of Python dependencies for the project.

## Contributing

Contributions are welcome! Feel free to open issues for any bugs or feature requests. Pull requests are also encouraged for adding new features or fixing existing issues.