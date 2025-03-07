import requests
import json
from dotenv import load_dotenv
from colorama import init, Fore, Style
import os

load_dotenv()

# Store API key and base URL as constants
API_KEY = os.getenv('TMDB_API_KEY')  # Move API key to .env file
BASE_URL = "https://api.themoviedb.org/3/movie"

# Common headers used across all requests
HEADERS = {
    "accept": "application/json",
    "Authorization": f"Bearer {API_KEY}"
}

def fetch_movies(endpoint, category_name):
    """
    Generic function to fetch movies from TMDB API
    
    Args:
        endpoint (str): API endpoint for specific movie category
        category_name (str): Display name for the movie category
    """

    url = f"{BASE_URL}/{endpoint}?language=en-US&page=1"
    
    try:
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()
        data = response.json()
        
        if not data.get('results'):
            print(f"{Fore.YELLOW}No movies found.{Style.RESET_ALL}")
            return
            
        print(f"\n{Fore.CYAN}{category_name}:{Style.RESET_ALL}")
        print(Fore.GREEN + "-" * 50 + Style.RESET_ALL)
        
        for movie in data['results']:
            title = movie['title']
            release_date = movie.get('release_date', 'N/A')
            rating = movie.get('vote_average', 'N/A')
            overview = movie.get('overview', 'No overview available')
            
            print(f"{Fore.WHITE}Title: {Fore.YELLOW}{title}{Style.RESET_ALL}")
            print(f"{Fore.WHITE}Release Date: {Fore.BLUE}{release_date}{Style.RESET_ALL}")
            print(f"{Fore.WHITE}Rating: {Fore.MAGENTA}{rating}/10{Style.RESET_ALL}")
            print(f"{Fore.WHITE}Overview: {Fore.CYAN}{overview[:100]}...{Style.RESET_ALL}\n")
            
        print(Fore.GREEN + "-" * 50 + Style.RESET_ALL)
        
        
    except requests.exceptions.RequestException as e:
        print(f"{Fore.RED}Error fetching data: {e}{Style.RESET_ALL}")
    except json.JSONDecodeError:
        print(f"{Fore.RED}Error decoding API response{Style.RESET_ALL}")

def get_now_playing():
    """Get the now playing movies from the TMDB API"""
    fetch_movies("now_playing", "Now Playing Movies")

def get_popular():
    """Get the popular movies from the TMDB API"""
    fetch_movies("popular", "Popular Movies")

def get_top_rated():
    """Get the top rated movies from the TMDB API"""
    fetch_movies("top_rated", "Top Rated Movies")

def get_upcoming():
    """Get the upcoming movies from the TMDB API"""
    fetch_movies("upcoming", "Upcoming Movies")