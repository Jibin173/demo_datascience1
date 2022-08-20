import configparser


config=configparser.RawConfigParser()
config.read("E:\\demo_datascience\\Configuration\\config.ini")

class ReadConfig:
    @staticmethod
    def getApplicationURL():
        url=config.get('common info','baseURL')
        return url

    @staticmethod
    def getUseremail():
        username=config.get('common info','useremail')
        return username

    @staticmethod
    def getPassword():
        password=config.get('common info','password')
        return password

    @staticmethod
    def getairflow():
        airflow=config.get('common info','airflowURL')
        return airflow

    @staticmethod
    def versionairflow():
        version1=config.get('common info','version')
        return version1

    @staticmethod
    def getgrafanaurl():
        airflow=config.get('common info','fan')
        return airflow

    @staticmethod
    def getgrafanaurlevent():
        airflow=config.get('common info','fanaevent')
        return airflow