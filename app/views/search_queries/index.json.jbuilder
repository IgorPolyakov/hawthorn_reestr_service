# frozen_string_literal: true

json.array! @search_queries do |sq|
  json.id sq.id.to_s
  json.title sq.title
  json.created_at sq.created_at
  json.location sq.locations do |location|
    json.id location.id.to_s
    json.kdastr_id location.kdastr_id
    json.region location.region
    json.district location.district
    json.populated_area location.populated_area
    json.street_type location.street_type
    json.street_name location.street_name
    json.house_number location.house_number
    json.apartment location.apartment
    json.zip_url location.zip_url
    json.status location.status
    json.search_ui location.search_ui
  end
end
