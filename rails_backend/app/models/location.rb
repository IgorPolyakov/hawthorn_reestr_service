# frozen_string_literal: true

class Location
  include Mongoid::Document
  include Mongoid::Timestamps

  field :cadastr_id, type: Integer # optional
  field :region, type: String
  field :district, type: String # optional
  field :populated_area, type: String # optional
  field :street, type: String
  field :street_name, type: String
  field :house_number, type: String
  field :apartment, type: String
  field :zip_url, type: String
  field :status, type: String, default: 'в обработке'
  field :search_ui, type: Integer

  embedded_in :search_query
  validates :region, :street, :street_name, :house_number, :apartment, :zip_url, :status, :search_ui, presence: true
end

# required date_request: yyyy-dd-MMThh:mm:ss (or some like this)
# required date_response: yyyy-dd-MMThh:mm:ss (or some like this)
