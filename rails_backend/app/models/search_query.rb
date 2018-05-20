class SearchQuery
  include Mongoid::Document
  field :search_uid, type: String
  embeds_many :address
  accepts_nested_attributes_for :address
end
