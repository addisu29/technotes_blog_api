from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Category

class BlogAPITests(APITestCase):
    
    def setUp(self):
        # Create a category 
        self.category = Category.objects.create(name="Coding")

    def test_view_posts(self):
        """Test that we can access the posts endpoint"""
        url = reverse('post-list') # This matches the router name
        response = self.client.get(url)
        
        # Check if the status code is 200 (Success)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_category_exists(self):
        """Test if the category was created correctly"""
        cat = Category.objects.get(name="Coding")
        self.assertEqual(cat.name, "Coding")