import pytest

@pytest.mark.usefixtures("init_driver")
class services:
    def get_title(self):
        print("deepak")



if __name__=="__main__":
    obj=services()
    obj.get_title()