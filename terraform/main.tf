resource "google_storage_bucket" "whatsapp_bucket" {
  name          = var.bucket_name
  location      = var.region
  force_destroy = true

  uniform_bucket_level_access = true

  lifecycle_rule { # clean in one year
    action {
      type = "Delete"
    }
    condition {
      age = 365
    }
  }
}
