import unittest
from unittest.mock import patch, MagicMock
import webScraping

class TestGetDriver(unittest.TestCase):
    @patch('webScraping.webdriver.Chrome')
    @patch('webScraping.Service')
    @patch('webScraping.Options')
    def test_get_driver_chrome(self, mock_options, mock_service, mock_chrome):
        chromedriver_path = "fake/path/chromedriver.exe"
        mock_options_instance = MagicMock()
        mock_options.return_value = mock_options_instance
        mock_service_instance = MagicMock()
        mock_service.return_value = mock_service_instance
        mock_chrome_instance = MagicMock()
        mock_chrome.return_value = mock_chrome_instance

        driver = webScraping.get_driver(chromedriver_path, use_brave=False)

        mock_options.assert_called_once()
        mock_service.assert_called_once_with(executable_path=chromedriver_path)
        mock_chrome.assert_called_once_with(service=mock_service_instance, options=mock_options_instance)
        self.assertEqual(driver, mock_chrome_instance)
        self.assertFalse(hasattr(mock_options_instance, 'binary_location') and mock_options_instance.binary_location)

    @patch('webScraping.webdriver.Chrome')
    @patch('webScraping.Service')
    @patch('webScraping.Options')
    def test_get_driver_brave(self, mock_options, mock_service, mock_chrome):
        chromedriver_path = "fake/path/chromedriver.exe"
        mock_options_instance = MagicMock()
        mock_options.return_value = mock_options_instance
        mock_service_instance = MagicMock()
        mock_service.return_value = mock_service_instance
        mock_chrome_instance = MagicMock()
        mock_chrome.return_value = mock_chrome_instance

        driver = webScraping.get_driver(chromedriver_path, use_brave=True)

        mock_options.assert_called_once()
        mock_service.assert_called_once_with(executable_path=chromedriver_path)
        mock_chrome.assert_called_once_with(service=mock_service_instance, options=mock_options_instance)
        self.assertEqual(driver, mock_chrome_instance)
        self.assertEqual(mock_options_instance.binary_location, r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe")

if __name__ == '__main__':
    unittest.main()