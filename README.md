#GoodViews Website

GoodViews is an engaging online destination for movie enthusiasts to explore, critique, and discuss a wide array of films. Mirroring the concept of Goodreads for book lovers, GoodViews serves as a haven for film buffs and casual viewers alike. The platform encourages users to rate and review movies, exchange recommendations, and curate personal lists of their film favorites. GoodViews offers an extensive catalog of cinematic experiences, encompassing new releases, timeless classics, and undiscovered treasures. Whether your interest lies in mainstream hits, indie productions, or global cinema, GoodViews is the ideal place for all your movie-related pursuits. Immerse yourself in the diverse world of movies and connect with a community of like-minded cinephiles. Discover your next favorite film and share your cinematic journey with others. Visit the live website [here](insert link) and dive into the captivating universe of GoodViews.

![Mockup](insert filepath)

---

## Table of Contents

---
## User Experience Design
### **Strategy Plane**

#### Site Goals
- To provide comprehensive information and reviews about a wide range of movies, covering various genres and periods, enabling users to discover and learn more about films of their interest.
- To facilitate a vibrant community where users can engage in discussions, share opinions, and connect with fellow movie lovers, enhancing their overall cinematic experience and appreciation.

#### User stories
## User Stories for GoodViews Website

### 1. As a general user:
- **1.1:** I want to easily find what I'm looking for and navigate the site intuitively.
- **1.2:** I want to view the site on any device, ensuring it is fully responsive.
- **1.3:** I want to be able to contact the site for movie recommendations, reporting issues, or general inquiries.
- **1.4:** I want to easily return to the main site without browser navigation if I encounter a non-existent page or a site error.

### 2. As a visitor without an account:
- **2.1:** I want to immediately understand the purpose of the site upon visiting.
- **2.2:** I want to be able to view movie reviews and information without needing an account.
- **2.3:** I want an option to create an account to access more personalized features like rating movies and participating in discussions.

### 3. As a registered user:
- **3.1:** I want to sign into my account easily.
- **3.2:** I want to browse movie reviews and find detailed information about films.
- **3.3:** I want to search and filter movies based on genres, ratings, and other criteria.
- **3.4:** I want to write and post my own movie reviews.
- **3.5:** I want to rate movies and have a list of my ratings easily accessible.
- **3.6:** I want to follow other users and see their reviews and movie recommendations.
- **3.7:** I want to easily log out of my account.

### 4. As a site administrator:
- **4.1:** I want to manage user-generated content for quality and appropriateness.
- **4.2:** I want to add, edit, or delete movie information to keep the database up-to-date.
- **4.3:** I want to respond to user inquiries and provide support as needed.
- **4.4:** I want to analyze user interaction data to improve the site's functionality and user experience.


### **Scope Plane for GoodViews**

#### **Features Planned:**

- **General**
  - Responsive design for optimal viewing on various devices.
  - PostgreSQL Database to store movie information, user profiles, reviews, and ratings.
  - Use of TMDb API to facilitate movie and TV show catalogue.
- **All Users (No Login Required)**
  - Navigation menu for easy access to different sections of the website.
  - Home page with introductory text and featured movies or categories.
  - Movie pages with detailed information, trailers, and user reviews.
  - Integration with movie TMDb database for comprehensive media information.
  - User registration and sign-in forms.
  - Custom error pages (404, 500) for better user experience in case of a problem.

- **Registered Users**
  - Sign-out functionality.
  - Personal profile page displaying user's reviews, ratings, and movie/ tv show watchlists.
  - Movie/ tv show discovery page with filters (genre, release year, ratings, etc.).
  - Ability to rate and review movies/ tv shows.
  - Personalised movie/ tv show recommendations based on user's history and preferences.
  - Option to follow other users and view their reviews and recommendations.

- **Site Administrators**
  - Dashboard for managing website content and user activity.
  - Tools to add, edit, or delete movie information to keep the database current.
  - Ability to manage user accounts and reviews for quality control.
  - Access to site analytics for monitoring engagement and user behavior.
  - Functionality to respond to user inquiries and feedback.

The table shows the importance and difficulty of these features - I will prioritise them based on this during the development process.


| Feature Category | Feature Description | Importance | Difficulty |
|------------------|---------------------|------------|------------|
| General          | Responsive design | High | Medium |
| General          | Database for movie info and user data | High | High |
| All Users        | Navigation menu | High | Medium |
| All Users        | Home page with intro and features | High | Low |
| All Users        | Movie pages with detailed info | High | Medium |
| All Users        | Integration with external movie databases | Medium | High |
| All Users        | User registration and sign-in forms | High | Low |
| All Users        | Custom error pages | Low | Low |
| Registered Users | Sign-out functionality | Medium | Low |
| Registered Users | Personal profile page | High | Medium |
| Registered Users | Movie discovery page with filters | High | Medium |
| Registered Users | Rate and review movies | High | Medium |
| Registered Users | Personalized movie recommendations | Medium | High |
| Registered Users | Follow other users and view their activities | Medium | High |
| Site Admins      | Dashboard for content and user management | High | High |
| Site Admins      | Add, edit, delete movie information | High | High |
| Site Admins      | Manage user accounts and reviews | High | Medium |
| Site Admins      | Site analytics access | Medium | Medium |
| Site Admins      | Respond to user inquiries and feedback | Medium | Low |


