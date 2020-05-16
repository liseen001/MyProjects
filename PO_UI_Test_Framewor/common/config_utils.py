import os
import configparser

current_dir = os.path.abspath(os.path.dirname(__file__))
config_path = os.path.join(current_dir, "..", 'conf',"config.ini")

class ConfigUtils(object):
    def __init__(self,path=config_path):
        self.cfg = configparser.ConfigParser()
        self.cfg.read(path)

    @property
    def url(self):
        url_value = self.cfg.get('default','url')
        return url_value

    @property
    def driver_path(self):
        driver_path_value = self.cfg.get('default','driver_path')
        return driver_path_value

    @property
    def driver_name(self):
        driver_name_value = self.cfg.get('default', 'driver_name')
        return driver_name_value

    @property
    def time_out(self):
        driver_name_value = float(self.cfg.get('default', 'time_out'))
        return driver_name_value

    @property
    def element_info_path(self):
        element_info_path_value = self.cfg.get('default', 'element_info_path')
        return element_info_path_value

    @property
    def screenshot_path(self):
        screenshot_path_value = self.cfg.get('default', 'screen_shot_path')
        return screenshot_path_value

    @property
    def log_path(self):
        log_path_value = self.cfg.get('default', 'log_path')
        return log_path_value

    @property
    def testdata_path(self):
        testdata_path_value = self.cfg.get('default', 'testdata_path')
        return testdata_path_value

    @property
    def case_path(self):
        case_path_value = self.cfg.get('default', 'case_path')
        return case_path_value

    @property
    def report_path(self):
        report_path_value = self.cfg.get('default', 'report_path')
        return report_path_value

    @property
    def log_level(self):
        log_level_value = int(self.cfg.get('default', 'log_level'))
        return log_level_value

    @property
    def user_name(self):
        user_name_value = self.cfg.get('default', 'user_name')
        return user_name_value

    @property
    def password(self):
        password_value = self.cfg.get('default', 'password')
        return password_value

    @property
    def smtp_server(self):
        smtp_server_value = self.cfg.get('email', 'smtp_server')
        return smtp_server_value

    @property
    def smtp_sender(self):
        smtp_sender_value = self.cfg.get('email', 'smtp_sender')
        return smtp_sender_value

    @property
    def smtp_password(self):
        smtp_password_value = self.cfg.get('email', 'smtp_password')
        return smtp_password_value

    @property
    def smtp_receiver(self):
        smtp_receiver_value = self.cfg.get('email', 'smtp_receiver')
        return smtp_receiver_value

    @property
    def smtp_cc(self):
        smtp_cc_value = self.cfg.get('email', 'smtp_cc')
        return smtp_cc_value

    @property
    def smtp_subject(self):
        smtp_subject_value = self.cfg.get('email', 'smtp_subject')
        return smtp_subject_value



local_config = ConfigUtils()

if __name__=='__main__':
    config = ConfigUtils()
    print(type(local_config.time_out),local_config.time_out)
    print( config.report_path )