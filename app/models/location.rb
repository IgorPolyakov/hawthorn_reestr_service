# frozen_string_literal: true

class Location
  include Mongoid::Document

  field :kdastr_id, type: Integer # optional
  field :use_kdastr, type: Boolean # optional
  field :region, type: String
  field :district, type: String # optional
  field :populated_area, type: String # optional
  field :street_type, type: String
  field :street_name, type: String
  field :house_number, type: String
  field :apartment, type: String
  field :zip_url, type: String
  field :status, type: String, default: 'в обработке'
  field :search_ui, type: Integer

  embedded_in :search_query
  # validates :region, :street_type, :street_name, :house_number, :apartment, :zip_url, presence: true
end

# required date_request: yyyy-dd-MMThh:mm:ss (or some like this)
# required date_response: yyyy-dd-MMThh:mm:ss (or some like this)
