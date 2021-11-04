from django.test import TestCase


class TestIndex(TestCase):
    def setUp(self):
        """Change view.py variable datas."""
        self.fake_url_index = "/fake_index.html"

    def test_correct_url_index(self):
        """Test acces to index page with the correct url."""
        result = self.client.get("/")
        assert result.status_code in [200]

    def test_fake_url_index(self):
        """Test acces to index page with a fake url."""
        response = self.client.get(self.fake_url_index)
        assert response.status_code in [404]