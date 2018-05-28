# frozen_string_literal: true

class HardWorker
  include Sidekiq::Worker

  def perform(search_query_id, location_id)
    search_query = SearchQuery.find(search_query_id)
    location = search_query.locations.find(location_id)
    data = {
      id: search_query_id,
      id_location: location_id,
      kdastr_id: location.kdastr_id, # null,
      use_kdastr: location.use_kdastr, # false,
      region: location.region, # "Томская область",
      district: location.district, # null,
      populated_area: location.populated_area, # null,
      street_type: location.street_type, # "Улица",
      street_name: location.street_name, # "Красноармейская",
      house_number: location.house_number, # "148",
      apartment: location.apartment # "26"
    }.to_json
    text = "python3 #{Rails.root.join('selenium_py', 'query_sender.py')} -v -http -q [#{data}]"
    system(text)
  end
end
