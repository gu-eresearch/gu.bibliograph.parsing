from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.app.testing import IntegrationTesting
from plone.app.testing import FunctionalTesting
from plone.app.testing import applyProfile

from zope.configuration import xmlconfig


class GuBibliographParsing(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE, )

    def setUpZope(self, app, configurationContext):
        # Load ZCML for this package
        import gu.bibliograph.parsing
        self.loadZCML(package=gu.bibliograph.parsing)
        self.loadZCML('overrides.zcml', package=gu.bibliograph.parsing)
        # p self.products

    def setUpPloneSite(self, portal):
        pass

GU_BIBLIOGRAPH_PARSING_FIXTURE = GuBibliographParsing()
GU_BIBLIOGRAPH_PARSING_INTEGRATION_TESTING = \
    IntegrationTesting(bases=(GU_BIBLIOGRAPH_PARSING_FIXTURE, ),
                       name="GuBibliographParsing:Integration")
