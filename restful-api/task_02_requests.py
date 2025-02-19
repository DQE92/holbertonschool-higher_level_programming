#!/usr/bin/python3
import requests
import csv

def fetch_and_print_posts():
    """
    Fetches posts from the JSONPlaceholder API and prints their titles.
    
    This function performs a GET request to the JSONPlaceholder API to retrieve
    a list of posts. If the request is successful (status code 200), it prints
    the title of each post.
    
    Returns:
        None
    
    Raises:
        requests.RequestException: If an error occurs during the HTTP request
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    print(f"Status Code: {response.status_code}")
    
    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post['title'])

def fetch_and_save_posts():
    """
    Fetches posts from the JSONPlaceholder API and saves them to a CSV file.
    
    This function performs a GET request to the JSONPlaceholder API to retrieve
    a list of posts. If the request is successful (status code 200), it extracts
    the id, title, and body of each post and saves them to a 'posts.csv' file.
    
    Returns:
        None
        
    Raises:
        requests.RequestException: If an error occurs during the HTTP request
        IOError: If an error occurs while writing to the CSV file
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    print(f"Status code: {response.status_code}")
    
    if response.status_code == 200:
        posts = response.json()
        
        structured_posts = [
            {
                'id': post['id'],
                'title': post['title'],
                'body': post['body']
            }
            for post in posts
        ]
        
        with open('posts.csv', 'w', newline='', encoding='utf-8') as file:
            fieldnames = ['id', 'title', 'body']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(structured_posts)
