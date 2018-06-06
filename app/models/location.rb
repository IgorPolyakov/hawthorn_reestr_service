# frozen_string_literal: true

class Location
  include Mongoid::Document
  include Mongoid::Timestamps
  after_save :run_zip_loader

  field :kdastr_id, type: String # optional
  field :use_kdastr, type: Boolean, default: false # optional
  field :region, type: String, default: 'Томская область'
  field :district, type: String # optional
  field :populated_area, type: String # optional
  field :street_type, type: String
  field :street_name, type: String
  field :house_number, type: String
  field :apartment, type: String
  field :zip_url, type: String
  field :status, type: String, default: 'запуск'
  field :search_uid, type: String
  field :root_path, type: String, default: ''

  embedded_in :search_query
  # validates :region, :street_type, :street_name, :house_number, :apartment, :zip_url, presence: true

  private

  def run_zip_loader
    if status == 'в обработке'
      ZipLoaderWorker.perform_in(2.hours, search_query.id.to_s, id.to_s)
    end
  end
end

# required date_request: yyyy-dd-MMThh:mm:ss (or some like this)
# required date_response: yyyy-dd-MMThh:mm:ss (or some like this)
