from selenium.webdriver.common.by import By
from selenium import webdriver
import time
from django.test import TestCase


# to run tests -> python manage.py test
# Create your tests here.
class ShopTest(TestCase):
    @classmethod
    def setUpTestData(self):
        self.username = 'sonyxme2'
        self.password = 'Minibika13'

    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument(
            "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36")

        self.driver = webdriver.Chrome(
            executable_path="driver/chromedriver.exe",
            options=options)

    def test_1_register(self):
        first_name = 'Mila'
        last_name = 'Bochkova'
        username = 'milaxme3'
        email = 'example_email@gmail.com'
        password = 'ytrewq4321'

        driver = self.driver
        driver.get('http://127.0.0.1:8000/api/')
        driver.maximize_window()
        time.sleep(1)

        reg_main_btn = driver.find_element(By.ID, 'accountRegistration').click()

        first_name_inp = driver.find_element(By.ID, 'first-name')
        first_name_inp.clear()
        first_name_inp.send_keys(first_name)

        last_name_inp = driver.find_element(By.ID, 'last-name')
        last_name_inp.clear()
        last_name_inp.send_keys(last_name)

        username_inp = driver.find_element(By.ID, 'username')
        username_inp.clear()
        username_inp.send_keys(username)

        email_inp = driver.find_element(By.ID, 'email')
        email_inp.clear()
        email_inp.send_keys(email)

        passw1_inp = driver.find_element(By.ID, 'password1')
        passw1_inp.clear()
        passw1_inp.send_keys(password)

        passw2_inp = driver.find_element(By.ID, 'password2')
        passw2_inp.clear()
        passw2_inp.send_keys(password)

        register_btn = driver.find_element(By.ID, 'enterInAccount').click()

        time.sleep(3)

        get_url = driver.current_url
        self.assertEqual(get_url, 'http://127.0.0.1:8000/api/home/')

        # result_text = driver.find_element(By.ID, 'results').text
        # self.assertIn("Спасибо за вступление в ряды буккроссеров!", driver.page_source)
        # if not result_text == u'Thank You for Joining BookCrossing!':
        #     raise NoSuchElementException('Аккаунт не создан!')

    def test_2_login(self):
        print(self.username)
        print(self.password)
        driver = self.driver
        driver.get('http://127.0.0.1:8000/api/')
        driver.maximize_window()
        time.sleep(1)

        log_main_btn = driver.find_element(By.ID, 'toComeInAccount').click()
        time.sleep(3)

        # login_inp = driver.find_element(By.XPATH, "//input[@id='username']")
        login_inp = driver.find_element(By.ID, 'nameuser')
        login_inp.clear()
        time.sleep(3)
        login_inp.send_keys(self.username)
        time.sleep(1)

        passw_inp = driver.find_element(By.ID, 'password')
        passw_inp.clear()
        passw_inp.send_keys(self.password)
        time.sleep(3)

        login_btn = driver.find_element(By.ID, 'enterInAccount1').click()
        time.sleep(3)

        get_url = driver.current_url
        self.assertEqual(get_url, 'http://127.0.0.1:8000/api/home/')
        # self.assertIn("Welcome", driver.page_source)


    # def test_3_notfound(self):
    #     driver = self.driver
    #     driver.get('https://www.bookcrossing.com/')
    #     driver.maximize_window()
    #
    #     search_main_btn = driver.find_element(By.CLASS_NAME, 'fa-search').click()
    #
    #     search_inp = driver.find_element(By.NAME, 'SearchText')
    #     search_inp.clear()
    #     search_inp.send_keys(search_text1)
    #     time.sleep(1)
    #     search_btn = driver.find_element(By.CLASS_NAME, 'btn-primary').click()
    #
    #     result_text = driver.find_element(By.ID, 'results').text
    #     self.assertIn("К сожалению, результат, соответствующий вводу, не найден.", driver.page_source)
    #     # if not result_text == u'К сожалению, результат, соответствующий вводу, не найден.':
    #     #     raise NoSuchElementException('Элемент не найден!')
    #
    # def test_4_found(self):
    #     driver = self.driver
    #     driver.get('https://www.bookcrossing.com/')
    #     driver.maximize_window()
    #
    #     search_main_btn = driver.find_element(By.CLASS_NAME, 'fa-search').click()
    #
    #     search_inp = driver.find_element(By.NAME, 'SearchText')
    #     search_inp.clear()
    #     search_inp.send_keys(search_text2)
    #
    #     search_btn = driver.find_element(By.CLASS_NAME, 'btn-primary').click()
    #     # driver.get("https://www.bookcrossing.com/search?q=" + search_text2)
    #     table_result = driver.find_element(By.XPATH, "//table[@class='searchresults']/tbody/tr")
    #     # res = search_text2 in table_result.text.lower()
    #     self.assertIn(search_text2, table_result.text.lower())


    def tearDown(self):
        self.driver.close()
        self.driver.quit()
