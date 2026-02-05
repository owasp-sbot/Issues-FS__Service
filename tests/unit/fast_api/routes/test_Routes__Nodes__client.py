from unittest                                                                                import TestCase
from osbot_fast_api_serverless.utils.Version                                                 import version__osbot_fast_api_serverless
from osbot_utils.testing.Graph__Deterministic__Ids                                           import graph_deterministic_ids
from osbot_utils.testing.__                                                                  import __, __SKIP__
from issues_fs.schemas.graph.Schema__Node__Create__Request  import Schema__Node__Create__Request
from issues_fs.schemas.graph.Schema__Node__Create__Response import Schema__Node__Create__Response
from tests.unit.Issues_FS__Service__Test_Objs                                                 import setup__issues_fs_service__test_objs


class test_Routes__Nodes__client(TestCase):

    @classmethod
    def setUpClass(cls):                                                         # Shared setup - create once
        cls.test_objs  = setup__issues_fs_service__test_objs()
        cls.client = cls.test_objs.fast_api__client


    def test__info__health(self):
        response = self.client.get('/info/status')
        assert response.status_code                   == 200
        assert response.json()                        == { 'environment': 'local'                            ,
                                                           'name'       : 'osbot_fast_api_serverless'        ,
                                                           'status'     : 'operational'                      ,
                                                           'version'    : version__osbot_fast_api_serverless }
        assert self.client.get('/info/health').json() == {'status': 'ok'}