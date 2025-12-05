# GameYap - Testing Documentation

## Overview
This document provides comprehensive testing procedures for the GameYap application, including manual test cases, step-by-step procedures, and test results.

## Test Scenarios

### 1. User Authentication & Authorization

#### 1.1 User Registration
**User Story**: As a new user, I want to register an account so that I can access the application.

**Test Steps**:
1. Navigate to the Register page from the navigation bar
2. Enter a valid username (minimum 3 characters)
3. Enter a valid password (minimum 8 characters, not all numeric)
4. Confirm the password
5. Click "Register" button

**Expected Result**: User is created and redirected to home page as logged-in user

**Test Result**: ✓ PASS

---

#### 1.2 User Login
**User Story**: As a registered user, I want to log in so that I can access my account and manage my games.

**Test Steps**:
1. Navigate to the Login page
2. Enter valid username
3. Enter valid password
4. Click "Login" button

**Expected Result**: User is authenticated and redirected to home page

**Test Result**: ✓ PASS

---

#### 1.3 User Logout
**User Story**: As a logged-in user, I want to log out so that I can end my session securely.

**Test Steps**:
1. Log in as an existing user
2. Click the "Logout" link in the navigation bar
3. Verify redirect to home page

**Expected Result**: User is logged out and session ends

**Test Result**: ✓ PASS

---

#### 1.4 Unauthorized Access Prevention
**User Story**: As a security measure, I want non-logged-in users to be restricted from accessing protected pages.

**Test Steps**:
1. Do not log in
2. Try to access `/game/create/` directly
3. Try to access `/profile/` directly

**Expected Result**: User is redirected to login page

**Test Result**: ✓ PASS

---

### 2. Game CRUD Operations

#### 2.1 Create Game - Owner Assignment
**User Story**: As a user, I want to create a game entry so that I can share games with the community.

**Test Steps**:
1. Log in as User A
2. Navigate to "Add Game"
3. Fill in game details:
   - Title: "Test Game"
   - Genre: "Action"
   - Release Date: 2024-01-15 (using date picker)
   - Description: "Test description"
4. Click "Save"

**Expected Result**: Game is created and assigned to User A, redirected to home page

**Test Result**: ✓ PASS

---

#### 2.2 Edit Own Game
**User Story**: As a game owner, I want to edit my game entry so that I can update information.

**Test Steps**:
1. Log in as User A (owner of a game)
2. Find the game in the list
3. Click "Edit" button
4. Modify the description
5. Click "Save"

**Expected Result**: Game is updated, form shows pre-filled data

**Test Result**: ✓ PASS

---

#### 2.3 Cannot Edit Other User's Game (Permission Check)
**User Story**: As a user, I should not be able to edit another user's game to maintain data integrity.

**Test Steps**:
1. Log in as User B (non-owner)
2. Navigate directly to edit URL of User A's game: `/game/<game_id>/edit/`
3. Verify no edit button is visible for User A's game

**Expected Result**: User is redirected to home page, cannot access edit form

**Test Result**: ✓ PASS

---

#### 2.4 Delete Own Game
**User Story**: As a game owner, I want to delete my game entry so that I can remove outdated information.

**Test Steps**:
1. Log in as User A (owner of a game)
2. Find the game in the list
3. Click "Delete" button
4. Click confirmation button

**Expected Result**: Game is marked as inactive and no longer appears in the list

**Test Result**: ✓ PASS

---

#### 2.5 Cannot Delete Other User's Game (Permission Check)
**User Story**: As a user, I should not be able to delete another user's game.

**Test Steps**:
1. Log in as User B (non-owner)
2. Navigate directly to delete URL of User A's game: `/game/<game_id>/delete/`
3. Verify no delete button is visible

**Expected Result**: User is redirected to home page

**Test Result**: ✓ PASS

---

### 3. Game Search & Filtering

#### 3.1 Search by Title
**User Story**: As a user, I want to search games by title so that I can find specific games quickly.

**Test Steps**:
1. Navigate to home page
2. Enter "Test" in the search box
3. Click "Search" or press Enter

**Expected Result**: Only games with "Test" in the title are displayed

**Test Result**: ✓ PASS

---

#### 3.2 Filter by Genre
**User Story**: As a user, I want to filter games by genre so that I can find games in my preferred category.

**Test Steps**:
1. Navigate to home page
2. Select a genre from the dropdown
3. Click "Filter"

**Expected Result**: Only games with the selected genre are displayed

**Test Result**: ✓ PASS

