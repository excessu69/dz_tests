import requests



class TestYandexDisk:
    def setup_method(self):
        self.headers = {'Authorization': 'y0_AgAAAAAWIRKDAADLWwAAAAD8wy66AADauAWslSRDBYF4NXVmVz5cIf2Mog'}

    def test_creat_folder(self):
        params = {'path': 'Image111'}
        response = requests.put('https://cloud-api.yandex.net/v1/disk/resources',
                                headers=self.headers,
                                params=params
                                )

        assert response.status_code == 201

    def test_creat_folder_1(self):
        params = {'path': 'Image111'}
        response = requests.put('https://cloud-api.yandex.net/v1/disk/resources',
                                headers=self.headers,
                                params=params
                                )

        assert response.status_code == 409

    def test_creat_folder_2(self):
        params = {'path': ''}
        response = requests.put('https://cloud-api.yandex.net/v1/disk/resources',
                                headers=self.headers,
                                params=params
                                )

        assert response.status_code == 400


    def test_creat_folder_3(self):
        params = {'path': 'Image1111'}
        response = requests.put('https://cloud-api.yandex.net/v1/disk',
                                headers=self.headers,
                                params=params
                                )

        assert response.status_code == 405

    def test_creat_folder_6(self):
        self.headers = {'Authorization': 'ahbrgfhwaby23gbiwbfgewr'}
        params = {'path': 'Image1111'}
        response = requests.put('https://cloud-api.yandex.net/v1/disk/resources',
                                headers=self.headers,
                                params=params
                                )

        assert response.status_code == 401

