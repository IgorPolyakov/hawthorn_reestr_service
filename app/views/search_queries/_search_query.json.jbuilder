# frozen_string_literal: true

json.array! @search_query do |sq|
  json.id sq.id.to_s
  json.title sq.title
  json.status sq.status
  json.created_at sq.created_at
  json.location sq.locations do |location|
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
    json.pdf_url location.pdf_url
    json.xml_url location.xml_url
    json.short_address location.short_address
    json.object_type location.object_type
    json.updated_at location.updated_at
  end
end
