from .models import Letting, Address

from django.test import TestCase
from django.urls import reverse


class LettingsIndexTest(TestCase):
    def test_lettings_index_url(self):
        """Test acces to index page."""
        response = self.client.get(reverse("lettings:index"))
        assert response.status_code in [200]

    def test_lettings_index_correct_content(self):
        """Test display the correct content to index page."""
        response = self.client.get(reverse("lettings:index"))
        self.assertIn(b"Lettings", response.content)
        self.assertIn(b"Home", response.content)
        self.assertIn(b"Profiles", response.content)
        assert response.status_code in [200]

    def test_lettings_index_return_correct_title(self):
        """Test display the correct context to index page."""
        response = self.client.get(reverse("lettings:index"))
        self.assertInHTML("Lettings", "Lettings")
        assert response.status_code in [200]

    def test_lettings_correct_template(self):
        """Test display the correct template to index page."""
        response = self.client.get(reverse("lettings:index"))
        self.assertTemplateUsed(response, "letting/index.html")
        assert response.status_code in [200]


class LettingsPageTest(TestCase):
    def setUp(self):
        """Create data example ."""
        Address.objects.create(
            number=1234,
            street="Test street",
            city="Test city",
            state="AA",
            zip_code=00000,
            country_iso_code="AAA",
        )
        address_test = Address.objects.first()
        Letting.objects.create(title="Test Title", address=address_test)

    def test_letting_correct_url(self):
        """Test access to letting page."""
        letting_test = Letting.objects.first()
        response = self.client.get(reverse("lettings:letting", args=[letting_test.id]))
        assert response.status_code in [200]

    def test_letting_correct_content(self):
        """Test display the correct context to letting page."""
        letting_test = Letting.objects.first()
        response = self.client.get(reverse("lettings:letting", args=[letting_test.id]))
        self.assertIn(b"Back", response.content)
        self.assertIn(b"Home", response.content)
        self.assertIn(b"Profiles", response.content)
        assert response.status_code in [200]

    def test_letting_correct_title(self):
        """Test display the correct title to letting page."""
        letting_test = Letting.objects.first()
        response = self.client.get(reverse("lettings:letting", args=[letting_test.id]))
        self.assertInHTML("Lettings", "Lettings")
        assert response.status_code in [200]

    def test_letting_correct_template(self):
        """Test display the correct template to letting page."""
        letting_test = Letting.objects.first()
        response = self.client.get(reverse("lettings:letting", args=[letting_test.id]))
        self.assertTemplateUsed(response, "letting/letting.html")
        assert response.status_code in [200]
