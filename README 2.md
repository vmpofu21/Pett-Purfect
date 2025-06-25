Purr-fect Match Pett
By Vanessa Mpofu and Jagrit Dhingra



CLARITY OF PURPOSE

Mission Statement: 
Connecting pet lovers and their furry friends for fun, friendship, and forever bonds – Purrfect is where tails wag and hearts meet!

Summary Statement:
Purr-fect Match Pett is a unique platform that blends pet-friendly social networking and dating for pet lovers. Unlike traditional dating apps, our app is designed to prioritize the bonds between pets and their owners, creating opportunities for romantic connections, friendships, and pet playdates. Whether you’re a single pet parent or just looking to expand your pet’s social circle, our app ensures everyone, fur babies included, feels at home.

Goals:

Target Audience - Use Cases:

Persona 1: ALEX ROOT – The New Pet Parent
Age: 27
Occupation: Junior Graphic Designer
Location: Urban apartment, Chicago
Pet: 6-month-old Golden Retriever (named Max)
Bio:
 Alex just adopted Max and is feeling overwhelmed with being a first-time dog parent. He’s looking for a supportive community to exchange tips, get advice on training, and find local dog-friendly meetups. Socially introverted, Alex prefers online interactions first before attending real-world events.
Goals:
Find beginner-friendly pet care resources
Join local dog meetups to help socialize Max
Connect with other new pet owners for shared experiences

Use Case:
Alex wants to find a local puppy playdate for his Golden Retriever, Max, to help socialize him.
Storyboard:
Alex logs into Purr-fect Match Pett and sees a personalized "Upcoming Events" section. Then he clicks "Puppy Playdates Near You". An interactive map with pins appears and he selects "Lincoln Park Puppy Social - Sunday 3 PM". Alex clicks "Join Event" and receives a confirmation and details. A group chat opens automatically so Alex can message other attendees and break the ice beforehand.
Persona 2: JACK PATEL – The Experienced Animal Enthusiast
Age: 35
Occupation: Small Business Owner (Pet Supplies Store)
Location: Suburban neighborhood, Austin, TX
Pet: Two cats (Luna & Simba) and a rescue beagle (Buddy)
Bio:
 Jack has been a lifelong animal lover and actively volunteers at shelters. He’s well-versed in pet behavior and enjoys educating others. He’s looking for a platform to share his knowledge, promote his store, and maybe even mentor new pet parents.
Goals:
Offer support and advice to the community
Network with other animal lovers and pet-related businesses
Increase the visibility of his local pet store and services
Use Case:
Jack wants to share his pet care tips and promote his local pet store’s workshop to new pet owners.
Storyboard:
Jack logs in and clicks on the "Community Board." He then creates a post titled "Free Dog Grooming Workshop This Saturday!" The interactive editor allows him to link the event directly with RSVP capability. Jack tags himself as a "Mentor" so new users know he’s available for advice. He gets replies, questions, and RSVP confirmations from pet parents.


Persona 3: LARA CROFT – The Adventurous Pet Explorer
Age: 31
Occupation: Travel Blogger / Content Creator
Location: Nomadic, based wherever her campervan is parked
Pet: Bengal cat (Shadow) and Australian Shepherd (Rex)
Bio:
 Lara lives for adventures and documents her road trips with her pets on social media. She's passionate about finding pet-friendly locations, hiking trails, and campsites. She wants to connect with like-minded pet owners who love exploring and share pet travel tips.
Goals:
Find pet-friendly travel recommendations
Collaborate with other adventurous pet lovers
Share stories, blogs, and content about traveling with pets
Use Case:
Lara wants to find pet-friendly hiking trails during her road trip and share content with the community.
Storyboard:
Lara opens the app and selects the "Pet-Friendly Explore" feature. She filters for "Hiking Trails" and "Dogs Allowed." She selects "Riverbend Canyon Trail" and reads user reviews, safety tips, and pet-friendly features. After hiking, Lara uploads photos, tags her location, and writes a quick blog review through the app’s "Share Adventure" feature.



OVERALL DESIGN 
What we have implemented:
Users can log in or create an account
Users can add their pets
Users can view, like, or unlike other pets’ profiles
After liking a pet’s profile, users can message the pet’s owner
Users can filter pets by age or species
Users can search for pets by name or species
Users can sort the pets in A→Z or Z→A, or by Location
Users can edit their profiles by:
changing their profile picture or,
Rewriting their bios
Users can edit their pets’ profiles by: 
changing their profile picture, 
rewriting their bios, or 
making the profile active or inactive
Users can upload blog posts or just read
Users can ONLY rsvp to events such as play dates/meetups
When users RSVP to an event, they get a confirmation email

Annotated Designs of Prototypes:


Login Page

When users get to our web application, they will be asked to log in. If they don’t have an account, they will be asked to sign up (basically creating an account)

