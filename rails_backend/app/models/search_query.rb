# frozen_string_literal: true

class SearchQuery
  include Mongoid::Document
  field :search_uid, type: String
  field :title, type: String
  embeds_many :locations
  accepts_nested_attributes_for :locations

  def status
    total = locations.inject(0) { |sum, loc| sum += 1 if loc.status == 'готово' }.to_i
    "#{total}/#{locations.count}"
  end
end
