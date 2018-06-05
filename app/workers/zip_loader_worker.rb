# frozen_string_literal: true

class ZipLoaderWorker
  include Sidekiq::Worker

  def perform(search_query_id, location_id)
    search_query = SearchQuery.find(search_query_id)
    location = search_query.locations.find(location_id)
    data = {}

    data[:id] = search_query_id
    data[:location_id] = location_id
    data[:search_uid] = location.search_uid

    pp "python3 #{Rails.root.join('selenium_py', 'zip_loader.py')} -v -http -q '[#{data.to_json}]'"
    `python3 #{Rails.root.join('selenium_py', 'zip_loader.py')} -v -http -q '[#{data.to_json}]'`
    # `curl -v -H "Accept: application/json" -H "Content-type: application/json" -X PATCH -d '{"location":{"status":"готово"}}' http://127.0.0.1:3000/search_queries/#{search_query_id}/locations/#{location_id}`

    status = SearchQuery.find(search_query_id).locations.find(location_id).status
    raise 'wait for zip archive' unless status == 'готово'
  end
end
