# GameYap Wireframes & Design Documentation

## Design Overview
This document provides wireframe specifications for the GameYap application. The design follows modern UX principles with a focus on simplicity, clarity, and user engagement.

---

## Wireframe: Home Page

### Layout Components
```
┌─────────────────────────────────────────────────────────┐
│  NAVBAR: Home | Add Game | Profile | Logout            │
├─────────────────────────────────────────────────────────┤
│                                                           │
│  SEARCH & FILTER SECTION                                 │
│  [Search by Title]  [Genre Dropdown]  [Filter Button]   │
│                                                           │
├─────────────────────────────────────────────────────────┤
│                     GAME CARDS GRID                       │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐   │
│  │  Game Title  │  │  Game Title  │  │  Game Title  │   │
│  │  Genre       │  │  Genre       │  │  Genre       │   │
│  │  Release: XX │  │  Release: XX │  │  Release: XX │   │
│  │  Owner: Name │  │  Owner: Name │  │  Owner: Name │   │
│  │              │  │              │  │              │   │
│  │ [Edit][Del]  │  │ [Edit][Del]  │  │ [Edit][Del]  │   │
│  └──────────────┘  └──────────────┘  └──────────────┘   │
│                                                           │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐   │
│  │  Game Title  │  │  Game Title  │  │  Game Title  │   │
│  └──────────────┘  └──────────────┘  └──────────────┘   │
│                                                           │
├─────────────────────────────────────────────────────────┤
│  LEADERBOARDS (Optional sections)                        │
│  Top Overwatch Players | Top Valorant Players           │
└─────────────────────────────────────────────────────────┘
```

### Key Features
- **Navigation Bar**: Displays Home, Add Game, Profile, Logout (logged-in) or Login/Register (not logged-in)
- **Search/Filter Section**: 
  - Text search for game titles (case-insensitive)
  - Genre filter dropdown
  - Release date filter
- **Game Cards**: Display grid layout with:
  - Game title and genre
  - Release date
  - Game owner name
  - Edit/Delete buttons (only visible to game owner)
- **Leaderboards**: Display top players for featured games

### Responsive Behavior
- **Desktop (1920px+)**: 3 columns of game cards
- **Tablet (768px)**: 2 columns of game cards
- **Mobile (375px)**: 1 column of game cards

---

## Wireframe: Login Page

### Layout Components
```
┌─────────────────────────────────────────────────────────┐
│  NAVBAR: Home | Login | Register                        │
├─────────────────────────────────────────────────────────┤
│                                                           │
│                   LOGIN FORM                             │
│                                                           │
│            ┌──────────────────────────┐                  │
│            │   GameYap               │                  │
│            │   Login to Your Account │                  │
│            ├──────────────────────────┤                  │
│            │                          │                  │
│            │ Username:                │                  │
│            │ [____________________]   │                  │
│            │                          │                  │
│            │ Password:                │                  │
│            │ [____________________]   │                  │
│            │                          │                  │
│            │   [Login Button]         │                  │
│            │                          │                  │
│            │  Don't have account?     │                  │
│            │  [Register Here]         │                  │
│            └──────────────────────────┘                  │
│                                                           │
└─────────────────────────────────────────────────────────┘
```

### Key Features
- **Centered Form**: Clean, minimal design
- **Username Field**: Text input for login
- **Password Field**: Secure password input
- **Login Button**: Large, clickable button
- **Registration Link**: Clear call-to-action for new users
- **Error Messages**: Display invalid credentials feedback

### UX Principles
- Single column layout for clarity
- Large form with high contrast
- Clear visual hierarchy

---

## Wireframe: Register Page

