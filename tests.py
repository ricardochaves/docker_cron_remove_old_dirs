"""
    All tests
"""
import os

import unittest
from unittest.mock import patch
from unittest.mock import MagicMock
from unittest.mock import call

from pyfakefs.fake_filesystem_unittest import TestCase

from script import execute
from script import remove_path
from script import is_dir
from script import is_old
from script import work_with_watch
from script import loop_root

class TestScript(TestCase):
    """
        Tests script.py
    """

    def setUp(self):
        self.setUpPyfakefs()

    @staticmethod
    @patch('script.loop_root')
    def test_execute(mock_loop_root):
        """
            Unit: Script: Test execute()
        """
        execute()

        mock_loop_root.assert_called_once_with()

    @staticmethod
    #@patch('logging.info')
    @patch('script.shutil.rmtree')
    @patch('script.arrow.get')
    def test_remove_path(mock_arrow_get, mock_removetree):
        """
            Unit: Script: Test remove_path()
        """

        entry = MagicMock()
        remove_path(entry)

        mock_arrow_get.assert_called_once_with(entry.stat().st_mtime)
        mock_removetree.assert_called_once_with(entry.path)
        #mock_log.assert_called_once()

    def test_is_dir(self):
        """
            Unit: Script: Test is_dir()
        """
        entry = MagicMock()
        entry.name.startswith.return_value = False
        entry.is_dir.return_value = True

        result = is_dir(entry)

        entry.name.startswith.assert_called_once_with('.')
        entry.is_dir.assert_called_once_with()
        self.assertTrue(result)

    @patch.dict(os.environ, {'TIME_TO_REMOVE_SECONDS': '1'})
    @patch('script.arrow.get')
    @patch('script.arrow.now')
    def test_is_old(self, mock_arrow_now, mock_arrow_get):
        """
            Unit: Script: Test is_old()
        """
        shi = MagicMock()
        shi.shift = MagicMock(return_value=2)

        mock_arrow_now.return_value = shi
        mock_arrow_get.return_value = 1

        entry = MagicMock()
        result = is_old(entry)

        self.assertTrue(result)
        shi.shift.assert_called_once_with(seconds=-1)
        mock_arrow_now.assert_called_once_with()
        mock_arrow_get.assert_called_once_with(entry.stat().st_mtime)


    @patch('script.remove_path')
    @patch('script.is_old')
    @patch('script.is_dir')
    @patch('script.os.scandir')
    def test_work_with_watch(self, mock_scan, mock_is_dir, mock_is_old, mock_remove_path):
        """
            Unit: Script: Test work_with_watch()
        """
        dir1 = MagicMock()
        dir2 = MagicMock()
        dirs = MagicMock()
        dirs.__enter__ = MagicMock(return_value=[dir1, dir2])
        mock_scan.return_value = dirs

        mock_is_dir.return_value = True
        mock_is_old.return_value = True

        work_with_watch('path')

        mock_scan.assert_called_once_with('path')

        expected_calls = [call(dir1), call(dir2)]
        self.assertTrue(mock_is_dir.call_args_list == expected_calls)
        self.assertTrue(mock_is_old.call_args_list == expected_calls)

        expected_calls = [call(dir1.path), call(dir2.path)]
        self.assertTrue(mock_remove_path.call_args_list == expected_calls)

    @patch('script.work_with_watch')
    @patch('script.os.scandir')
    def test_loop_root(self, mock_scan, mock_work):
        """
            Unit: Script: Test loop_root()
        """
        dir1 = MagicMock()
        dir2 = MagicMock()
        dirs = MagicMock()
        dirs.__enter__ = MagicMock(return_value=[dir1, dir2])
        mock_scan.return_value = dirs

        loop_root()

        expected_calls = [call(dir1.path), call(dir2.path)]
        self.assertTrue(mock_work.call_args_list == expected_calls)

if __name__ == '__main__':
    unittest.main()
