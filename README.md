# Grazioso Salvare Animal Shelter Dashboard

![Grazioso Salvare Logo](logo.png)

**Author:** Sarvarbek Fazliddinov  
**Course:** CS 340 – Client/Server Development  

---

## About the Project

This project implements a functional MongoDB dashboard for **Grazioso Salvare**, an international animal rescue training company. The dashboard enables users to identify and categorize dogs that are suitable candidates for various types of search-and-rescue training based on data from the Austin Animal Center shelter dataset.

The application follows the **Model-View-Controller (MVC)** design pattern:
- **Model:** MongoDB database  
- **View:** Dash dashboard widgets and visualizations  
- **Controller:** Python callback functions that manage interaction between the database and dashboard components  

---

## Required Functionality

The dashboard provides the following features:

- **Interactive Filtering Options**  
  Radio buttons allow users to filter dogs by rescue type:
  - Water Rescue  
  - Mountain or Wilderness Rescue  
  - Disaster or Individual Tracking  
  - Reset (Show All)

- **Dynamic Data Table**  
  An interactive data table that responds to filter selections with:
  - Pagination  
  - Sorting  
  - Column filtering  

- **Geolocation Chart**  
  A Leaflet map displaying the geographic location of selected animals with popup details.

- **Breed Distribution Chart**  
  A pie chart showing the distribution of dog breeds based on the current filter.

- **Branding**  
  Grazioso Salvare logo and unique project identifier displayed prominently.

---

## Dashboard Screenshots

The screenshots below demonstrate the functionality of each rescue filter.

### 1. Starting State (Reset / Show All)

Default unfiltered view displaying all animals in the database, including a variety of breeds such as Pit Bull Mix, Labrador Retriever Mix, Domestic Shorthair Mix, and others.

![Starting State – Show All](screenshot_reset.png)

---

### 2. Water Rescue Filter

Displays **Labrador Retriever Mix** dogs that are **intact females** between **26–156 weeks old**, suitable for water rescue training.

![Water Rescue Filter](screenshot_water_rescue.png)

---

### 3. Mountain or Wilderness Rescue Filter

Displays **German Shepherd Mix**, **Alaskan Malamute**, **Siberian Husky Mix**, and **Rottweiler Mix** dogs that are **intact males** between **26–156 weeks old**, suitable for mountain or wilderness rescue training.

![Mountain or Wilderness Rescue Filter](screenshot_mountain_rescue.png)

---

### 4. Disaster or Individual Tracking Filter

Displays **German Shepherd Mix**, **Bloodhound**, and **Rottweiler Mix** dogs that are **intact males** between **20–300 weeks old**, suitable for disaster rescue and individual tracking.

![Disaster or Individual Tracking Filter](screenshot_disaster_rescue.png)

---

## Tools Used

- **MongoDB**  
  Used as the database due to its flexibility and strong compatibility with Python via PyMongo.

- **Dash (Plotly)**  
  Used to build the interactive web dashboard, including tables, charts, maps, and callback functionality.

- **Python**  
  Used to implement the CRUD module, database queries, and dashboard logic.

---

## Steps to Complete

1. Set up MongoDB and imported the animal shelter CSV dataset  
2. Created a reusable CRUD Python module for database operations  
3. Built the dashboard layout including logo, filters, data table, charts, and map  
4. Developed MongoDB queries for each rescue type  
5. Connected all components using Dash callback functions  
6. Tested functionality and captured dashboard screenshots  

---

## Challenges

One major challenge was handling MongoDB’s `_id` (ObjectID) field, which caused issues when rendering the data table. This was resolved by removing the `_id` column from the DataFrame before displaying it in Dash.

Another challenge involved breed name consistency. Some rescue filters initially returned no results because breed names in the dataset included `"Mix"` suffixes. Adjusting queries to match the actual dataset resolved the issue.

---

## Resources

- Austin Animal Center Outcomes Dataset  
- Dash Documentation: https://dash.plotly.com/  
- MongoDB Documentation: https://docs.mongodb.com/  

---

## Portfolio Reflection (CS 340)

This repository serves as a portfolio artifact demonstrating my ability to design client-driven database applications using MongoDB and Python. The modular CRUD design improves maintainability, reusability, and scalability, while the interactive dashboard transforms raw data into actionable information for real-world decision-making.
