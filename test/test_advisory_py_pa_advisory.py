# coding: utf-8

"""
    VulnCheck API

    Version 3 of the VulnCheck API

    The version of the OpenAPI document: 3.0
    Contact: support@vulncheck.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from vulncheck_sdk.models.advisory_py_pa_advisory import AdvisoryPyPAAdvisory

class TestAdvisoryPyPAAdvisory(unittest.TestCase):
    """AdvisoryPyPAAdvisory unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AdvisoryPyPAAdvisory:
        """Test AdvisoryPyPAAdvisory
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AdvisoryPyPAAdvisory`
        """
        model = AdvisoryPyPAAdvisory()
        if include_optional:
            return AdvisoryPyPAAdvisory(
                advisory_id = '',
                affected = [
                    vulncheck_sdk.models.advisory_py_pa_advisory_affected_inner.advisory_PyPAAdvisory_affected_inner(
                        package = vulncheck_sdk.models.advisory_py_pa_advisory_affected_inner_package.advisory_PyPAAdvisory_affected_inner_package(
                            ecosystem = '', 
                            name = '', 
                            purl = '', ), 
                        ranges = [
                            vulncheck_sdk.models.advisory_py_pa_advisory_affected_inner_ranges_inner.advisory_PyPAAdvisory_affected_inner_ranges_inner(
                                events = [
                                    vulncheck_sdk.models.advisory_py_pa_advisory_affected_inner_ranges_inner_events_inner.advisory_PyPAAdvisory_affected_inner_ranges_inner_events_inner(
                                        fixed = '', 
                                        introduced = '', )
                                    ], 
                                ranges_type = '', )
                            ], 
                        versions = [
                            ''
                            ], )
                    ],
                aliases = [
                    ''
                    ],
                date_added = '',
                details = '',
                modified = '',
                published = '',
                references = [
                    vulncheck_sdk.models.advisory_py_pa_advisory_references_inner.advisory_PyPAAdvisory_references_inner(
                        refs_type = '', 
                        url = '', )
                    ],
                was_withdrawn = True,
                withdrawn = ''
            )
        else:
            return AdvisoryPyPAAdvisory(
        )
        """

    def testAdvisoryPyPAAdvisory(self):
        """Test AdvisoryPyPAAdvisory"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
