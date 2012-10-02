from bibliograph.parsing.parsers.bibtex import BibtexParser
from bibliograph.parsing.parsers.endnote import EndNoteParser
from bibliograph.parsing.parsers.medline import MedlineParser
from bibliograph.parsing.parsers.ris import RISParser
from bibliograph.parsing.parsers.xml import XMLParser


def fixupresult(result):
    # 1. move extracted keywords to plone subject
    if 'keywords' in result:
        result['subject'] = result['keywords']
        #del result['keywords']
    # 2. if url is a pubmed url extract pubmedid and store it
    if 'url' in result:
        try:
            pre, pmid = result['url'].rsplit('/', 1)
            if pre == 'http://www.ncbi.nlm.nih.gov/pubmed':
                if not 'identifiers' in result:
                    result['identifiers'] = []
                result['identifiers'].append({'label': 'PMID',
                                              'value': pmid})
        except ValuError:
            # not enough values to unpack in rsplit
            pass
    return result


class WrappedBibtexParser(BibtexParser):

    def parseEntry(self, entry):
        return fixupresult(BibtexParser.parseEntry(self, entry))


class WrappedEndNoteParser(EndNoteParser):

    def parseEntry(self, entry):
        return fixupresult(EndNoteParser.parseEntry(self, entry))


class WrappedMedlineParser(MedlineParser):

    def parseEntry(self, entry):
        return fixupresult(MedlineParser.parseEntry(self, entry))


class WrappedRISParser(RISParser):

    def parseEntry(self, entry):
        return fixupresult(RISParser.parseEntry(self, entry))


class WrappedXMLParser(XMLParser):

    def parseEntry(self, entry):
        return fixupresult(XMLParser.parseEntry(self, entry))
