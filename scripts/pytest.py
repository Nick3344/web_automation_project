def test_login():
    driver.get('https://example.com/login')
    login(driver, 'username', 'password')
    assert 'Dashboard' in driver.title
