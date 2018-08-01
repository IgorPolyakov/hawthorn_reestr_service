# frozen_string_literal: true

class Location
  include Mongoid::Document
  include Mongoid::Timestamps

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
  field :log_path, type: String, default: ''

  embedded_in :search_query
  # validates :region, :street_type, :street_name, :house_number, :apartment, :zip_url, presence: true
  def log
    File.exist?(log_path) ? File.read(log_path) : 'Нет доступных журналов'
  end
end
