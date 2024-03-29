# frozen_string_literal: true

json.set! :search_query do
  json.id @search_query.id.to_s
  json.title @search_query.title
  json.created_at @search_query.created_at
  json.location @search_query.locations do |location|
    json.id location.id.to_s
    json.kdastr_id location.kdastr_id
    json.use_kdastr location.use_kdastr
    json.region location.region
    json.district location.district
    json.populated_area location.populated_area
    json.street_type location.street_type
    json.street_name location.street_name
    json.house_number location.house_number
    json.apartment location.apartment
    json.zip_url location.zip_url
    json.status location.status
    json.search_uid location.search_uid
    json.root_path location.root_path
    json.updated_at location.updated_at
  end
end
