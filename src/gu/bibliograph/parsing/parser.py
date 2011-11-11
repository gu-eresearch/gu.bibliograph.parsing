from bibliograph.parsing.parsers.bibtex import BibtexParser
from bibliograph.parsing.parsers.endnote import EndNoteParser
from bibliograph.parsing.parsers.medline import MedlineParser
from bibliograph.parsing.parsers.ris import RISParser
from bibliograph.parsing.parsers.xml import XMLParser


def fixupresult(result):
    if 'keywords' in result:
        result['subject'] = result['keywords']
        #del result['keywords']
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
