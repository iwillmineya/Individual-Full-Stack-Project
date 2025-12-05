# GameYap Full Stack Capstone Project

## Project Overview
GameYap is a web application designed to provide a welcoming space for people to talk about games. Users can register, log in, add games, edit/delete their own entries, and interact with a responsive, user-friendly interface. The app is built with Django, Bootstrap, and custom CSS for a modern look and feel.

**Live Demo**: [https://gameyapp-82d05d711186.herokuapp.com/](https://gameyapp-82d05d711186.herokuapp.com/)

---

## Table of Contents
1. [UX Design Process](#ux-design-process)
2. [Agile Methodology](#agile-methodology)
3. [Database & Models](#database--models)
4. [Features & Functionality](#features--functionality)
5. [Technical Stack](#technical-stack)
6. [Installation & Setup](#installation--setup)
7. [Deployment](#deployment)
8. [Testing](#testing)
9. [Security](#security)
10. [AI Tool Reflection](#ai-tool-reflection)
11. [Challenges & Lessons Learned](#challenges--lessons-learned)
12. [Version Control](#version-control)

---

## UX Design Process
Wireframes for all major pages are included in [`wireframes.md`](wireframes.md):
- **Home Page**: Navigation bar, game cards, search/filter functionality, add/edit/delete buttons
- **Login/Register**: Centered forms with clear navigation and validation messages
- **Game Form**: User-friendly input fields with help text for date format
- **Profile Page**: User information, bio, avatar, and favorite games
- **Admin Page**: Standard Django admin interface for site management

I evolved my design based on user feedback and usability testing, making significant changes from my initial prototypes to better match user needs and expectations.

---

## Agile Methodology

### User Stories & Sprint Planning
Project tasks and user stories were tracked using GitHub Projects. Each user story follows the format:
- **As a** [user type]
- **I want** [specific action]
- **So that** [benefit/reason]

### Example User Stories:
1. **As a user**, I want to register and create an account, **so that** I can access the application and manage my games.
2. **As a game owner**, I want to edit my game entries, **so that** I can keep information current and accurate.
3. **As a user**, I want to search for games by title or genre, **so that** I can find games that interest me quickly.
4. **As a user**, I want to see other users' games but only edit my own, **so that** the platform maintains data integrity.

All major features were linked to project goals and updated as sprints progressed through each development milestone.

---

## Database & Models

### Entity Relationship Diagram
```
User (Django built-in)
├── Game (1:many relationship)
├── UserProfile (1:1 relationship)
│   └── favorite_games (many:many with Game)
└── Vote (1:many relationship)

Game
├── GameMedia (1:many relationship)
└── Vote (1:many relationship)
```

### Models Description

**Game Model**:
- `user` (ForeignKey) - Game owner for permission control
- `title` - Game title (max 100 chars)
- `genre` - Game genre (max 50 chars)
- `release_date` - Date format: YYYY-MM-DD
- `description` - Detailed game description
- `likes` - Like count (positive integer)
- `dislikes` - Dislike count (positive integer)
- `is_active` - Soft delete flag (boolean)

**UserProfile Model**:
- `user` (OneToOneField) - Link to Django User
- `bio` - User biography
- `avatar` - Profile picture
- `favorite_games` (ManyToManyField) - User's favorite games

**Vote Model**:
- `user` (ForeignKey) - Voting user
- `game` (ForeignKey) - Game being voted on
- `vote_type` - LIKE or DISLIKE choice
- Unique constraint on (user, game) to prevent duplicate votes

**GameMedia Model**:
- `game` (ForeignKey) - Associated game
- `media_type` - IMAGE or VIDEO
- `file` - Media file upload
- `uploaded_at` - Auto timestamp

---

## Features & Functionality

### Authentication & Authorization
- ✅ User registration with password validation
- ✅ Secure login/logout functionality
- ✅ Permission checks: Users can only edit/delete their own games
- ✅ Protected views: Restricted pages redirect to login
- ✅ Direct URL protection: Cannot bypass UI to access unauthorized pages

### Game Management (CRUD)
- ✅ **Create**: Users add new games with title, genre, release date, and description
- ✅ **Read**: Display all games with search and filter capabilities
- ✅ **Update**: Game owners can edit their entries (form pre-fills existing data)
- ✅ **Delete**: Soft delete - games marked inactive instead of removal
- ✅ **User Assignment**: Games automatically assigned to creator

### Search & Filtering
- ✅ Search by game title (case-insensitive contains)
- ✅ Filter by genre
- ✅ Filter by release date
- ✅ Combine multiple filters

### User Profile Management
- ✅ View user profile with bio and avatar
- ✅ Edit profile information
- ✅ Manage favorite games list
- ✅ Profile image upload

### Frontend & UX
- ✅ Responsive Bootstrap design (mobile, tablet, desktop)
- ✅ Navigation bar with conditional links based on auth status
- ✅ Game cards with owner information
- ✅ Form validation with clear error messages
- ✅ Date format help text on game forms
- ✅ Success/error feedback messages
- ✅ Leaderboard display for esports games

---

## Technical Stack

### Backend
- **Django 5.2.7** - Web framework
- **Python 3.10+** - Programming language
- **PostgreSQL** - Database (via Neon)
- **dj-database-url** - Database URL parsing
- **django-heroku** - Heroku deployment utilities

### Frontend
- **HTML5** - Markup
- **CSS3** - Custom styling
- **Bootstrap 5** - Responsive framework
- **JavaScript** - Client-side interactivity

### Deployment & DevOps
- **Heroku** - Cloud hosting platform
- **WhiteNoise** - Static file serving
- **Gunicorn** - WSGI application server

### Development Tools
- **Git & GitHub** - Version control
- **Visual Studio Code** - Code editor
- **Pylance** - Python language server

---

## Installation & Setup

### Prerequisites
- Python 3.10 or higher
- pip (Python package manager)
- Virtual environment (venv or conda)
- Git

### Local Development Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/iwillmineya/Individual-Full-Stack-Project.git
   cd Individual-Full-Stack-Project
   ```

2. **Create virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Create `.env` file** with environment variables:
   ```env
   DJANGO_SECRET_KEY=your-secret-key-here
   DJANGO_DEBUG=True
   DATABASE_URL=sqlite:///db.sqlite3  # For local development
   ```

5. **Run migrations**:
   ```bash
   python manage.py migrate
   ```

6. **Create superuser** (for admin access):
   ```bash
   python manage.py createsuperuser
   ```

7. **Run development server**:
   ```bash
   python manage.py runserver
   ```

8. **Access the application**:
   - Application: http://localhost:8000
   - Admin panel: http://localhost:8000/admin

---

## Deployment

### Deployment to Heroku

#### Prerequisites
- Heroku account (free or paid)
- Heroku CLI installed
- Git repository initialized

#### Step-by-Step Deployment Process

1. **Install Heroku CLI**:
   ```bash
   # Windows: Download from https://devcenter.heroku.com/articles/heroku-cli
   # macOS: brew install heroku/brew/heroku
   ```

2. **Login to Heroku**:
   ```bash
   heroku login
   ```

3. **Create Heroku application**:
   ```bash
   heroku create your-app-name
   ```

4. **Set environment variables** on Heroku:
   ```bash
   heroku config:set DJANGO_SECRET_KEY='your-secure-secret-key'
   heroku config:set DJANGO_DEBUG=False
   heroku config:set DATABASE_URL='your-postgres-database-url'
   ```

5. **Configure PostgreSQL database**:
   ```bash
   heroku addons:create heroku-postgresql:hobby-dev
   ```
   Or use external database like Neon PostgreSQL:
   ```bash
   heroku config:set DATABASE_URL='postgresql://user:password@host:port/database'
   ```

6. **Deploy application**:
   ```bash
   git push heroku main
   ```

7. **Run migrations on Heroku**:
   ```bash
   heroku run python manage.py migrate
   ```

8. **Create superuser on Heroku** (optional):
   ```bash
   heroku run python manage.py createsuperuser
   ```

9. **View logs**:
   ```bash
   heroku logs --tail
   ```

#### Environment Variables Required
- `DJANGO_SECRET_KEY` - Secret key for Django (generate using `django.core.management.utils.get_random_secret_key()`)
- `DJANGO_DEBUG` - Set to `False` in production
- `DATABASE_URL` - PostgreSQL connection string
- `ALLOWED_HOSTS` - Comma-separated list of allowed hostnames

#### Deployment Configuration Files
- **Procfile** - Defines Heroku process types (web dyno runs Gunicorn)
- **runtime.txt** - Specifies Python version
- **requirements.txt** - Lists all Python dependencies
- **.gitignore** - Prevents secrets from being committed

#### Troubleshooting Common Issues
- **Static files not loading**: Run `python manage.py collectstatic`
- **Database errors**: Check `heroku logs --tail` and verify `DATABASE_URL`
- **Build failures**: Ensure all dependencies are in `requirements.txt`
- **Secret key issues**: Verify environment variables are set correctly

---

## Testing

### Test Coverage
Comprehensive testing documentation is available in [`TESTING.md`](TESTING.md).

### Test Categories
1. **Authentication Testing** (4 tests)
   - User registration with validation
   - User login and logout
   - Unauthorized access prevention

2. **CRUD Operations** (5 tests)
   - Game creation with owner assignment
   - Edit own game
   - Permission check: Cannot edit other's games
   - Delete own game
   - Permission check: Cannot delete other's games

3. **Search & Filtering** (2 tests)
   - Search by title
   - Filter by genre

4. **User Profile** (2 tests)
   - View profile
   - Edit profile

5. **Security** (2 tests)
   - Direct URL access prevention
   - Secret key protection

### Test Results Summary
- **Total Tests**: 20
- **Passed**: 20 ✅
- **Failed**: 0 ✅
- **Pass Rate**: 100%

### Running Tests Locally
```bash
# Run all tests
python manage.py test

# Run tests for specific app
python manage.py test gameyap

# Run with verbosity
python manage.py test -v 2

# Run specific test class
python manage.py test gameyap.tests.TestGamePermissions
```

---

## Security

### Security Measures Implemented

1. **Secret Key Protection**
   - ✅ SECRET_KEY stored in environment variables
   - ✅ Never hardcoded or exposed in repository
   - ✅ Different keys for development and production

2. **Permission System**
   - ✅ User ownership tracking for games
   - ✅ Permission checks in views (game_update, game_delete)
   - ✅ Permission checks in templates (hide buttons for non-owners)
   - ✅ Protection against direct URL manipulation

3. **CSRF Protection**
   - ✅ Django CSRF middleware enabled
   - ✅ CSRF tokens in all forms

4. **Password Security**
   - ✅ Django built-in password validators
   - ✅ Minimum length enforcement
   - ✅ Common password prevention
   - ✅ Numeric password prevention

5. **Database Security**
   - ✅ Connection via secure protocols
   - ✅ User isolation (soft delete)
   - ✅ SQL injection prevention (ORM usage)

6. **Deployment Security**
   - ✅ DEBUG = False in production
   - ✅ ALLOWED_HOSTS restricted to domain
   - ✅ Environment variables for sensitive data
   - ✅ .gitignore prevents accidental commits

### Security Best Practices
- Regular security audits
- Dependency vulnerability scanning
- Input validation on all forms
- Output escaping in templates
- HTTP Security Headers configured

---

## AI Tool Reflection

### Key Decisions Using AI

#### 1. **Database Model Design**
**Decision**: Adding `user` field to Game model for ownership tracking
- **AI's Role**: Reviewed relationship patterns and suggested ForeignKey approach
- **Outcome**: Cleaner permission checks and better data integrity
- **Impact**: Enabled LO3 requirement for user-based permissions

#### 2. **Permission Implementation Strategy**
**Decision**: Implement permission checks at view level and UI level
- **AI's Role**: Explained defensive programming approach and why direct URL access needs protection
- **Outcome**: Added checks in both `game_update` and `game_delete` views plus template conditionals
- **Impact**: Prevented unauthorized access even through direct URL manipulation

#### 3. **Security: Environment Variables**
**Decision**: Move SECRET_KEY to environment variables
- **AI's Role**: Identified security vulnerability and suggested best practices
- **Outcome**: Implemented `os.environ.get()` pattern and created comprehensive .gitignore
- **Impact**: Resolved LO5 and LO6 security criteria

#### 4. **Form UX Improvement**
**Decision**: Add date format help text to GameForm
- **AI's Role**: Suggested using Django form widgets with help_text and date picker
- **Outcome**: Users see format requirements and have date picker widget
- **Impact**: Addressed assessment feedback about date format confusion

### AI's Role in Bug Resolution

#### 1. **Permission Check Bypass**
**Bug**: Non-owners could edit/delete games via direct URL
- **AI's Diagnosis**: Identified missing permission verification in views
- **Resolution**: Added `if game.user != request.user: return redirect("home")` checks
- **Result**: ✅ Fixed security vulnerability

#### 2. **Game Owner Assignment**
**Bug**: Games not tracking ownership
- **AI's Diagnosis**: Suggested adding user field to Game model
- **Resolution**: Created migration 0006_game_user.py and updated game_create view
- **Result**: ✅ Games now properly assigned to creators

#### 3. **Form Widget Enhancement**
**Bug**: Confusing date input format
- **AI's Suggestion**: Use HTML5 date input type and add help text
- **Resolution**: Updated GameForm with proper widgets and help_texts
- **Result**: ✅ Improved user experience with date picker and format guidance

### AI's Contribution to Performance & UX

#### 1. **Database Query Optimization**
- **Suggestion**: Use `select_related()` and `prefetch_related()` for queries
- **Status**: Evaluated for future optimization

#### 2. **Frontend Performance**
- **Suggestion**: Lazy loading for game images
- **Status**: Identified for future enhancement

#### 3. **UX Improvements**
- **Suggestion**: Add success messages after CRUD operations
- **Status**: Django messages framework implemented
- **Result**: Better user feedback on actions

### AI's Influence on Development Workflow

#### 1. **Code Review & Quality**
- AI helped identify code quality issues and suggested refactoring patterns
- Improved code readability and maintainability

#### 2. **Testing Strategy**
- AI suggested comprehensive testing approach with multiple test scenarios
- Guided creation of detailed testing documentation

#### 3. **Documentation**
- AI helped structure and format technical documentation
- Suggested best practices for README and TESTING files

#### 4. **Problem-Solving**
- AI provided quick answers to technical questions
- Helped debug issues through systematic troubleshooting
- Suggested alternative approaches when initial solutions weren't working

### Conclusion on AI Usage
AI was used strategically to:
- ✅ Identify security vulnerabilities
- ✅ Improve code quality and architecture
- ✅ Enhance user experience
- ✅ Provide technical guidance
- ✅ Structure documentation

Most core logic and design decisions remained developer-driven, with AI serving as a technical advisor and quality reviewer.

---

## Challenges & Lessons Learned

### Major Challenges

1. **GitHub Repository Mix-up** (Week 1-2)
   - **Issue**: Saved code to wrong repository for ~1.5 weeks
   - **Impact**: Had to restart development and re-organize work
   - **Lesson**: Always verify repository URL before starting work

2. **Heroku Deployment Issues** (Week 3-4)
   - **Issue**: Multiple build failures and database connection errors
   - **Causes**: Missing environment variables, incorrect Procfile, database URL issues
   - **Resolution**: Systematic debugging of logs and configuration files
   - **Lesson**: Read Heroku logs carefully; most issues show clear error messages

3. **Permission System Implementation** (Week 5)
   - **Issue**: Initial design didn't properly prevent unauthorized access
   - **Resolution**: Added defensive checks in views and templates
   - **Lesson**: Defensive programming is essential for security-critical features

4. **Date Format Confusion** (User Testing)
   - **Issue**: Users confused about required date format
   - **Resolution**: Added date picker widget and format help text
   - **Lesson**: Always provide clear user guidance for specific input formats

### Lessons Learned

1. **Start Simple, Scale Gradually**
   - Begin with basic CRUD, then add features like search/filter
   - Each feature should be tested before adding the next

2. **Security First**
   - Think about security implications from the start
   - Don't hardcode secrets; use environment variables
   - Implement permission checks at multiple levels

3. **User Experience Matters**
   - Small UX improvements (help text, date picker) have big impact
   - Test with actual users when possible
   - Provide clear feedback for all actions

4. **Documentation is Crucial**
   - Good documentation saves time for future maintenance
   - Detailed git commit messages help track changes
   - Testing documentation proves features work

5. **Version Control Discipline**
   - Always verify you're in the correct repository
   - Commit frequently with descriptive messages
   - Use `.gitignore` to prevent accidents

---

## Version Control

### Git Workflow
- **Branch Strategy**: Main branch for stable code
- **Commit Frequency**: Regular commits after feature completion
- **Commit Messages**: Descriptive, following conventional commits format

### Example Commits
```
- feat: Add user field to Game model for ownership tracking
- fix: Implement permission checks for game update/delete
- security: Move SECRET_KEY to environment variables
- docs: Add comprehensive testing documentation
- refactor: Improve GameForm with date picker widget
```

### Repository Structure
```
Individual-Full-Stack-Project/
├── config/                 # Django settings and URLs
├── mainproject/
│   ├── config/            # Project configuration
│   └── gameyap/           # Main application
│       ├── migrations/    # Database migrations
│       ├── static/        # CSS, JavaScript
│       ├── templates/     # HTML templates
│       ├── models.py      # Database models
│       ├── views.py       # View logic
│       ├── forms.py       # Form definitions
│       └── urls.py        # URL routing
├── staticfiles/           # Collected static files
├── manage.py              # Django management script
├── requirements.txt       # Python dependencies
├── Procfile              # Heroku deployment config
├── README.md             # This file
├── TESTING.md            # Testing documentation
└── wireframes.md         # UI/UX design documentation
```

---

## Future Enhancements

- [ ] Automated testing with pytest
- [ ] API endpoints (Django REST Framework)
- [ ] Real-time notifications
- [ ] Advanced recommendation system
- [ ] Social features (comments, reviews)
- [ ] Image optimization and CDN integration
- [ ] Performance monitoring and analytics

---

## Support & Contact

For questions or issues, please open an issue in the GitHub repository:
[https://github.com/iwillmineya/Individual-Full-Stack-Project/issues](https://github.com/iwillmineya/Individual-Full-Stack-Project/issues)

---

**Last Updated**: December 2024
**Status**: Active Development
**License**: MIT