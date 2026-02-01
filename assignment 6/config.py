
BS_USERNAME = "baglantolegenov_boTV1N"
BS_ACCESS_KEY = "5x3NrYDtNHbAL7P1hswC"

# BrowserStack Hub URL
BS_HUB_URL = f"https://{BS_USERNAME}:{BS_ACCESS_KEY}@hub-cloud.browserstack.com/wd/hub"

# Browser configurations
# We'll test on 2 different browsers
BROWSER_CONFIGS = [
    {
        'name': 'Chrome_Windows',
        'browserName': 'Chrome',
        'browserVersion': 'latest',
        'os': 'Windows',
        'osVersion': '11',
        'sessionName': 'Login Test - Chrome on Windows 11',
        'buildName': 'Assignment 6 - Task 2'
    },
    {
        'name': 'Firefox_Windows',
        'browserName': 'Firefox',
        'browserVersion': 'latest',
        'os': 'Windows',
        'osVersion': '11',
        'sessionName': 'Login Test - Firefox on Windows 11',
        'buildName': 'Assignment 6 - Task 2'
    }
]

# Optional: Add more browser configurations
# Uncomment to test on Safari or Edge
"""
    {
        'name': 'Safari_Mac',
        'browserName': 'Safari',
        'browserVersion': 'latest',
        'os': 'OS X',
        'osVersion': 'Monterey',
        'sessionName': 'Login Test - Safari on Mac',
        'buildName': 'Assignment 6 - Task 2'
    },
    {
        'name': 'Edge_Windows',
        'browserName': 'Edge',
        'browserVersion': 'latest',
        'os': 'Windows',
        'osVersion': '11',
        'sessionName': 'Login Test - Edge on Windows 11',
        'buildName': 'Assignment 6 - Task 2'
    }
"""