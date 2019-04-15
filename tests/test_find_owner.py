from time import sleep

import pytest


class TestFindOwnerSet():

    @pytest.mark.possitive
    def test_find_owner(self, pm):
        pm.home_page.open()
        sleep(5)
