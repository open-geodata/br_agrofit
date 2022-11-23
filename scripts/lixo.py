


# Download add-ons: xpath
url = 'https://addons.mozilla.org/firefox/downloads/file/3588871/xpath_finder-1.0.2-fx.xpi'
r = requests.get(url)
with open(adds_path / 'xpath.xpi', 'wb') as f:
    f.write(r.content)



# Download add-ons: content_type
r = requests.get('https://addons.mozilla.org/firefox/downloads/file/3718676/content_type_fixer-1.7.1-fx.xpi')
with open(adds_path / 'content_type.xpi', 'wb') as f:
    f.write(r.content)    




# Set Profile
profile = webdriver.FirefoxProfile()
profile.set_preference('intl.accept_languages', 'pt-BR, pt')
profile.set_preference('browser.download.folderList', 2)
profile.set_preference('browser.download.manager.showWhenStarting', False)
profile.set_preference('browser.download.dir', os.getcwd())
profile.set_preference('browser.helperApps.neverAsk.saveToDisk', 'application/octet-stream, application/pdf, application/vnd.ms-excel')
profile.set_preference('general.useragent.override', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36')
profile.set_preference('pdfjs.disabled', True)
profile.set_preference('plugin.scan.Acrobat', '99.0')
profile.set_preference('plugin.scan.plid.all', False)
profile.set_preference('browser.helperApps.showOpenOptionForPdfJS', False)
profile.set_preference('browser.download.forbid_open_with', True)

# Set Options
options = Options()
options.headless = False

# Set Driver
driver = webdriver.Firefox(firefox_profile=profile, options=options, service_log_path='../logs/geckodriver.log')
driver.install_addon(adds_path / 'xpath.xpi', temporary=True)
driver.install_addon(adds_path / 'content_type.xpi', temporary=True)