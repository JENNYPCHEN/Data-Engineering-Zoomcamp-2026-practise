variable "credentials" {
  description = "My Credentials"
  # Use forward slashes (or double-escape backslashes) so Terraform doesn't treat them as escape sequences.
  default     = "C:/Users/User/Documents/DONOTDELETE/data-zoom-camp-2026-db1c5ef1ff04.json"
}

variable "project" {
  description = "Project"
  default     = "data-zoom-camp-2026"
}

variable "region" {
  description = "Region"
  default     = "europe-west1"
}

variable "location" {
  description = "Project Location"
  default     = "EU"
}

variable "bq_dataset_name" {
  description = "My BigQuery Dataset Name"
  default     = "demo_dataset"
}

variable "gcs_bucket_name" {
  description = "My Storage Bucket Name"
  default     = "terraform-demo-terra-bucket"
}

variable "gcs_storage_class" {
  description = "Bucket Storage Class"
  default     = "STANDARD"
}