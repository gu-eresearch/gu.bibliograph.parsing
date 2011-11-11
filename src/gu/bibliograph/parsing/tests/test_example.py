import unittest2 as unittest
from zope.component import getUtilitiesFor, getUtility
from bibliograph.parsing.interfaces import IBibliographyParser
from gu.bibliograph.parsing import parser

from gu.bibliograph.parsing.testing import\
    GU_BIBLIOGRAPH_PARSING_INTEGRATION_TESTING

PARSERS = {'bibtex': parser.WrappedBibtexParser,
           'endnote': parser.WrappedEndNoteParser,
           'medline': parser.WrappedMedlineParser,
           'ris': parser.WrappedRISParser,
           'xml': parser.WrappedXMLParser}


BIBDATA = '''
@book{author:11,
author = "First Author and Second Author",
title  = "A bibtex entry for testing",
year = 2011,
keywords = "testing, bibtex, plone",
}
'''


class TestUtilities(unittest.TestCase):

    layer = GU_BIBLIOGRAPH_PARSING_INTEGRATION_TESTING

    def setUp(self):
        # you'll want to use this to set up anything you need for your tests
        # below
        pass

    def test_registration(self):
        regs = getUtilitiesFor(IBibliographyParser)
        for (name, parser) in regs:
            self.assertTrue(name in PARSERS)
            self.assertTrue(isinstance(parser, PARSERS[name]))

    def test_parser(self):
        parser = getUtility(IBibliographyParser, name='bibtex')
        entries = parser.getEntries(BIBDATA)
        self.assertEqual(len(entries), 1)
        self.assertTrue('keywords' in entries[0])
        self.assertTrue('subject' in entries[0])
        self.assertEqual(entries[0]['keywords'], entries[0]['subject'])