### Layout Components
```
┌─────────────────────────────────────────────────────────┐
│  NAVBAR: Home | Login | Register                        │
├─────────────────────────────────────────────────────────┤
│                                                           │
│                REGISTRATION FORM                         │
│                                                           │
│            ┌──────────────────────────┐                  │
│            │   Create New Account    │                  │
│            ├──────────────────────────┤                  │
│            │                          │                  │
│            │ Username:                │                  │
│            │ [____________________]   │                  │
│            │  ℹ 3+ characters         │                  │
│            │                          │                  │
│            │ Password:                │                  │
│            │ [____________________]   │                  │
│            │  ℹ Min 8 characters      │                  │
│            │                          │                  │
│            │ Confirm Password:        │                  │
│            │ [____________________]   │                  │
│            │                          │                  │
│            │ [Register Button]        │                  │
│            │                          │                  │
│            │ Already have account?    │                  │
│            │ [Login Here]             │                  │
│            └──────────────────────────┘                  │
│                                                           │
└─────────────────────────────────────────────────────────┘
```

### Key Features
- **Username Field**: Minimum length validation
- **Password Field**: Security requirements display
- **Confirm Password**: Verification field
- **Help Text**: Display password requirements
- **Validation Feedback**: Real-time error messages
- **Login Link**: Easy navigation for existing users

### Validation Rules
- Username: Minimum 3 characters
- Password: Minimum 8 characters, not all numeric
- Password confirmation must match

---

## Wireframe: Game Form (Add/Edit)

### Layout Components
```
┌─────────────────────────────────────────────────────────┐
│  NAVBAR: Home | Add Game | Profile | Logout            │
├─────────────────────────────────────────────────────────┤
│                                                           │
│              ADD/EDIT GAME FORM                          │
│                                                           │
│    ┌────────────────────────────────────┐               │
│    │  Game Title                        │               │
│    │  [________________________]          │               │
│    │                                     │               │
│    │  Genre                              │               │
│    │  [Action | RPG | Strategy | ...]   │               │
│    │                                     │               │
│    │  Release Date                       │               │
│    │  [Date Picker: YYYY-MM-DD]          │               │
│    │  ℹ Format: YYYY-MM-DD               │               │
│    │                                     │               │
│    │  Description                        │               │
│    │  [________________________]          │               │
│    │  [________________________]          │               │
│    │  [________________________]          │               │
│    │                                     │               │
│    │   [Save]  [Cancel]                  │               │
│    └────────────────────────────────────┘               │
│                                                           │
└─────────────────────────────────────────────────────────┘
```

### Key Features
- **Title Field**: Text input (max 100 chars)
- **Genre Field**: Text input or dropdown (max 50 chars)
- **Release Date Field**: 
  - Date picker widget for easy selection
  - Help text showing format: "Use date format: YYYY-MM-DD (e.g., 2024-12-05)"
  - Format validation
- **Description Field**: Textarea (multiple rows)
- **Form Buttons**:
  - Save: Submit form
  - Cancel: Return to home page
- **Pre-filled Data**: Edit forms show existing values
- **Validation Messages**: Clear error display for invalid inputs

### UX Improvements
- Date picker widget to reduce typing errors
- Help text for date format requirements
- Pre-filled form on edit with current data
- Submit feedback (success/error messages)

---

## Wireframe: Profile Page

### Layout Components
```
┌─────────────────────────────────────────────────────────┐
│  NAVBAR: Home | Add Game | Profile | Logout            │
├─────────────────────────────────────────────────────────┤
│                                                           │
│              USER PROFILE                                │
│                                                           │
│    ┌────────────────────────────────────┐               │
│    │  [Avatar]    Username              │               │
│    │              Member since: YYYY     │               │
│    │                                     │               │
│    │  Bio                                │               │
│    │  "Game enthusiast and collector..."│               │
│    │                                     │               │
│    │  [Edit Profile Button]              │               │
│    └────────────────────────────────────┘               │
│                                                           │
│    ┌────────────────────────────────────┐               │
│    │  MY GAMES (X games)                │               │
│    │  ┌──────────┐  ┌──────────┐        │               │
│    │  │Game 1    │  │Game 2    │        │               │
│    │  │[Edit]    │  │[Edit]    │        │               │
│    │  └──────────┘  └──────────┘        │               │
│    │                                     │               │
│    │  ┌──────────┐  ┌──────────┐        │               │
│    │  │Game 3    │  │Game 4    │        │               │
│    │  │[Edit]    │  │[Edit]    │        │               │
│    │  └──────────┘  └──────────┘        │               │
│    └────────────────────────────────────┘               │
│                                                           │
│    ┌────────────────────────────────────┐               │
│    │  FAVORITE GAMES (X games)          │               │
│    │  ┌──────────┐  ┌──────────┐        │               │
│    │  │Fav Game 1│  │Fav Game 2│        │               │
│    │  └──────────┘  └──────────┘        │               │
│    └────────────────────────────────────┘               │
│                                                           │
└─────────────────────────────────────────────────────────┘
```

