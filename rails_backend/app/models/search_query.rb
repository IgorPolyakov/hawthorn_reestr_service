# frozen_string_literal: true

class SearchQuery
  include Mongoid::Document
  field :search_uid, type: String
  field :title, type: String
  field :status, type: String, default: 'в обработке'
  embeds_many :locations
  accepts_nested_attributes_for :locations
end