---

### 4. User Profile Management

#### 4.1 View Profile
**User Story**: As a logged-in user, I want to view my profile so that I can see my information and games.

**Test Steps**:
1. Log in
2. Click "Profile" in the navigation bar
3. Verify profile information displays

**Expected Result**: User profile page loads with correct information

**Test Result**: ✓ PASS

---

#### 4.2 Edit Profile
**User Story**: As a user, I want to edit my profile so that I can update my bio and avatar.

**Test Steps**:
1. Log in
2. Navigate to Profile
3. Click "Edit Profile"
4. Update bio and/or avatar
5. Click "Save"

**Expected Result**: Profile is updated, redirected to profile view

**Test Result**: ✓ PASS

---

### 5. Navigation & UI

#### 5.1 Navigation Bar Visibility
**User Story**: As a user, I want the navigation bar to show appropriate links based on my login status.

**Test Steps**:
1. Visit home page without logging in
   - Verify: Home, Login, Register visible
2. Log in
   - Verify: Home, Add Game, Profile, Logout visible

**Expected Result**: Navigation changes based on authentication status

**Test Result**: ✓ PASS

---

#### 5.2 Responsive Design
**User Story**: As a user, I want the application to work on mobile and desktop devices.

**Test Steps**:
1. Test on desktop (1920x1080)
2. Test on tablet (768x1024)
3. Test on mobile (375x812)
4. Verify layouts are responsive

**Expected Result**: Content is readable and accessible on all device sizes

**Test Result**: ✓ PASS

---

### 6. Form Validation

#### 6.1 Date Format Help Text
**User Story**: As a user, I want clear indication of the expected date format so that I can enter dates correctly.

**Test Steps**:
1. Navigate to Add Game form
2. Look for date input field
3. Verify help text shows date format

**Expected Result**: Help text displays "Use date format: YYYY-MM-DD (e.g., 2024-12-05)"

**Test Result**: ✓ PASS

---

#### 6.2 Invalid Date Entry
**User Story**: As a user, I want the system to reject invalid date formats to prevent errors.

**Test Steps**:
1. Navigate to Add Game form
2. Try entering an invalid date format (e.g., "12/25/2024")
3. Try to submit

**Expected Result**: Form shows error, does not submit

**Test Result**: ✓ PASS

---

#### 6.3 Required Fields Validation
**User Story**: As a user, I want the system to require essential fields to maintain data quality.

**Test Steps**:
1. Navigate to Add Game form
2. Leave title field empty
3. Try to submit

**Expected Result**: Form shows validation error, does not submit

**Test Result**: ✓ PASS

---

## Security Testing

### 7.1 Direct URL Access Prevention
**Test Steps**:
1. Log in as User B
2. Try to access another user's game edit page directly: `/game/<user_a_game_id>/edit/`
3. Try to access game delete page directly: `/game/<user_a_game_id>/delete/`

**Expected Result**: User is redirected to home page (403 Forbidden equivalent)

**Test Result**: ✓ PASS

---

### 7.2 Secret Key Protection
**Test Steps**:
1. Verify SECRET_KEY is not visible in settings.py (should use environment variable)
2. Verify .gitignore includes .env files
3. Verify DEBUG is set to False in production

**Expected Result**: No sensitive data is hardcoded or exposed

**Test Result**: ✓ PASS

---

## Test Coverage Summary

| Category | Tests | Passed | Failed |
|----------|-------|--------|--------|
| Authentication | 4 | 4 | 0 |
| CRUD Operations | 5 | 5 | 0 |
| Search & Filter | 2 | 2 | 0 |
| User Profile | 2 | 2 | 0 |
| Navigation & UI | 2 | 2 | 0 |
| Form Validation | 3 | 3 | 0 |
| Security | 2 | 2 | 0 |
| **TOTAL** | **20** | **20** | **0** |

---

## Known Issues & Resolutions

None at this time. All test cases pass successfully.

---

## Browser Compatibility

- ✓ Chrome 120+
- ✓ Firefox 121+
- ✓ Safari 17+
- ✓ Edge 121+

---

## Regression Testing

After each deployment, the following critical test cases should be re-run:
1. User authentication (registration, login, logout)
2. Game creation with correct user assignment
3. Permission checks (cannot edit/delete other users' games)
4. Date format validation on forms
5. Direct URL access security checks

---

## Conclusion

All test cases have passed successfully. The application meets the requirements for user authentication, game management with proper permission controls, and security standards.
