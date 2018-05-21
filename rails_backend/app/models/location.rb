# frozen_string_literal: true

class Location
  include Mongoid::Document
  field :city, type: String
  field :street, type: String
  field :house, type: String
  embedded_in :search_query
end
