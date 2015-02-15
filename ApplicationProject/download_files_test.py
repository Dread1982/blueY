import unittest
import download_files as df
from mock import Mock, patch, mock_open, call


class DownloadFilesTest(unittest.TestCase):

    def setUp(self):
        self.source_file_name = "testSource.txt"
        self.download_folder = "images"

        self.filename1 = "image1.jpg"
        self.filename2 = "image2.jpg"
        self.filename3 = "image3.jpg"
        self.url1 = "http://testserver.com/"+self.filename1
        self.url2 = "http://testserver.com/"+self.filename2
        self.url3 = "http://testserver.com/"+self.filename3

        self.source_file_data = '\n'.join([self.url1, self.url2, self.url3])

        self.response_content_1 = "responseContent1"
        self.response_content_2 = "responseContent2"
        self.response_content_3 = 'responseContent3'

        self.downloaded_filename1 = self.download_folder + "\\" + self.filename1
        self.downloaded_filename2 = self.download_folder + "\\" + self.filename2
        self.downloaded_filename3 = self.download_folder + "\\" + self.filename3

        # create and setup mocks
        self.mock_file_open = mock_open()
        self.mock_os = Mock()
        self.mock_request = Mock()
        self.mock_response1 = Mock()
        self.mock_response2 = Mock()
        self.mock_response3 = Mock()

        self.mock_file_open.return_value.__iter__.return_value = self.source_file_data.splitlines()

        self.mock_response1.content = self.response_content_1
        self.mock_response1.status_code = 200
        self.mock_response2.content = self.response_content_2
        self.mock_response2.status_code = 200
        self.mock_response3.content = self.response_content_3
        self.mock_response3.status_code = 200

    def test_get_filename(self):
        self.assertEqual(self.downloaded_filename1, df.get_filename(self.url1, self.download_folder))

    def test_save_file_to_disc(self):
        with patch("__builtin__.open", self.mock_file_open):
            df.save_file_to_disc(self.response_content_1, self.filename1)

        self.mock_file_open.assert_called_once_with(self.filename1, "wb")
        self.mock_file_open().write.assert_calledn_once_with(self.response_content_1)

    def test_create_download_folder_new(self):
        self.mock_os.path.exists.return_value = False

        with patch("download_files.os", self.mock_os):
            df.create_download_folder("images")

        self.mock_os.path.exists.assert_called_once_with("images")
        self.mock_os.makedirs.assert_called_once_with("images")

    def test_create_download_folder_exists(self):
        self.mock_os.path.exists.return_value = True

        with patch("download_files.os", self.mock_os):
            df.create_download_folder("images")

        self.mock_os.path.exists.assert_called_once_with("images")
        self.assertEquals(0, self.mock_os.makedirs.get.call_count)

    def test_download_file(self):
        self.mock_request.get.return_value = self.mock_response1

        with patch("download_files.os", self.mock_os):
            with patch("__builtin__.open", self.mock_file_open):
                with patch("download_files.requests", self.mock_request):
                    df.download_file(self.url1, self.download_folder)

        self.mock_request.get.assert_called_once_with(self.url1)
        self.mock_file_open.assert_called_once_with(self.downloaded_filename1, "wb")
        self.mock_file_open().write.assert_calledn_once_with(self.response_content_1)

    def test_download_file_bad_response(self):
        self.mock_response1.status_code = 404
        self.mock_request.get.return_value = self.mock_response1

        with patch("download_files.os", self.mock_os):
            with patch("__builtin__.open", self.mock_file_open):
                with patch("download_files.requests", self.mock_request):
                    df.download_file(self.url1, self.download_folder)

        self.mock_request.get.assert_called_once_with(self.url1)
        self.assertEquals(0, self.mock_file_open.call_count)
        self.assertEquals(0, self.mock_file_open().write.call_count)

    def test_download_files(self):
        return_values = [self.mock_response1, self.mock_response2, self.mock_response3]
        self.mock_request.get.side_effect = lambda x: return_values[self.mock_request.get.call_count - 1]

        with patch("download_files.os", self.mock_os):
            with patch("__builtin__.open", self.mock_file_open):
                with patch("download_files.requests", self.mock_request):
                    df.download_files(self.source_file_name, self.download_folder)

        open_file_calls = [call(self.source_file_name, "r"), call(self.downloaded_filename1, "wb"),
                           call(self.downloaded_filename2, "wb"), call(self.downloaded_filename3, "wb")]
        self.mock_file_open.assert_has_calls(open_file_calls, any_order=True)

        req_get_calls = [call(self.url1), call(self.url2), call(self.url3)]
        self.mock_request.get.assert_has_calls(req_get_calls, any_order=True)

        write_calls = [call(self.response_content_1), call(self.response_content_2), call(self.response_content_3)]
        self.mock_file_open().write.assert_has_calls(write_calls, any_order=True)

if __name__ == "__main__":
    unittest.main()