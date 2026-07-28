from checkov.common.models.enums import TRUE_VALUES
from checkov.terraform.checks.resource.base_resource_check import BaseResourceCheck
from checkov.common.models.enums import ANY_VALUE


class S3BucketMustHaveTagging(BaseResourceCheck):
    def __init__(self):
        name = "Ensure S3 bucket has required tags"
        id = "CKV2_CUSTOM_1"
        supported_resources = ['aws_s3_bucket']
        categories = []
        super().__init__(name=name, id=id, categories=categories, supported_resources=supported_resources)

    def scan_resource_conf(self, conf):
        """
        Looks for required tags on S3 buckets
        """
        if 'tags' in conf:
            tags = conf['tags'][0]
            required_tags = ['Name', 'Environment']
            
            for required_tag in required_tags:
                if required_tag not in tags:
                    return CheckResult.FAILED
            return CheckResult.PASSED
        return CheckResult.FAILED


check = S3BucketMustHaveTagging()
