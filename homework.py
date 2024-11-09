import requests


class Homework:
    @staticmethod
    def get(url: str) -> str:
        """
        Sends a GET request to the specified URL and returns the response text.

        Args:
            url (str): The URL to send the GET request to.

        Returns:
            str: The response text from the GET request.
        """
        return requests.get(url).text

    @staticmethod
    def post(data: dict, url: str) -> str:
        """
        Sends a POST request with the given data to the specified URL and returns the response text.

        Args:
            data (dict): The data to send in the POST request.
            url (str): The URL to send the POST request to.

        Returns:
            str: The response text from the POST request.
        """
        return requests.post(url, json=data).text
