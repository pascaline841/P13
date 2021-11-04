from .models import Profile

from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse


class ProfilesIndexTest(TestCase):
    def test_profiles_index_url(self):
        """Test acces to index page."""
        response = self.client.get(reverse("profiles:index"))
        assert response.status_code in [200]

    def test_profiles_index_correct_content(self):
        """Test display the correct content to index page."""
        response = self.client.get(reverse("profiles:index"))
        self.assertIn(b"Profiles", response.content)
        self.assertIn(b"Home", response.content)
        self.assertIn(b"Profiles", response.content)
        assert response.status_code in [200]

    def test_profiles_index_return_correct_title(self):
        """Test display the correct context to index page."""
        response = self.client.get(reverse("profiles:index"))
        self.assertInHTML("Profiles", "Profiles")
        assert response.status_code in [200]

    def test_profiles_correct_template(self):
        """Test display the correct template to index page."""
        response = self.client.get(reverse("profiles:index"))
        self.assertTemplateUsed(response, "profile/index.html")
        assert response.status_code in [200]


class ProfilesPageTest(TestCase):
    def setUp(self):
        """Change view.py datas example."""
        User.objects.create(
            username="johndoe",
            first_name="John",
            last_name="Doe",
            email="john.doe@test.com",
        )
        user_test = User.objects.first()
        Profile.objects.create(user=user_test, favorite_city="Test Favorite City")

    def test_profile_correct_url(self):
        """Test acces to profile page."""
        user_test = User.objects.first()
        response = self.client.get(
            reverse("profiles:profile", args=[user_test.username])
        )
        assert response.status_code in [200]

    def test_profile_correct_content(self):
        """Test display the correct context to profile page."""
        user_test = User.objects.first()
        response = self.client.get(
            reverse("profiles:profile", args=[user_test.username])
        )
        self.assertIn(b"Back", response.content)
        self.assertIn(b"Home", response.content)
        self.assertIn(b"Lettings", response.content)
        assert response.status_code in [200]

    def test_profile_correct_title(self):
        """Test display the correct context to profile page."""
        user_test = User.objects.first()
        response = self.client.get(
            reverse("profiles:profile", args=[user_test.username])
        )
        self.assertInHTML(user_test.username, f"<h1>{user_test.username}</h1>")
        assert response.status_code in [200]

    def test_profile_correct_template(self):
        """Test display the correct template to profile page."""
        user_test = User.objects.first()
        response = self.client.get(
            reverse("profiles:profile", args=[user_test.username])
        )
        self.assertTemplateUsed(response, "profile/profile.html")
        assert response.status_code in [200]
