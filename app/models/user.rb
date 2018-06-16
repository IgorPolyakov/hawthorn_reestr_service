class User
  include Mongoid::Document
  include ActiveModel::SecurePassword
  field :email, type: String
  has_secure_password
  field :password_digest, type: String

end
