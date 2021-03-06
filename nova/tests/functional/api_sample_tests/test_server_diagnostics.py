# Copyright 2012 Nebula, Inc.
# Copyright 2013 IBM Corp.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from nova.tests.functional.api_sample_tests import test_servers


class ServerDiagnosticsSamplesJsonTest(test_servers.ServersSampleBase):
    # The 'os_compute_api:os-server-diagnostics' policy is admin-only
    ADMIN_API = True
    sample_dir = "os-server-diagnostics"

    def test_server_diagnostics_get(self):
        uuid = self._post_server()
        response = self._do_get('servers/%s/diagnostics' % uuid)
        self._verify_response('server-diagnostics-get-resp', {},
                              response, 200)


class ServerDiagnosticsSamplesJsonTestV248(ServerDiagnosticsSamplesJsonTest):
    microversion = '2.48'
    scenarios = [('v2_48', {'api_major_version': 'v2.1'})]
