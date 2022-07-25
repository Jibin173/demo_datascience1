import mysql


class Dashboard:

  #WebElement
  DVR_onlineCount_xpath="/html/body/div/div/main/div[3]/div/div/div[1]/div/div/div[1]/div/div/div[1]/div/section/div[2]/div/div[2]/div/div[1]/table/tbody/tr/td[2]"
  DeviceAvailabiltyDailycomparisonbtn_xpath="/html/body/div/div/main/div[3]/div/div/div[1]/div/section/div/div[3]/ul/li[1]/a"
  DetailedReportbutton_xpath = "/html[1]/body[1]/div[1]/div[1]/main[1]/div[3]/div[1]/div[1]/div[1]/div[1]/section[1]/div[1]/div[3]/button[1]/div[1]/span[1]"




  def __init__(self, driver):
   self.driver = driver

  def getonline_count(self):
    self.driver.implicitly_wait(90)
    element=self.driver.find_element_by_xpath(self.DVR_onlineCount_xpath)
    print(element.is_displayed())
    count=element.text
    print("Online count of DVR from the dashboard is ",element.text)
    li=list(count)
    num=li[0]+li[1]
    lis=list(num)
    actual=int(num)
    return actual

  def databaseconnection(self):
    connection = mysql.connector.connect(host='164.52.223.139',
                                         database='terrier_1',
                                         user='admin',
                                         password='carinov@123')
    print("We are connected to the database")
    mycursor = connection.cursor()
    mycursor.execute(
      "select count(status)from(select server_name ,server_status as status from recording_server rs where is_disabled = 0) as a group by status")
    myresult = mycursor.fetchall()
    print("Value availabe in database is",myresult[0][0])
    expect=myresult[0][0]
    return expect
