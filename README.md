#  TravEasy: SQL / Flask / Appsmith Boilerplate Project
### Team Member(s): Vincent Demaisip, Wei Ding, Miguel Gonzales, Eric Wu, and Gregory Zeng

This repo contains a boilerplate setup for spinning up 3 Docker containers: 
1. A MySQL 8 container for obvious reasons
1. A Python Flask container to implement a REST API
1. A Local AppSmith Server

## How to setup and start the containers
**Important** - you need Docker Desktop installed

1. Clone this repository.  
1. Create a file named `db_root_password.txt` in the `secrets/` folder and put inside of it the root password for MySQL. 
1. Create a file named `db_password.txt` in the `secrets/` folder and put inside of it the password you want to use for the a non-root user named webapp. 
1. In a terminal or command prompt, navigate to the folder with the `docker-compose.yml` file.  
1. Build the images with `docker compose build`
1. Start the containers with `docker compose up`.  To run in detached mode, run `docker compose up -d`. 

## TravEasy - Traveling Guide Application
Welcome to our Traveling Guide Application repository!

## Project Overview
TravEasy is a comprehensive application designed to streamline and simplify the entire trip planning process. Our application aims to provide travelers with comprehensive guidance on transportation, activities, and payment fees, ensuring they have the best experience possible. Whether you're embarking on a solo adventure, organizing a family vacation, or planning a business trip, TravEasy has you covered. 

## Features
Transportation Guidance: Find the best routes and modes of transportation for your journey.

Activity Recommendations: Discover exciting activities and attractions at your destination.

Payment Fee Information: Get insights into payment fees and currency exchange rates.

User-friendly Interface: Our app is designed to be easy to use, making travel planning hassle-free.

Real-time Updates: Stay informed with real-time updates on transportation schedules and availability.
