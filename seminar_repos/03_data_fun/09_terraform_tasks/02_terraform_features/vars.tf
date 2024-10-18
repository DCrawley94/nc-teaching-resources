variable "colleagues" {
  type    = list(string)
  default = ["colleague_1", "colleague_2", "colleague_3"]
}

variable "db_username" {
  description = "Database administrator username"
  type        = string
  sensitive   = true
}

variable "db_password" {
  description = "Database administrator password"
  type        = string
  sensitive   = true
}