### Key Features
- **Profile Section**:
  - User avatar (image)
  - Username
  - Member since date
  - Bio text
  - Edit Profile button
- **My Games Section**:
  - Display all games created by user
  - Edit button for each game
  - Delete button for each game
  - Game count display
- **Favorite Games Section**:
  - Display games marked as favorites
  - User can manage favorites

---

## Wireframe: Delete Confirmation Page

### Layout Components
```
┌─────────────────────────────────────────────────────────┐
│  NAVBAR: Home | Add Game | Profile | Logout            │
├─────────────────────────────────────────────────────────┤
│                                                           │
│         DELETE GAME CONFIRMATION                         │
│                                                           │
│    ┌────────────────────────────────────┐               │
│    │  ⚠️  Delete Game?                  │               │
│    │                                     │               │
│    │  Are you sure you want to delete   │               │
│    │  "Game Title" by [Your Name]?      │               │
│    │                                     │               │
│    │  This action cannot be undone.    │               │
│    │                                     │               │
│    │  [Cancel]  [Delete]                │               │
│    └────────────────────────────────────┘               │
│                                                           │
└─────────────────────────────────────────────────────────┘
```

### Key Features
- **Warning Message**: Clear indication of action
- **Game Information**: Show which game will be deleted
- **Confirmation Buttons**:
  - Cancel: Return without deleting
  - Delete: Confirm deletion (marked as dangerous action)

### UX Safety Features
- Red/warning color for delete button
- Clear confirmation message
- Ability to cancel action

---

## Color Scheme & Typography

### Colors
- **Primary**: #007BFF (Blue) - Actions, links
- **Secondary**: #6C757D (Gray) - Secondary elements
- **Success**: #28A745 (Green) - Success messages
- **Danger**: #DC3545 (Red) - Delete, danger actions
- **Background**: #FFFFFF (White)
- **Text**: #212529 (Dark Gray)

### Typography
- **Headers**: Bootstrap default (larger, bold)
- **Body**: 14-16px sans-serif
- **Forms**: Clear labels, placeholders
- **Help Text**: Smaller, lighter gray text

---

## Responsive Design Breakpoints

### Desktop (1920px and above)
- 3-column game card grid
- Full navigation bar
- Side leaderboards

### Tablet (768px - 1024px)
- 2-column game card grid
- Responsive navigation
- Stacked leaderboards

### Mobile (375px - 767px)
- 1-column game card grid
- Hamburger menu for navigation
- Full-width forms
- Optimized touch targets (44px minimum)

---

## Accessibility Features

- **ARIA Labels**: Form inputs have proper labels
- **Color Contrast**: Text meets WCAG AA standards
- **Keyboard Navigation**: All interactive elements accessible via keyboard
- **Focus Indicators**: Clear focus states for interactive elements
- **Alt Text**: Placeholder for future image uploads
- **Form Validation**: Clear error messages

---

## Visual Design Notes

1. **Consistency**: Uniform spacing, typography, and colors across pages
2. **Hierarchy**: Clear visual distinction between primary and secondary actions
3. **Whitespace**: Adequate spacing for readability
4. **Feedback**: Visual/text feedback for all user actions
5. **Simplicity**: Minimal distractions, focus on core functionality

---

## Future Design Enhancements

- [ ] Dark mode support
- [ ] Image upload and display for game artwork
- [ ] Rating system with star display
- [ ] Comment/review section on games
- [ ] User badges and achievements
- [ ] Advanced filtering with date range picker
- [ ] Game comparison view

---

**Last Updated**: December 2024- Standard Django admin interface

---

These wireframes describe the layout and navigation for each major page. You can include this in your README as part of your UX documentation.
