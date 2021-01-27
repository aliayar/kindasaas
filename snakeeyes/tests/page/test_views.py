from flask import url_for


class TestPage(object):

    def test_home_page(self, client):
        """
        Home page should respond with a 200, success.
        """
        response = client.get(url_for('page.home'))
        assert response.status_code == 200

    def test_terms_page(self, client):
        """
        Terms page should respond with a 200, success.
        """
        response = client.get(url_for('page.terms'))
        assert response.status_code == 200

    def test_privacy_page(self, client):
        """
        Privacy page should respond with a 200, success.
        """
        response = client.get(url_for('page.privacy'))
        assert response.status_code == 200

    def test_faq_page(self, client):
        """
        FAQ page should respond with a 200, success.
        """
        response = client.get(url_for('page.faq'))
        assert response.status_code == 200

    def test_faq_page_title(self, client):
        """
        This page should have a title
        """
        response = client.get(url_for('page.faq'))
        assert '<title>' in str(response.data)
        assert '</title>' in str(response.data)
