from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from .models import Book
from django.contrib.auth.models import User

class BookAPITestCase(APITestCase):
    
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='password')
        self.client = APIClient()
        self.client.login(username='testuser', password='password')
        
        # Create some Book objects
        self.book1 = Book.objects.create(title="Book 1", author="Author 1", publication_year=2000)
        self.book2 = Book.objects.create(title="Book 2", author="Author 2", publication_year=2010)
        
        self.book_list_url = reverse('book-list')  # Ensure the URL is named in your urls.py
        self.book_detail_url = lambda pk: reverse('book-detail', args=[pk])



    def test_create_book(self):
        data = {
            'title': 'New Book',
            'author': 'New Author',
            'publication_year': 2024
        }
        response = self.client.post(self.book_list_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)  # We already have 2 books in setUp
        self.assertEqual(Book.objects.last().title, 'New Book')



    def test_retrieve_book(self):
        response = self.client.get(self.book_detail_url(self.book1.pk))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Book 1')
    def test_update_book(self):
        data = {
            'title': 'Updated Book',
            'author': 'Updated Author',
            'publication_year': 2025
        }
        response = self.client.put(self.book_detail_url(self.book1.pk), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, 'Updated Book')

    def test_delete_book(self):
        response = self.client.delete(self.book_detail_url(self.book1.pk))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)

    def test_filter_books(self):
        response = self.client.get(f"{self.book_list_url}?publication_year=2000")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Book 1')

    def test_search_books(self):
        response = self.client.get(f"{self.book_list_url}?search=Author 1")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['author'], 'Author 1')


    def test_order_books(self):
        response = self.client.get(f"{self.book_list_url}?ordering=title")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['title'], 'Book 1')
        self.assertEqual(response.data[1]['title'], 'Book 2')
    def test_create_book_without_authentication(self):
        self.client.logout()  # Log out the test user
        data = {
            'title': 'Unauthorized Book',
            'author': 'Unauthorized Author',
            'publication_year': 2024
        }
        response = self.client.post(self.book_list_url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

