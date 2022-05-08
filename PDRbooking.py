from selenium import webdriver
from selenium.webdriver.support.select import Select
from time import sleep
from selenium.common.exceptions import NoSuchElementException
from datetime import date, timedelta

from Bookingdetails import cdpath, username, password, domain, date_mode, starttime, endtime, venue, booking_purpose, no_of_users


class PDRbookingBot():
    def login(self):
        self.driver = webdriver.Chrome(cdpath)
        self.driver.get('https://venus.wis.ntu.edu.sg/PortalServices/ServiceListModule/LaunchService.aspx?type=1&launchSvc=https%3A%2F%2Fsso%2Ewis%2Entu%2Eedu%2Esg%2Fwebexe88%2Fowa%2Fsso%5Fredirect%2Easp%3Ft%3D1%26app%3Dhttps%3A%2F%2Fwis%2Entu%2Eedu%2Esg%2Fpls%2Fwebexe88%2Ffb%5Fstudent%2Emain%5Fall')

        sleep(2)

        # Enter username & select domain
        username_field = self.driver.find_element_by_xpath('/html/body/div/div/div[2]/table/tbody/tr/td/form/center[1]/table/tbody/tr/td/table/tbody/tr[2]/td[2]/input')
        username_field.send_keys(username)

        def domain_id(domain):
            if domain == 'STAFF':
                self.driver.find_element_by_xpath('/html/body/div/div/div[2]/table/tbody/tr/td/form/center[1]/table/tbody/tr/td/table/tbody/tr[3]/td[2]/select/option[1]').click()
            elif domain == 'STUDENT':
                self.driver.find_element_by_xpath('/html/body/div/div/div[2]/table/tbody/tr/td/form/center[1]/table/tbody/tr/td/table/tbody/tr[3]/td[2]/select/option[2]').click()
            elif domain == 'ASSOC':
                self.driver.find_element_by_xpath('/html/body/div/div/div[2]/table/tbody/tr/td/form/center[1]/table/tbody/tr/td/table/tbody/tr[3]/td[2]/select/option[3]').click()
            elif domain == 'NIESTUDENT':
                self.driver.find_element_by_xpath('/html/body/div/div/div[2]/table/tbody/tr/td/form/center[1]/table/tbody/tr/td/table/tbody/tr[3]/td[2]/select/option[4]').click()
            elif domain == 'NIESTAFF':
                self.driver.find_element_by_xpath('/html/body/div/div/div[2]/table/tbody/tr/td/form/center[1]/table/tbody/tr/td/table/tbody/tr[3]/td[2]/select/option[5]').click()
            else:
                self.driver.find_element_by_xpath('/html/body/div/div/div[2]/table/tbody/tr/td/form/center[1]/table/tbody/tr/td/table/tbody/tr[3]/td[2]/select/option[2]').click()

        domain_id(domain)

        ok_btn = self.driver.find_element_by_xpath('/html/body/div/div/div[2]/table/tbody/tr/td/form/center[1]/table/tbody/tr/td/table/tbody/tr[4]/td/input[1]')
        ok_btn.click()

        # Enter password
        password_field = self.driver.find_element_by_xpath('/html/body/div/div/div[2]/table/tbody/tr/td/form/center[1]/table/tbody/tr/td/table/tbody/tr[3]/td[2]/input')
        password_field.send_keys(password)

        login_btn = self.driver.find_element_by_xpath('/html/body/div/div/div[2]/table/tbody/tr/td/form/center[1]/table/tbody/tr/td/table/tbody/tr[5]/td/input[1]')
        login_btn.click()

    def booking(self):
        self.driver.switch_to.frame('left_fr')

        # Enter start date & end date
        startdate_field = self.driver.find_element_by_xpath('/html/body/form[1]/table[1]/tbody/tr[2]/td/input')
        startdate_field.clear()

        enddate_field = self.driver.find_element_by_xpath('/html/body/form[1]/table[1]/tbody/tr[4]/td/input')
        enddate_field.clear()

        if date_mode == 'auto':
            auto_date = (date.today() + timedelta(days = 2)).strftime('%d-%b-%Y').upper()
            startdate_field.send_keys(auto_date)
            enddate_field.send_keys(auto_date)
        elif date_mode == 'manual':
            return None

        # Enter start & end time
        starttime_option = Select(self.driver.find_element_by_xpath('/html/body/form[1]/table[1]/tbody/tr[7]/td/select'))
        starttime_option.select_by_visible_text(starttime)

        endtime_option = Select(self.driver.find_element_by_xpath('/html/body/form[1]/table[1]/tbody/tr[8]/td/select'))
        endtime_option.select_by_visible_text(endtime)

        booking_btn = self.driver.find_element_by_xpath('/html/body/form[1]/table[2]/tbody/tr[1]/td/input')
        booking_btn.click()

        # Select venue
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame('right_fr')
        sleep(2)
        try:
            venue_option = Select(self.driver.find_element_by_xpath('//*[@id="xyz"]/table/tbody/tr[2]/td/select'))
            venue_option.select_by_visible_text("LHN-PDR+" + venue)
        except NoSuchElementException:
            print('\033[91m' + 'ERROR: LHN-PDR+' + venue + ' has already been booked by other users.' + '\033[0;0m')
            self.driver.quit()
            exit()


        # Select booking type, purpose and number of users
        booking_type_option = self.driver.find_element_by_xpath('//*[@id="xyz"]/table/tbody/tr[8]/td[2]/select/option[2]')
        booking_type_option.click()

        booking_purpose_field = self.driver.find_element_by_xpath('//*[@id="xyz"]/table/tbody/tr[9]/td[2]/input')
        booking_purpose_field.send_keys(booking_purpose)

        no_of_users_field = self.driver.find_element_by_xpath('//*[@id="xyz"]/table/tbody/tr[10]/td[2]/input')
        no_of_users_field.send_keys(no_of_users)

        booknow_btn = self.driver.find_element_by_xpath('//*[@id="xyz"]/input[10]')
        booknow_btn.click()

        sleep(2)
        success_header = self.driver.find_element_by_xpath('/html/body/font').text()
        success_message = self.driver.find_element_by_xpath('/html/body/font/b/em').text()
        print ('\33[4m\33[1m\33[32m' + success_header + '\033[0;0m')
        print('\33[4m\33[1m\33[32m' + success_message + '\033[0;0m')

        self.driver.quit()

# Executing class & functions
bot = PDRbookingBot()
bot.login()
sleep(2)
bot.booking()