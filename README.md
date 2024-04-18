# Musicify - Personalized Music Recommendation System


This Django project is a music recommender system that provides personalized music recommendations based on user preferences. It integrates with the Spotify API to fetch music data and utilizes content-based filtering algorithms to generate recommendations.

## Project Structure

music_recommender_project/
├── users/ # Django app for user authentication and profile management
│ ├── migrations/ # Database migrations
│ ├── templates/ # HTML templates for user authentication and profile management
| |   ├── static/ # Static files (e.g., CSS)
│ └── style.css # Custom CSS styles  
│ ├── admin.py # Admin configurations
│ ├── forms.py # Forms for user authentication and profile management
│ ├── models.py # User profile model definition
│ ├── urls.py # URL patterns for user authentication and profile management
│ └── views.py # Views for user authentication and profile management
├── music_recommender/ # Django app for music recommendation functionality
│ ├── migrations/ # Database migrations
│ ├── templates/ # HTML templates for music recommendations
│ ├── admin.py # Admin configurations
│ ├── models.py # Music track model definition
│ ├── urls.py # URL patterns for music recommendations
│ └── views.py # Views for music recommendations
├── api_integration/ # Integration with the Spotify API
│ ├── spotify_api.py # Functions to authenticate and interact with the Spotify API
│ └── spotify_data.py # Functions to fetch music data from Spotify
├── music_recommender_project/ # Django project settings and configurations
│ ├── settings.py # Project settings
│ ├── urls.py # Project URL patterns
│ └── wsgi.py # WSGI application entry point
├── db.sqlite3 # SQLite database file (default for Django projects)
├── manage.py # Django management script
├── README.md # Project documentation
└── requirements.txt # Python package dependencies

## Features

- User authentication and authorization system.
- User profile management with preferences such as favorite genre and artist.
- Integration with the Spotify API to fetch music data.
- Content-based filtering algorithm to enhance recommendations.
- Responsive web interface for easy access on various devices.

## Technologies Used

- **Django**: Python web framework for building the backend logic and handling user authentication.
- **Bootstrap**: Frontend framework for creating responsive and visually appealing user interfaces.
- **Spotipy**: A python Framework to Integrate the Spotify API to fetch music data and recommendations.
- **HTML/CSS**: Markup and styling languages for structuring and designing the web pages.
- **JavaScript**: Client-side scripting language for dynamic interactivity and asynchronous requests.

## Setup Instructions

1. Clone the repository: `git clone https://github.com/Josh-dev69/musicify.git`
2. Navigate to the project directory: `cd musicify`
3. Install the required python packages: `pip install -r requirements.txt`
4. Run migrations: `python manage.py migrate`
5. Create a superuser(for admin access): `python manage.py createsuperuser`
6. Start the development server: `python manage.py runserver`
7. Access the application in your browser at `http://localhost:8000`

## Usage

- Register a new account and log in to access personalized recommendations.
- Update your user profile with your favorite genre and artist preferences.
- Navigate to the recommendations page to view personalized music recommendations.
- Log out to exit your account.

## Contributing

Contributions are welcome! Feel free to open issues for any bugs or feature requests. Pull requests are also encouraged for adding new features or fixing existing issues.