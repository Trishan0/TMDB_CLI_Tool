# TMDB CLI Tool
<div align="center">
    <img src="https://socialify.git.ci/Trishan0/TMDB_CLI_Tool/image?forks=1&issues=1&language=1&name=1&pulls=1&stargazers=1&theme=Auto" alt="TMDB CLI Tool" width="640" height="320" />
</div>
<br><br>
<br>

<div align='center' style=" display: grid;">

  [![Gmail](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:sanjanatrishan@gmail.com)
  [![Github](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Trishan0)
  [![Medium](https://img.shields.io/badge/Medium-12100E?style=for-the-badge&logo=medium&logoColor=white)](https://medium.com/@trishan-fernando)
  [![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/trishan-fernando/)
</div>

---

# TMDB CLI Tool Project

A command-line interface tool that fetches and displays movie information from The Movie Database (TMDB) API. This tool allows users to view now playing, popular, top-rated, and upcoming movies with detailed information including titles, release dates, ratings, and brief overviews.

## Features

- View now playing movies in theaters
- Browse popular movies
- Check top-rated movies of all time
- See upcoming movie releases
- Colorized output for better readability
- Detailed movie information including release dates and ratings

## Example Commands

Here are some example commands and their usage:

```bash
tmdb-app type now-playing
# Now Playing Movies:
# --------------------------------------------------
# Title: Dune: Part Two
# Release Date: 2024-02-28
# Rating: 8.5/10
# Overview: Follow the mythic journey of Paul Atreides as he unites with Chani and the Fremen...
#
# Title: Madame Web
# Release Date: 2024-02-14
# Rating: 5.6/10
# Overview: Cassandra Webb is a New York City paramedic who starts to show signs of clairvoyance...

tmdb-app type popular
# Popular Movies:
# --------------------------------------------------
# Title: Anyone But You
# Release Date: 2023-12-21
# Rating: 7.1/10
# Overview: After an amazing first date, Bea and Ben's fiery attraction turns ice cold...

tmdb-app type top-rated
# Top Rated Movies:
# --------------------------------------------------
# Title: The Godfather
# Release Date: 1972-03-14
# Rating: 8.7/10
# Overview: Spanning the years 1945 to 1955, a chronicle of the fictional Italian-American Corleone...

tmdb-app type upcoming
# Upcoming Movies:
# --------------------------------------------------
# Title: Godzilla x Kong: The New Empire
# Release Date: 2024-03-27
# Rating: 0/10
# Overview: Two ancient titans, Godzilla and Kong, clash in an epic battle as humans unravel...
```

## Getting Started

### Prerequisites

- Python 3.7 or higher
- TMDB API Key (Get it from [TMDB website](https://www.themoviedb.org/settings/api))

### Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/Trishan0/TMDB_CLI_Tool.git
    cd TMDB_CLI_Tool
    ```

2. Create a virtual environment:
    ```sh
    python -m venv venv
    ```

3. Activate the virtual environment:
    - On Windows:
        ```sh
        venv\Scripts\activate
        ```
    - On macOS/Linux:
        ```sh
        source venv/bin/activate
        ```

4. Install dependencies:
    ```sh
    pip install -r requirements.txt
    ```

5. Create a `.env` file in the root directory and add your TMDB API key:
    ```sh
    TMDB_API_KEY=your_api_key_here
    ```

6. Install the package in development mode:
    ```sh
    pip install -e .
    ```

## Usage

The TMDB CLI Tool supports the following commands:

- **View Now Playing Movies**: 
    ```sh
    tmdb-app type now-playing
    ```

- **View Popular Movies**: 
    ```sh
    tmdb-app type popular
    ```

- **View Top Rated Movies**: 
    ```sh
    tmdb-app type top-rated
    ```

- **View Upcoming Movies**: 
    ```sh
    tmdb-app type upcoming
    ```

Original Project Link: [TMDB CLI Tool](https://roadmap.sh/projects/tmdb-cli-tool)

## API Response Format

The tool processes JSON responses from the TMDB API in the following format:

```json
{
  "results": [
    {
      "title": "Movie Title",
      "release_date": "2024-02-23",
      "vote_average": 7.5,
      "overview": "Movie description..."
    }
  ]
}
```

### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---