Home page

The Home page contains profiles of other pets on the website. As a user, you can connect with these pet owners.


Profile page

The navigation bar at the top provides clear and accessible links to core sections like Home, Events, Blog, and Profile, helping users understand where they are and move between sections with ease. The “Profile” tab is highlighted, offering clear visual feedback. The left section prioritizes personal identity, showing a friendly profile picture and name, immediately establishing user recognition. 

Events page

The user can ONLY rsvp to an event but cannot create an event. There’s just about enough information the user needs to know and prepare for a certain event that they would have RSVP’d to.






Screenshots of the Final Web Application:
Home page


For the home page, we added a couple of advanced features such as Sort By, Search, and Filter. We incorporated some AJAX within the Search feature, which enabled auto-completion. When the user clicks on the “View Pet” button, it takes them to a page with the pet’s details, and the user can unlike/like the pet, which opens up an option for mutual-like messaging. The like/unlike feature was also implemented with some AJAX. 

Events page


We built the events page using Bootstrap along with custom CSS for styling. Users can easily RSVP “Yes” or “No” to any event, and they automatically receive a confirmation email upon responding.

Messages - with a sample conversation

When a user “Likes” a pet’s profile, they are instantly granted access to message the pet’s owner. This feature fosters direct communication between users, helping them connect over shared interests in pets. It adds a social and interactive element to the platform, enhancing user engagement and community building.

Profile page

On the Profile page, users can edit their personal information or add a new pet to their account. They also have the option to upload or change their profile picture for a more personalized experience. To help users keep track of their interactions, all liked pets are displayed directly on their profile. This layout makes it easy to manage activity and stay connected with favorite pets on the platform.



TECHNICAL CONTRIBUTION 

Database Schema Diagram: 


This database diagram shows the three main types of relationships between tables: one-to-one (1-1), one-to-many (1-M), and many-to-many (M-M). These relationships help explain how different types of information in the system are connected. In a one-to-many relationship, one record in a table can be linked to many records in another table. For instance, one user can create multiple blog posts, meaning the same user ID appears many times in the blog posts table. Similarly, a single user can own multiple pets, send and receive many messages, give likes to many pets, and RSVP to multiple events. Each of these cases shows a situation where one user is connected to many items in another table. Pets also have a one-to-many relationship with likes, since a single pet can be liked by many users. Events also follow this pattern one event can have many users RSVP to it.

On the other hand, a many-to-many relationship allows many records in one table to be linked to many records in another. This is usually handled using a third, or “join” table. In this diagram, the ‘event_rsvps’ table is used to connect users and events. This means that one user can RSVP to many different events, and each event can have many different users who RSVP. The ‘event_rsvps’ table holds the user ID and the event ID together in each row to show which users have responded to which events. 

Routes Flow Chart:





List of advanced features:
Filter pets by species or age
Sort pet listings A–Z or Z–A
Search by pet name or species
Emails to users when they RSVP to an event
Like/unlike
Mutual messaging
Hosted the website

Annotated code snippets of the Advanced Features:

Messaging feature


This Flask route handles polling for chat messages between the currently logged-in user and another user identified by user_id. It retrieves messages sent by and received from the specified user, combines them, and orders them by their timestamp. The route then returns the messages as a JSON array, including metadata such as sender and receiver IDs, usernames, message content, timestamp, and a flag indicating if the message was sent by the current user. If the other user does not exist, it responds with a 404 error.



Unlike/like code

This JavaScript code enables a "like" and "unlike" feature for a pet profile using AJAX. When the page loads, it attaches a click event to the like button. When the button is clicked, it sends a POST request to either the /like/<pet_id> or /unlike/<pet_id> route, depending on the current state. After the server responds, it updates the button to reflect the new state (Like or Unlike) without reloading the page.


















Filter feature code

This Flask route handles requests to the home or index page and displays a list of active pets with optional filtering and sorting. It allows users to search for pets by name or species, and apply filters based on species or age ranges (0–2, 3–5, or 6+ years old). The results are paginated, and the current page number is taken from the query parameters. This makes it easy for users to browse and find pets that match their preferences.








Edit Profile Form code

This code defines a Flask-WTF form called EditProfileForm for users to update their profile information. The form includes fields for name, username, a short bio, and an optional profile picture (limited to JPG and PNG formats). It checks that the username is not already taken, unless it’s the same as the user’s original one. If a new username is entered and already exists in the database, the form raises a validation error to prompt the user to choose a different one.


FUTURE DEVELOPMENT POTENTIAL 


Petfinder API Integration
Connect to real-time adoptable pet listings and support in-app applications.
Chat with Shelters
Add direct messaging for quick communication with adoption centers.
OpenAI API Integration for Recommendations
Suggest pets based on user searches and interaction history.
Google Places API Integration for Map View
Display all pets on a map based on the user's location.

