# 📦 Terraform - WhatsApp Analyzer Infra

This folder contains Terraform code to create a GCS bucket for storing WhatsApp parsed data.

Do not forget to setup your GCP credentials with gcloud auth.

## ⚙️ Usage

```bash
cd terraform/
cp terraform.tfvars.example terraform.tfvars
# Edit terraform.tfvars with your GCP project_id, region and bucket_name

terraform init
terraform plan -var-file="terraform.tfvars"
terraform apply -var-file="terraform.tfvars"