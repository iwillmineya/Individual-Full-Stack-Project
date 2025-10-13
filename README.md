# GameYap Full Stack Capstone Project

## Project Overview
GameYap is a web application designed to provide a welcoming space for people to talk about games. Users can register, log in, add games, edit/delete their entries, and interact with a responsive, user-friendly interface. The app is built with Django, Bootstrap, and custom CSS for a modern look and feel.

## UX Design Process
Wireframes for all major pages are included in [`wireframes.md`](wireframes.md):
- Home Page: Navigation bar, game cards, add/edit/delete buttons
- Login/Register: Centered forms, clear navigation
- Game Form: Simple, accessible input fields
- Admin Page: Standard Django admin

I changed my design completely from my initial expectations to better fit user needs and feedback.

## Agile Methodology
Project tasks and user stories were tracked using GitHub Projects. I documented all major features and linked them to project goals, updating progress as I worked through each milestone.

## Database & Models
The app uses Django ORM with a custom `Game` model and user profile model. Relationships and fields were chosen to support the core features and ensure data integrity.

## Features & Functionality
- User registration, login, and logout
- Add, edit, and delete games
- Advanced search and filter for games (by title, genre, release date)
- Leaderboards for top games/players
- Responsive design with Bootstrap
- Secure access controls for CRUD operations

## Testing
Manual testing was performed for all features. I used AI tools to scan my code and check for errors. All major functionality was verified to work as expected.

## Deployment
The app is deployed to Heroku. Deployment steps included:
- Setting up environment variables for secrets
- Using `.gitignore` to keep sensitive info out of the repo
- Ensuring `DEBUG` is off in production
- Resolving Heroku build and runtime issues

## Security
Managing secrets and security was challenging, as it was new to me. I used environment variables and `.gitignore` to protect sensitive data. No passwords or secrets are committed to the repository.

## AI Tool Reflection
I used minimal AI, mainly for code generation when I was stuck or troubleshooting. AI helped scan my code for errors and suggest fixes, but most logic and design decisions were my own.

## Challenges & Highlights
I faced many issues with Heroku and GitHub. For about a week and a half, I was saving my code to the wrong GitHub repo and had to start over. This was very stressful and almost made me lose motivation, but I pushed through. Heroku also gave me trouble at the start, but I resolved the issues and got the app deployed.

## Version Control
I used Git and GitHub for version control, with regular commits and descriptive messages documenting my progress.

---

For wireframes and design documentation, see [`wireframes.md`](wireframes.md).