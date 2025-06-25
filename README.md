# 🐾 Purr-fect Match Pett

**By Vanessa Mpofu and Jagrit Dhingra**  
Connecting pet lovers and their furry friends for fun, friendship, and forever bonds – *Purr-fect* is where tails wag and hearts meet!

---

## 🚀 Overview

**Purr-fect Match Pett** is a unique web platform that blends pet-friendly social networking with dating for pet lovers. Unlike traditional dating or social apps, our focus is on strengthening the bond between pets and their owners while fostering romantic connections, friendships, and pet playdates.

Whether you’re a single pet parent or just want your pet to have more furry friends, Purr-fect makes everyone – humans and animals alike – feel welcome.

---

## 🎯 Goals

- Provide a safe, friendly community for pet lovers
- Facilitate meaningful friendships and relationships
- Offer localized pet meetups and playdates
- Promote knowledge sharing and pet care tips

---

## 🧑‍💻 Target Audience & Use Cases

### Persona 1: **Alex Root – The New Pet Parent**
- **Age:** 27 | **Occupation:** Graphic Designer | **Location:** Chicago  
- **Pet:** Max (Golden Retriever, 6 months)

**Goals:**
- Learn pet care tips
- Socialize his pup
- Connect with other first-time pet owners

**Use Case:**  
Alex finds a local puppy playdate via the "Events Near You" section. He RSVPs, joins a group chat, and gets connected with other new pet parents.

---

### Persona 2: **Jack Patel – The Experienced Animal Enthusiast**
- **Age:** 35 | **Occupation:** Pet Store Owner | **Location:** Austin, TX  
- **Pets:** Luna, Simba (Cats), Buddy (Beagle)

**Goals:**
- Mentor new pet parents
- Promote his pet store
- Share pet knowledge

**Use Case:**  
Jack uses the Community Board to post about an upcoming dog grooming workshop and tags himself as a mentor. He receives RSVP confirmations and messages from users.

---

### Persona 3: **Lara Croft – The Adventurous Pet Explorer**
- **Age:** 31 | **Occupation:** Travel Blogger | **Location:** Nomadic  
- **Pets:** Shadow (Bengal Cat), Rex (Australian Shepherd)

**Goals:**
- Find pet-friendly travel spots
- Share stories and travel tips
- Connect with fellow explorers

**Use Case:**  
Lara uses the "Pet-Friendly Explore" feature to find hiking trails. She shares a blog post with photos and reviews after her adventure.

---

## 💡 Features

### ✅ Core Features Implemented
- User registration & login
- Add, edit, and manage pet profiles
- Like/unlike pet profiles
- Mutual-like messaging system
- Filter, sort, and search pets
- RSVP to events (with confirmation email)
- Upload and read blog posts

### ✅ Advanced Features
- AJAX-powered Like/Unlike system
- Auto-complete pet search bar
- Real-time chat messaging
- Profile & pet profile editing with file uploads
- Filter pets by species & age group
- Sort pets alphabetically or by location

---

## 🖥️ UI/UX Design

### Home Page
- View pet profiles
- Search, filter, and sort pets
- Like/unlike and view details

### Profile Page
- Edit user bio and picture
- Manage pet profiles
- View liked pets

### Events Page
- Browse and RSVP to upcoming events
- Auto-email confirmation

### Messaging
- Initiate conversation after mutual likes
- Real-time communication via AJAX

### Blog
- Post and read user-generated pet content

---

## 🗃️ Database Schema

- **Users ↔ Pets** (One-to-Many)
- **Users ↔ Likes ↔ Pets** (Many-to-Many)
- **Users ↔ Messages ↔ Users** (Two-way communication)
- **Users ↔ BlogPosts** (One-to-Many)
- **Users ↔ Events ↔ RSVPs** (Many-to-Many via join table)

Includes:
- Relational integrity with foreign keys
- Validation for usernames and profile data
- Secure password handling

---

## 🔄 Routes Flow Chart

- `/login`, `/logout`, `/register`
- `/home` – View pets
- `/profile` – Edit profile, add/edit pets
- `/messages/<user_id>` – Chat view
- `/events` – RSVP to events
- `/blog` – Read/write blog posts

---

## 🔍 Code Snippet Highlights

### 🔁 Messaging (Polling Route)
```python
@app.route('/poll_messages/<user_id>')
def poll_messages(user_id):
    # Combines sent/received messages and returns them ordered by timestamp
