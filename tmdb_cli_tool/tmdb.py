import argparse
from tmdb_cli_tool.model import get_now_playing, get_popular, get_top_rated, get_upcoming

def main():
    parser = argparse.ArgumentParser(
        description="Simple CLI Tool to show the movies from The Movie Database"
    )
    
    subparsers = parser.add_subparsers(dest="command", help="Available Commands")
        
    # Create the general "type" command that can be used for different categories
    type_parser = subparsers.add_parser('type', help="Show movies by category")
    type_parser.add_argument('category', type=str, help="Category", choices=["now-playing", "popular", "top-rated", "upcoming"])
    
    args = parser.parse_args()
    
    if args.command == 'type':
        if args.category == 'now-playing':
            get_now_playing()
        elif args.category == 'popular':
            get_popular()
        elif args.category == 'top-rated':
            get_top_rated()
        elif args.category == 'upcoming':
            get_upcoming()
        else:
            print(f"Unknown category: {args.category}")
    
    else:
        parser.print_help()
