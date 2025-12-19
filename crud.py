# crud.py
# =============================================================================
# CRUD Python Module for Grazioso Salvare Animal Shelter Database
# =============================================================================
# Purpose: Provides Create, Read, Update, Delete operations for MongoDB
# Author: Sarvarbek Fazliddinov
# Course: CS 340 - Client/Server Development
# =============================================================================

from pymongo import MongoClient
from pymongo.errors import PyMongoError


class AnimalShelter:
    """
    A class to perform CRUD operations on the AAC animal shelter MongoDB database.
    
    Attributes:
        client (MongoClient): MongoDB client connection
        database (Database): Reference to the AAC database
    """
    
    def __init__(self, username, password):
        """
        Initialize the AnimalShelter class with database connection.
        
        Args:
            username (str): MongoDB username for authentication
            password (str): MongoDB password for authentication
        """
        # Build connection URI with authentication credentials
        self.client = MongoClient(f'mongodb://{username}:{password}@localhost:27017')
        # Connect to the AAC (Austin Animal Center) database
        self.database = self.client['aac']
    
    # =========================================================================
    # CREATE - Insert a new document into the animals collection
    # Input: data (dict) - key/value pairs for the new document
    # Return: True if successful, False otherwise
    # =========================================================================
    def create(self, data):
        """Insert a document into the animals collection."""
        # Validate that data is not None or empty
        if data is not None:
            try:
                # Insert the document into animals collection
                result = self.database.animals.insert_one(data)
                # Return True if inserted_id exists (successful insert)
                return True if result.inserted_id else False
            except PyMongoError as e:
                # Handle any MongoDB errors
                print("Error inserting document:", e)
                return False
        return False
    
    # =========================================================================
    # READ - Query documents from the animals collection
    # Input: query (dict) - key/value pairs for search criteria
    # Return: List of matching documents, empty list if none found
    # =========================================================================
    def read(self, query):
        """Query for documents in the animals collection."""
        try:
            # Use find() to return all matching documents (not find_one)
            cursor = self.database.animals.find(query)
            # Convert cursor to list for easier manipulation
            results = list(cursor)
            return results
        except PyMongoError as e:
            # Handle any MongoDB errors
            print("Error reading documents:", e)
            return []
    
    # =========================================================================
    # UPDATE - Modify existing documents in the animals collection
    # Input: query (dict) - criteria to find documents to update
    #        new_values (dict) - key/value pairs to update
    # Return: Number of documents modified
    # =========================================================================
    def update(self, query, new_values):
        """Update documents matching the query criteria."""
        try:
            # Use update_many with $set operator to modify fields
            result = self.database.animals.update_many(query, {"$set": new_values})
            # Return count of modified documents
            return result.modified_count
        except PyMongoError as e:
            # Handle any MongoDB errors
            print("Error updating documents:", e)
            return 0
    
    # =========================================================================
    # DELETE - Remove documents from the animals collection
    # Input: query (dict) - criteria to find documents to delete
    # Return: Number of documents deleted
    # =========================================================================
    def delete(self, query):
        """Delete documents matching the query criteria."""
        try:
            # Use delete_many to remove all matching documents
            result = self.database.animals.delete_many(query)
            # Return count of deleted documents
            return result.deleted_count
        except PyMongoError as e:
            # Handle any MongoDB errors
            print("Error deleting documents:", e)
            return 0
