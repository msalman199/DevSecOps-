output "security_hub_arn" {
  description = "ARN of the Security Hub account"
  value       = aws_securityhub_account.main.arn
}

output "guardduty_detector_id" {
  description = "ID of the GuardDuty detector"
  value       = aws_guardduty_detector.main.id
}

output "config_recorder_name" {
  description = "Name of the Config recorder"
  value       = aws_config_configuration_recorder.main.name
}

output "codecommit_repository_url" {
  description = "URL of the CodeCommit repository"
  value       = aws_codecommit_repository.main.clone_url_http
}

output "config_s3_bucket" {
  description = "S3 bucket for Config"
  value       = aws_s3_bucket.config.bucket
}
