from osbot_fast_api_serverless.deploy.Deploy__Serverless__Fast_API      import Deploy__Serverless__Fast_API
from issues_fs_service.config                                           import LAMBDA_DEPENDENCIES__ISSUES_FS_SERVICE, SERVICE_NAME
from issues_fs_service.fast_api.lambda_handler                          import run


class Deploy__Service(Deploy__Serverless__Fast_API):

    def handler(self):
        return run

    def lambda_dependencies(self):
        return LAMBDA_DEPENDENCIES__ISSUES_FS_SERVICE

    def lambda_name(self):
        return SERVICE_NAME
