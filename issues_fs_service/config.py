from issues_fs_service import package_name

SERVICE_NAME                            = package_name
FAST_API__TITLE                         = "Issues-FS Service"
FAST_API__DESCRIPTION                   = "Issues-FS Service - FastAPI server with REST endpoints"
LAMBDA_DEPENDENCIES__ISSUES_FS_SERVICE  = ['memory-fs==v0.41.0'                     ,
                                            'osbot-fast-api-serverless==v1.34.0'     ]
