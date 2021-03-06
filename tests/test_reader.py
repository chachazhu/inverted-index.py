import os
import unittest
from inverted_index.utils import manipulate
from inverted_index.utils.io import IO


class TestIO(unittest.TestCase):
    """Test reader module."""

    def test_get_docs(self):
        r = IO()
        r.dir = os.path.dirname(os.path.realpath(__file__)) + '/test_docs/'
        docs, num_docs = r._get_docs()
        self.assertIsInstance(docs, list)
        self.assertIsInstance(num_docs, int)

    def test_read_manipulate(self):
        r = IO()
        r.dir = os.path.dirname(os.path.realpath(__file__)) + '/test_docs/'
        file_path = r.dir + '1.txt'
        self.assertIsInstance(r._read_manipulate(file_path), list)

    def test_make_runs(self):
        r = IO()
        r.dir = os.path.dirname(os.path.realpath(__file__)) + '/test_docs/'
        docs, num_docs = r._get_docs()
        runs = r._make_runs(docs, num_docs)
        self.assertIsInstance(runs, list)

    def test_run_to_temp(self):
        r = IO()
        r.dir = os.path.dirname(os.path.realpath(__file__)) + '/test_docs/'
        docs, num_docs = r._get_docs()
        run = r._make_runs(docs, num_docs)[0]
        r.run_to_temp(run)

    def test_merge_runs(self):
        r = IO()
        r.dir = os.path.dirname(os.path.realpath(__file__)) + '/test_docs/'
        docs, num_docs = r._get_docs()
        runs = r._make_runs(docs, num_docs)
        # make runs to temp
        [r.run_to_temp(run) for run in runs]
        r.merge_runs()

