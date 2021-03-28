from selenium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException


lst = []
nums = []


def mainfunc(usr,pwd,ek,do,teen,chaar):
	my_dict = {
		'IHS223' : 'IHS 223 - Business Communication Skills',
		'ihs223' : '211',
		'IHS222' :'IHS 222-Principles of Management',
		'ihs222' : '212',
		'IHS221' : 'IHS 221-Fundamentals of Economics',
		'ihs221' : '213',
		'IMA221' : 'IMA221-Probability ,Statistics and Random Process',
		'ima221' : '214',
		'ICS224' : 'ICS 224-Computer Networks',
		'ics224' : '215',
		'ICS223' : 'ICS 223-Complier Design',
		'ics223' : '216',
		'ICS222' : 'ICS 222- Object-Oriented Analysis and Design',
		'ics222' : '217',
		'ICS221' : 'ICS 221-Theory of Computation',
		'ics221' : '218'
	           }
	lst.append(my_dict.get(str(ek)))
	lst.append(my_dict.get(str(do)))
	lst.append(my_dict.get(str(teen)))
	lst.append(my_dict.get(str(chaar)))
	nums.append(my_dict.get(str(ek).lower()))
	nums.append(my_dict.get(str(do).lower()))
	nums.append(my_dict.get(str(teen).lower()))
	nums.append(my_dict.get(str(chaar).lower()))
	u=usr
	p=pwd
	url='https://lmsone.iiitkottayam.ac.in/course/index.php?categoryid=9'
	# executable_path=r"C:\Users\LENOVO\PycharmProjects\FirstseleniumTest\drivers\chromedriver.exe"
	driver=webdriver.Chrome()
	driver.get(url)
	for i in range(0,4):
		driver.find_element_by_link_text(""+str(lst[i])+"").click()
		if i==0:
			usrnm=driver.find_element_by_xpath('//*[@id="username"]')
			usrnm.send_keys(''+str(u)+'')
			pswd=driver.find_element_by_xpath('//*[@id="password"]')
			pswd.send_keys(''+str(p)+'')
			driver.find_element_by_xpath('//*[@id="loginbtn"]').click()
			try:
				if driver.find_element_by_link_text('Invalid login, please try again'):
					return 1
			except NoSuchElementException :
				pass

		time.sleep(15)
		driver.maximize_window()
		driver.find_element_by_xpath('//*[@id="module-'+str(nums[i])+'"]/div/div/div[2]/div[1]/a/span').click()
		driver.find_element_by_xpath('//*[@id="join_button_input"]').click()
		chwd = driver.window_handles
		p = driver.current_window_handle
		for w in chwd:
			if(w!=p):
				driver.switch_to.window(w)
		time.sleep(15)
		driver.find_element_by_xpath('/html/body/div[4]/div/div/div[1]/div/div/span/button[2]').click()
		'''
		driver.find_element_by_xpath('//*[@id="message-input"]').send_keys('Good morning')
		time.sleep(7)
		driver.find_element_by_xpath('//*[@id="tippy-40"]/span[1]/i').click()
		'''
		time.sleep(15)
		driver.close()
		driver.switch_to.window(p)
		driver.get(url)