#### Wireframes

This section presents the wireframes for the GoodViews website. Creating wireframes is a crucial step in the development process, as they provide a clear visual guideline for the user interface and layout. These wireframes are the initial concepts for how the site will display and organize its content and features. Below are the designs for various pages and functionalities of GoodViews:

<details>
<summary>##### Home Page</summary>
**Description:** This wireframe shows the proposed layout for the home page, featuring elements such as the navigation bar, featured movie/ TV shows sections, and options for user login/signup.

*Insert Home Page Wireframe Image Here*  
[Link Placeholder for Home Page Wireframe Image](#)

</details>

<details>
<summary>##### Movie Detail Page</summary>
**Description:** The wireframe for the movie detail page outlines how information, reviews, and related content for individual movies will be presented.

*Insert Movie Detail Page Wireframe Image Here*  
[Link Placeholder for Movie Detail Page Wireframe Image](#)

</details>

<details>
<summary>##### TV Show Detail Page</summary>
**Description:** The wireframe for the TV show detail page outlines how information, reviews, and related content for individual TV shows will be presented.

*Insert TV Show Detail Page Wireframe Image Here*  
[Link Placeholder for TV Show Detail Page Wireframe Image](#)

</details>

<details>
<summary>##### User Profile Page</summary>
**Description:** This wireframe illustrates the layout for a user's profile page, showcasing sections for personal information, reviews, ratings, and watchlists.

*Insert User Profile Page Wireframe Image Here*  
[Link Placeholder for User Profile Page Wireframe Image](#)

</details>

<details>
<summary>##### Search and Filter Functionality</summary>
**Description:** The design for the search and filtering interface demonstrates how users can effectively find and select movies based on various criteria.

*Insert Search and Filter Functionality Wireframe Image Here*  
[Link Placeholder for Search and Filter Functionality Wireframe Image](#)

</details>

<details>
<summary>##### Error Page</summary>
**Description:** This wireframe outlines the design of the error pages, such as the 404 (Page Not Found) and 500 (Internal Server Error) pages. The focus is on maintaining a user-friendly experience even in the event of an error, by providing helpful messages and links to guide users back to the main content of the GoodViews website.

*Insert Error Page Wireframe Image Here*  
[Link Placeholder for Error Page Wireframe Image](#)

</details>


<details>
<summary>##### Admin Dashboard</summary>
**Description:** As the sole developer and administrator, the wireframe for the admin dashboard is designed to manage content, user activities, and analytics efficiently.

*Insert Admin Dashboard Wireframe Image Here*  
[Link Placeholder for Admin Dashboard Wireframe Image](#)

</details>

---

These wireframes represent initial drafts and are subject to change as the project progresses. They are intended to guide the creation and refinement of the GoodViews website, providing a clear understanding of its structure and user experience from the perspective of the developer.

#### Design

##### Colour Scheme

![GoodViews Colour Scheme](insert filepath)

The colour scheme depicted above was selected for the GoodViews website. This palette was finalized after several iterations throughout the development process, particularly focusing on accessibility and visual appeal. 

The primary colour scheme of GoodViews revolves around a sophisticated and classic cinematic look:
  - Black - Used predominantly for backgrounds, providing a sleek and professional canvas that enhances other colors.
  - White - Employed for text and key elements to ensure high readability and contrast against the black background.
  - Gold - Chosen for highlights, call-to-action buttons, and other critical features, adding a touch of elegance and importance.

Secondary colors include:
- Subtle shades of grey for less prominent but necessary elements, maintaining the site's minimalist and sophisticated aesthetic.
- A consistent color for interactive elements, ensuring intuitive navigation and user experience.

##### Typography

The GoodViews website employs two typefaces that harmoniously complement each other and align with the site's cinematic theme:
- [Cinzel](https://fonts.google.com/specimen/Cinzel) for headings and main titles, reflecting a classic movie feel.
- [Roboto](https://fonts.google.com/specimen/Roboto) for main body text, ensuring clarity and ease of reading across various devices and screens.

These typefaces were chosen for their readability and aesthetic appeal, contributing to a seamless and engaging user experience on the GoodViews platform.

#### Graphics / Imagery

This section details the sources and creation methods for the various graphics and imagery used throughout the GoodViews website.

- **Logo & Favicon:** The logo and favicon for GoodViews were crafted using Canva, providing a unique and recognizable brand identity for the site.

  *Insert link to logo and favicon images here*

*write about other images once they've been used*
All images and graphics used on GoodViews have detailed in the credits section.


### Bugs and Issues

#### Flashed messages not appearing in layout template
The [flashing](https://flask.palletsprojects.com/en/3.0.x/patterns/flashing/) layout specified in the documentation did not work. No messages would flash and they would still be in the queue. 

To workaround this issue I made a Jinja macro which I could import into my `layout.html` inside the `{% block body %}`
without it being overidden by child templates using the `{% block body %}`. 

