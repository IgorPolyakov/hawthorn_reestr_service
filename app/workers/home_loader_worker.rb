# frozen_string_literal: true

class HomeLoaderWorker
  include Sidekiq::Worker

  def perform(search_query_id, location_id)
    search_query = SearchQuery.find(search_query_id)
    location = search_query.locations.find(location_id)
    data = {}

    data[:id] = search_query_id
    data[:location_id] = location_id
    data[:kdastr_id] = location.kdastr_id == '' ? nil : location.kdastr_id # null
    data[:use_kdastr] = location.use_kdastr == '' ? nil : location.use_kdastr # false
    data[:region] = location.region == '' ? nil : location.region # "Томская область"
    data[:district] = location.district == '' ? nil : location.district # null
    data[:populated_area] = location.populated_area == '' ? nil : location.populated_area # null
    data[:street_type] = location.street_type == '' ? nil : location.street_type # "Улица"
    data[:street_name] = location.street_name == '' ? nil : location.street_name # "Красноармейская"
    data[:house_number] = location.house_number == '' ? nil : location.house_number # "148"
    data[:apartment] = location.apartment == '' ? nil : location.apartment # "26"

    pp "python3 #{Rails.root.join('selenium_py', 'home_loader.py')} -v -http -q '[#{data.to_json}]'"
    `python3 #{Rails.root.join('selenium_py', 'home_loader.py')} -v -http -q '[#{data.to_json}]'`
    # `curl -v -H "Accept: application/json" -H "Content-type: application/json" POST -d '{ "search_query" : { "title" : "some_title", "locations_attributes" : { "0" : { "kdastr_id" : "88005553535", "use_kdastr" : "true" }, "1" : { "kdastr_id" : "88005553536", "use_kdastr" : "true" } } } }' http://127.0.0.1:3000/search_queries.json`
    # status = SearchQuery.find(search_query_id).locations.find(location_id).status
  rescue Mongoid::Errors::DocumentNotFound
  end
end
