"""
Driver do Selenium
nov.22
"""

from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from traquitanas.scrapping import adds, gecko


class Driver(webdriver.Firefox):
    """
    Cria driver customizado do Selenium

    :param webdriver: _description_
    :type webdriver: _type_
    """

    def __init__(
        self, my_driver_path, my_logs_path, my_download_path, *args, **kwargs
    ):
        """
        verify_ssl

        :param my_driver_path: _description_
        :type my_driver_path: pathlib
        :param my_logs_path: _description_
        :type my_logs_path: pathlib
        """
        # Services
        gecko_path = gecko.get_path_geckodriver(
            my_driver_path, verify_ssl=kwargs['verify_ssl']
        )

        # Logs
        logs_filepath = my_logs_path / 'geckodriver.log'

        # Services
        my_service = FirefoxService(
            executable_path=gecko_path, log_path=logs_filepath
        )

        # Options
        my_options = FirefoxOptions()
        my_options.headless = False
        my_options.set_preference('intl.accept_languages', 'pt-BR, pt')
        my_options.set_preference('browser.download.folderList', 2)
        my_options.set_preference('browser.download.dir', str(my_download_path))
        my_options.set_preference(
            'browser.download.manager.showWhenStarting', 'false'
        )
        my_options.set_preference(
            'browser.helperApps.neverAsk.saveToDisk',
            'application/octet-stream;application/vnd.ms-excel;text/html',
        )

        # Driver
        my_driver = super(Driver, self)
        my_driver.__init__(service=my_service, options=my_options)

    def add_extension_xpath(self, my_adds_path):
        """
        Adiciona Xpath extension

        :param my_adds_path: Pasta da Extensão
        :type my_adds_path: pathlib
        """
        adds.add_extension_xpath(self, my_adds_path)


if __name__ == '__main__':
    pass
